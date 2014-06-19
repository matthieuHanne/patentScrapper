/* Default base view*/

define(['backbone', 'text!tpl/base.html', 'text!tpl/root.html'], function(Backbone, baseTpl, rootTpl){
    'use strict';

    return Backbone.View.extend({
        'id': 'wrapper',
        'tagName': 'div',
		//TODO: Export squeleton to a template
        'initialize': function() {
        	this.$el.html(_.template(baseTpl))
            $(document.getElementsByTagName('body')).append(this.$el);
            this.$el.find('#depth-2').hide();
            this.$el.find('#depth-3').hide();
            this.$el.find('#depth-1').html(_.template(rootTpl)); 
        },

        'render': function(el, target, option){
            if(el instanceof Backbone.View)
                el = el.$el;

            target = target ? this.$el.find(target) : this.$el;
			var effect = 'slide';
			var options = { direction: 'right' };
			var duration = 700;
			//TODO: Refactor need
            if( option === 'overwrite'){
                $('#depth-3').empty().hide();
                target.hide().empty().append(el).slideToggle( "slow" );
			}
            else
                target.hide().empty().append(el).slideToggle( "slow" );

            return this;
        },
		'events': {
			'click .btn' : 'toggleDepth2',
			'click .navigation li' : 'goTo'
		},
		'toggleDepth2': function(event){
			event.preventDefault();
			App.Router.navigate(event.currentTarget.getAttribute("route"), {trigger: true})
		},
    });
});
