/*global define Leaf View*/
define(['backbone'],
        function(Backbone){
            'use strict';

            var view = Backbone.View.extend({
                'tagName'	: 'section',
                'initialze'	: function(){
                },
                'render'	: function(tpl){
                        var template = _.template(tpl);
                        this.$el.html(template); 
                    $.get(App.config.apiUrl+'/patentapi/base',function(bases){
                        for(var i=0; i <  bases.key.length; i++){
                           $('tbody').append("<tr><td>"+bases.key[i]+"</td><tr>")
                        }
                    }.bind(this));

                    return this;
                },
                'events': {
                    'click .add-keyword'	: 'addKeywordRow',
                'click .start-search' 	: 'startSearch',
                'click .start-crawl'	: 'startCrawl',
                'click .update-keyword'	: 'updateKeyword',
                'click .show-databases' : 'showDatabases',
                },
                'showDatabases' : function(event){
                    require(['views/table','text!tpl/table.html'],function(table, tpl){
                        App.view.render(new table().render(tpl), '#depth-3');
                        $("#dirty").append($('#base').val());
                        $.post(App.config.apiUrl+'/patentapi/keyword', {base:$('#base').val()},function(data){
                            $('#bases-keyword').empty()
                            for(var i=0; i <  data.key.length; i++){
                               $('#bases-keyword').append("<tr><td>"+i+"</td><td>"+data.key[i]+"</td><tr>")
                            }
                        });
                    });

                },
                'updateKeyword' : function(event){
                    var database = $('#base').val();
                    if(database !== "" ){
                        $('.alert-base').hide();
                    }
                    else{
                        $('.alert-base').show();
                    }
                },
                'addKeywordRow' : function(event){
                    $('.col-xs-6:first-child').clone().appendTo('.keywords');
                },
                'startSearch' : function(event){
                    //Prepare request content
                    var keys=''; 
                    var param='';
                    var bdd='';
                    $('.keyword').each(function(){keys+=$(this).val()+' ';});
                    $('.param').each(function(){if($(this).prop('checked')) param+=$(this).val()});
                    $('.bdd').each(function(){if($(this).prop('checked')) bdd+=$(this).val()});
                    //Send get request
                    $.post(App.config.apiUrl+'/patentapi/export',
                            {keywords: keys, args: param, mail: $('#mail').val(), base:$('#base').val()});
                    App.Router.navigate('dashboard', {trigger: true})
                },
                'startCrawl' : function(event){
                    //Prepare request content
                    var keys=''; 
                    var param='';
                    var bdd='';
                    var base='';
                    $('.keyword').each(function(){keys+=$(this).val()+' '});
                    $('.param').each(function(){if($(this).prop('checked')) param+=$(this).val()});
                    $('.bdd').each(function(){if($(this).prop('checked')) bdd+=$(this).val()});
                    //Send get request
                    $.post(App.config.apiUrl+'/patentapi/number',{keywords: keys}, function(data){
                        if(data.count <= 1000){
                            $.post(App.config.apiUrl+'/patentapi/crawl',
                                {keywords: keys, export_config: param, mail_to: $('#email').val(), databases: bdd,base:$('#base').val()});
                            App.Router.navigate('dashboard', {trigger: true})    
                        }
                        else{alert("Vous tentez de scaper plus de 1000 brevets! Requete abandonnée")}
                    });

                }
            });

            return view;
        });
