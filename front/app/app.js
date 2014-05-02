/* App */

define(['backbone'],function(Backbone) {
	'use strict';

	var App = _.extend({
		'config': require.appConfig,
		'initialize': function(){
			require(
				['router','views/base', 'views/leaf'],
				function(Router, BaseView, LeafView){

					/*Router initialisation*/
					this.Router = Router;

					this.view = new BaseView();
                    //this.view.render(routeView, '#depth-1');
                    /*this.view.render( new HeaderView().render(), '#header');
                    this.view.render( new FooterView().render(), '#footer');
                    */

    				Backbone.history.start({ pushState: true });
					return this;
				}.bind(this)
			);
		}
	});
	window.App = App;
	return App;

});
