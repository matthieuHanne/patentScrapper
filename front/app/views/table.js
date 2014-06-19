
/*global define Leaf View*/
define(['backbone'],function(Backbone){
    'use strict';
    var view = Backbone.View.extend({
        'tagName'	: 'section',
        'initialize'	: function(){
        },
        render: function (tpl) {
            this.$el.html(tpl);
            return this;
        },

    });
    return view;
});
