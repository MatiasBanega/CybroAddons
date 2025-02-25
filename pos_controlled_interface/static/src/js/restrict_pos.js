odoo.define('pos_controlled_interface', function(require){
    const NumpadWidget =  require('point_of_sale.NumpadWidget')
    const { patch } = require('web.utils');
//    Patching NumpadWidget  to disable discount and price buttons when the respective filed is enabled.
    patch(NumpadWidget.prototype, 'point_of_sale/static/src/js/Screens/ProductScreen/NumpadWidget.js', {
         mounted() {
             if (this.env.pos.config.control_discount){
                $($('.numpad').find('.mode-button')[2]).removeClass('disable')
             }else{
                $($('.numpad').find('.mode-button')[2]).addClass('disable');
             }
             if (this.env.pos.config.control_price) {
                $($('.numpad').find('.mode-button')[1]).removeClass('disable');
             }else{
                $($('.numpad').find('.mode-button')[1]).addClass('disable');
             }
         },
         changeMode(mode) {
             if (mode === 'discount'  && this.env.pos.config.control_discount) {
                return;
             }
             if (mode === 'price'  && this.env.pos.config.control_price) {
                return;
             }
             this.trigger('set-numpad-mode', { mode });
         }
    })
});
