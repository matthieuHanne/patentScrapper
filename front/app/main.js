/* require initialisation*/
require.config({
    'baseUrl': require.appConfig.host,
    'paths': {
        'backbone': 'lib/backbone-min',
        'app': 'app/app',
        'router': 'app/router',
        'views': 'app/views',
        'tpl': 'app/templates',
        'underscore': 'lib/lodash',
    },
    'shim': {
        'backbone': {
            'deps': [
                'underscore',
                'lib/jquery.min',
            ],
            'exports': 'Backbone'
        },
    }
});

define(['app'],
    function(App) {
    App.initialize();
});
