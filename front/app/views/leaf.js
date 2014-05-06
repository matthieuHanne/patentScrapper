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
                'addKeywordRow' : function(event ){
                    $('.col-xs-3:first-child').clone().appendTo('.keywords');
                },
                'startSearch' : function(event){
                    //Prepare request content
                    var keys=''; 
                    var param='';
                    var bdd='';
                    $('.keyword').each(function(){keys+=$(this).val()+' '});
                    $('.param').each(function(){if($(this).prop('checked')) param+=$(this).val()});
                    $('.bdd').each(function(){if($(this).prop('checked')) bdd+=$(this).val()});
                    //Send get request
                    $.post(App.config.apiUrl+'/patentapi/export',
                    {keywords: keys, args: param, mail: this.$el.find('#mail').val()},
                    function(data){console.log(data.result)});
                },
                'startCrawl' : function(event){
                    //Prepare request content
                    var keys=''; 
                    var param='';
                    var bdd='';
                    $('.keyword').each(function(){keys+=$(this).val()+' '});
                    $('.param').each(function(){if($(this).prop('checked')) param+=$(this).val()});
                    $('.bdd').each(function(){if($(this).prop('checked')) bdd+=$(this).val()});
                    //Send get request
                    $.post(App.config.apiUrl+'/patentapi/crawl',
                    {keywords: keys, export_config: param, mail_to: this.$el.find('#email').val(), databases: bdd},
                    function(data){console.log(data.result)});

                }
            });

            return view;
        });
