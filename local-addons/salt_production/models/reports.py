from datetime import datetime, timedelta

from odoo import api, fields, models, tools


def get_periods_query(base_query, periods=None, group_by=''):
    periods = periods or [
        ("Today", "where date(time) = CURRENT_DATE"),
        (
            "This month to date",
            "where date(time) <= CURRENT_DATE and "
            f"date(time) >= '{(datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')}'"
        ),
        (
            "This year to date",
            "where date(time) <= CURRENT_DATE and "
            f"date(time) >= '{(datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')}'"
        ),
        ("Overall to date", "where date(time) <= CURRENT_DATE"),
    ]

    queries = []
    id = 1
    for period_name, where_query in periods:
        query = base_query.replace("<PERIOD>", period_name)
        query = query.replace("<ID>", str(id))
        query = f'{query} {where_query} {group_by}'
        queries.append(query)
        id += 1

    return " UNION ALL ".join(queries)


class WashingReportPeriodsSummary(models.Model):
    _name = 'salt_production.washing_report_periods_summary'
    _description = 'salt_production.washing_report_periods_summary'
    _auto = False

    period = fields.Char(string="Period")
    crystalizer_id = fields.Many2one(
        'salt_production.crystalizer',
        'Crystalizer'
    )
    effective_working_hours = fields.Float(string='Effective working hours')
    
    total_production = fields.Float(string='Total production')
    productivity_per_hour = fields.Float(string='Productivity per hour')
    total_washing_losses = fields.Float(string='Total washing losses')
    water_load_salt_losses = fields.Float(string='Water load salt losses')
    washing_losses = fields.Float(string='Washing losses')

    def init(self):

        base_query = """
        select CAST('<ID>' AS text) as "id",
        CAST('<PERIOD>' AS text) as "period",
        sum(effectivehr) as "effective_working_hours",
        salt_production_crystalizer.id as crystalizer_id,
        
        sum(net_salt_produced) as "total_production",
        sum(net_salt_produced)/sum(effectivehr) as "productivity_per_hour",
        sum(waterloadloss) + sum(washinglosscalc) as "total_washing_losses",
        sum(waterloadloss) as "water_load_salt_losses",
        sum(washinglosscalc) as "washing_losses"
        from salt_production_washing
        left join salt_production_crystalizer on
        salt_production_crystalizer.id = salt_production_washing.crystalizer_id
        """

        query = get_periods_query(
            base_query, None, 'group by salt_production_crystalizer.id')

        tools.drop_view_if_exists(
            self._cr, 'salt_production_washing_report_periods_summary')

        report_query = f"""
            CREATE OR REPLACE VIEW
            salt_production_washing_report_periods_summary AS (
                {query}
            )"""
        print(report_query)
        self._cr.execute(report_query)


class RefinaryReportPeriodsSummary(models.Model):
    _name = 'salt_production.refinary_report_periods_summary'
    _description = 'salt_production.refinary_report_periods_summary'
    _auto = False

    period = fields.Char(string="Period")
    crystalizer_id = fields.Many2one(
        'salt_production.crystalizer',
        'Crystalizer'
    )
    salt_input = fields.Float(string='Salt input (MTons)')
    total_production = fields.Float(string='Total production (MTons)')

    coarse_salt = fields.Float(string='Coarse salt (MTons)')
    fine_salt = fields.Float(string='Fine salt (MTons)')
    coarse_and_fine_salt = fields.Float(string='Coarse + Fine salt (MTons)')
    powder_salt = fields.Float(string='Powder salt (MTons)')

    effective_working_hours = fields.Float(string='Effective working hours')
    productivity_per_hour = fields.Float(string='Productivity per hour')
    production_losses = fields.Float(string='Production losses')

    def init(self):

        base_query = """
        select CAST('<ID>' AS text) as "id",
         CAST('<PERIOD>' AS text) as "period", sum(effectivehr)
          as "effective_working_hours",
        salt_production_crystalizer.id as crystalizer_id,
        sum(rawincome) as "salt_input",

        sum(coarse) as "coarse_salt",
        sum(finesalt) as "fine_salt",
        sum(coarse_and_fine) as "coarse_and_fine_salt",
        sum(powdersalt) as "powder_salt",
        sum(totalrefine) as "total_production",

        (sum(totalrefine))/sum(effectivehr)
         as "productivity_per_hour",
        sum(lossrefine) as "production_losses"
        from salt_production_refine
        left join salt_production_crystalizer on
        salt_production_crystalizer.id = salt_production_refine.crystalizer_id
        """

        query = get_periods_query(
            base_query, None, 'group by salt_production_crystalizer.id')

        tools.drop_view_if_exists(
            self._cr, 'salt_production_refinary_report_periods_summary')

        report_query = f"""
            CREATE OR REPLACE VIEW
            salt_production_refinary_report_periods_summary AS (
                {query}
            )"""
        print(report_query)
        self._cr.execute(report_query)


