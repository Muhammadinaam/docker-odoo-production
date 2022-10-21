odoo.define('pos_order_types.pos_delivery_method',function(require) {
    "use strict";

    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const { useListener } = require('web.custom_hooks');
    const { useState, useRef } = owl.hooks;
    const { Gui } = require('point_of_sale.Gui');




class SetDeliveryMethodButton extends PosComponent {

        constructor() {
            super(...arguments);
            useListener('click', this.button_click);
        }

        async button_click() {
            var orders = this.env.pos.orders;


            var no_delivery_method = [{
            label: this.env._t("None"),
        }];
        const currentdelivery_method = this.env.pos.get_order().delivery_method

        const selection_list = [
                {
                    id: -1,
                    label: this.env._t('None'),
                    isSelected: !currentdelivery_method,
                },
            ];
            for (let del_meth of this.env.pos.delivery_methods) {
                selection_list.push({
                    id: del_meth.id,
                    label: del_meth.name,
                    isSelected: currentdelivery_method
                        ? del_meth.id === currentdelivery_method.id
                        : false,
                    item: del_meth,
                });
            }



             const { confirmed, payload: selected_delivery_method } = await this.showPopup(
                'SelectionPopup',
                {
                    title: this.env._t('Select Order Type'),
                    list: selection_list,
                }

            );
                if (confirmed){
                    var order = this.env.pos.get_order();
                    order.delivery_method = selected_delivery_method;
                    order.trigger('change');

                }

        }

        get_current_delivery_method_name(){
            var name = this.env._t('Order Types');
            var order = this.env.pos.get_order();

            if (order) {
                var delivery_method = order.delivery_method;

                if (delivery_method) {
                    name = delivery_method.name;
                }
            }
             return name;
        }

}


SetDeliveryMethodButton.template = 'SetDeliveryMethodButton';
ProductScreen.addControlButton({

        component: SetDeliveryMethodButton,
        condition: function () {
            return true;
        },
        position: ['before', 'SetPricelistButton'],
    });

    Registries.Component.add(SetDeliveryMethodButton);
    return SetDeliveryMethodButton;



});