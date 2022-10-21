odoo.define('pos_order_types.models', function (require) {
"use strict";

var models = require('point_of_sale.models');




models.load_models({
    model: 'delivery.type',
    fields: ['name'],
    domain: function(self){ return [['id','in',self.config.delivery_methods]]; },
    loaded: function(self,delivery_methods){
        self.delivery_methods = delivery_methods;
    }
});

    var _super_order = models.Order;

    models.Order = models.Order.extend({
        initialize: function (attr, options) {
            _super_order.prototype.initialize.call(this, attr, options);
            this.delivery_method = this.delivery_method || false;
        },
        export_as_JSON: function(){
            var json = _super_order.prototype.export_as_JSON.apply(this,arguments);
            json.delivery_method = this.delivery_method || false;
            json.delivery_method_id  = this.delivery_method ? this.delivery_method.id : false;
            return json;
        },
        init_from_JSON: function(json){
            _super_order.prototype.init_from_JSON.apply(this,arguments);
            this.delivery_method = json.delivery_method || false;

        },
    });


});