class ActualAndProjectedProduction(models.Model):
    _name = 'salt_production.actual_and_projected_report'
    _auto = False

    month = fields.Datetime(string="Month")
    crystalizer_id = fields.Many2one(
        'salt_production.crystalizer',
        'Crystalizer'
    )
    cycle = fields.Char(string="Cycle")
    actual_production = fields.Float(string='Actual production')
    projected_production = fields.Float(string='Projected production')
    variance = fields.Float(string='Variance')
    efficiency = fields.Float(string='Efficiency')

    def init(self):

        query = """
        select ap.month as id, ap.*, pp.projected_production, 
        ap.actual_production - pp.projected_production as variance,
        (ap.actual_production - pp.projected_production)*100/NULLIF(pp.projected_production,0) as efficiency from (

        select DATE_TRUNC('month', ap.time) as month,
        ap.crystalizer_id, ap.cycle, sum(ap.net_salt_produced) as actual_production from salt_production_washing ap
        group by DATE_TRUNC('month', ap.time), ap.crystalizer_id, ap.cycle

        ) ap left join (

        select DATE_TRUNC('month', pp.time) as month,
        pp.crystalizer_id, pp.cycle, sum(pp.projected) as projected_production from salt_production_projectedprod pp
        group by DATE_TRUNC('month', pp.time), pp.crystalizer_id, pp.cycle

        ) pp
        on pp.month = ap.month and pp.crystalizer_id = ap.crystalizer_id and pp.cycle = ap.cycle
        """

        tools.drop_view_if_exists(
            self._cr, 'salt_production_actual_and_projected_report')

        report_query = f"""
            CREATE OR REPLACE VIEW
            salt_production_actual_and_projected_report AS (
                {query}
            )"""
        print(report_query)
        self._cr.execute(report_query)


class ActualAndProjectedWashingProductionGraph(models.Model):
    _name = 'salt_production.actual_and_projected_washing_production_graph'
    _auto = False

    month = fields.Datetime(string="Month")
    production_type = fields.Char(string="Production type")
    crystalizer_id = fields.Many2one(
        'salt_production.crystalizer',
        'Crystalizer'
    )
    cycle = fields.Char(string="Cycle")
    production = fields.Float(string='Production')

    def init(self):

        query = """
        select ROW_NUMBER() OVER() as id, t.* from (

        select DATE_TRUNC('month', ap.time) as month, cast('Actual' as TEXT) as production_type,
        ap.crystalizer_id, ap.cycle, sum(ap.net_salt_produced) as production from salt_production_washing ap
        group by DATE_TRUNC('month', ap.time), ap.crystalizer_id, ap.cycle

        UNION ALL

        select DATE_TRUNC('month', pp.time) as month, cast('Projected' as TEXT) as production_type,
        pp.crystalizer_id, pp.cycle, sum(pp.projected) as production from salt_production_projectedprod pp
        group by DATE_TRUNC('month', pp.time), pp.crystalizer_id, pp.cycle
        ) t
        """

        tools.drop_view_if_exists(
            self._cr, 'salt_production_actual_and_projected_washing_production_graph')

        report_query = f"""
            CREATE OR REPLACE VIEW
            salt_production_actual_and_projected_washing_production_graph AS (
                {query}
            )"""
        print(report_query)
        self._cr.execute(report_query)
