/* Post router*/
define(['app', 'backbone'], function(App, Backbone) {
    'use strict';

			var routes = {
				'routes':{ 
					'': 'index',
					'search': 'search',
					'crawl': 'crawl',
					'dashboard': 'dashboard',
				},
				'index': function(){
                        /*
                        App.view.render((new HomeView()).renderCarousel(), '#container');
                        App.view.render((new HomeView()).renderMarket(), '#container');
                        */
                },
				'crawl': function(){ 
					require(['views/leaf','text!tpl/crawl.html'],function(leaf, tpl){
						App.view.render(new leaf().render(tpl), '#depth-2', 'overwrite');
					});
				},
				'search': function(){ 
					require(['views/leaf','text!tpl/search.html'],function(leaf, tpl){
						App.view.render(new leaf().render(tpl), '#depth-2', 'overwrite');
					});
				},
				'dashboard': function(){
					require(['views/leaf','text!tpl/dashboard.html'],function(leaf, tpl){
						App.view.render(new leaf().render(tpl), '#depth-3');
					});
				}
			};

		return new (Backbone.Router.extend(routes))();
});


