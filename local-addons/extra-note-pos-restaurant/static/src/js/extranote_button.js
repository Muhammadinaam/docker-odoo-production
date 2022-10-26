alert('aaddbb')
odoo.define('extra_note_pos_restaurant.OrderExtraNoteButton', function (require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const { useListener } = require('web.custom_hooks');
    const Registries = require('point_of_sale.Registries');

    class OrderExtraNoteButton extends PosComponent {
        constructor() {
            super(...arguments);
            useListener('click', this.onClick);
        }
        async onClick() {
            const currentExtraNote = this.env.pos.get_order().extra_note

            const { confirmed, payload: inputNote } = await this.showPopup('TextAreaPopup', {
                startingValue: currentExtraNote,
                title: this.env._t('Add Extra Note'),
            });

            if (confirmed) {
                var order = this.env.pos.get_order();
                order.extra_note = inputNote;
                order.trigger('change');
            }
        }

        get_extra_note() {
            var order = this.env.pos.get_order();

            if (order && order.extra_note) {
                return 'Extra note: ' + order.extra_note;
            }
            return 'Extra note: ';
        }
    }
    OrderExtraNoteButton.template = 'OrderExtraNoteButton';
    ProductScreen.addControlButton({

        component: OrderExtraNoteButton,
        condition: function () {
            return true;
        },
        position: ['before', 'SetPricelistButton'],
    });

    Registries.Component.add(OrderExtraNoteButton);
    return OrderExtraNoteButton;
});
