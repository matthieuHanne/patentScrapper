/*global define Leaf View*/
define(['backbone'],
		function(Backbone){
			'use strict';

			var view = Backbone.View.extend({
				'tagName'	: 'section',
				'initialze'	: function(){
				},
				'render'	: function(tpl){
					this.$el.html(_.template(tpl)); 
					return this;
				},
				'events': {
					'click .add-keyword'	: 'addKeywordRow',
				'click .start-search' 	: 'startSearch',
				'click .start-crawl'	: 'startCrawl',
				},
				'addKeywordRow' : function(event){
					$('.col-xs-3:first-child').clone().appendTo('.keywords');
				},
				'startSearch' : function(event){
					//TODO: Alert
					//Request to API
					var keys=[]; 
					$('.keyword').each(function(){keys.push($(this).val())})
						var param='';
					$('.param').each(function(){if($(this).prop('checked')) param +=$(this).val()})
						var bdd='';
					$('.bdd').each(function(){if($(this).prop('checked')) bdd +=$(this).val()})


						$.ajax({
							type: 'POST',
							url: App.config.apiUrl+'/patentapi/export',
							crossDomain: true,
							data: JSON.stringify({keywords: keys, args: param, target: bdd }),
							contentType: 'application/json',
							success: function(responseData, textStatus, jqXHR) {
								var value = responseData.someKey;
								App.Router.navigate('dashboard', {trigger: true})
							},
							error: function (responseData, textStatus, errorThrown) {
								console.log( "ERROR:", error );

							}
						});
				},
				'startCrawl' : function(event){
					//TODO: Alert
					//Request to API
					var keys=[]; 
					$('.keyword').each(function(){keys.push($(this).val())})
						var param='';
					$('.param').each(function(){if($(this).prop('checked')) param +=$(this).val()})
						var bdd='';
					$('.bdd').each(function(){if($(this).prop('checked')) bdd +=$(this).val()})

						$.post(App.config.apiUrl+'/patentapi/crawl',{'keywords[]': keys, 'args': param, 'target': bdd })
						.done(function(responseData){
							App.Router.navigate('dashboard', {trigger: true})
						})
					.fail(function() {
						alert( "Post failed" );
						App.Router.navigate('dashboard', {trigger: true})
					});
				},
			});

			return view;
		});
