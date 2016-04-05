(function(config) {
    if (window.hasOwnProperty('require')) {
        require.config(config);
    } else {
        window.require = config;
    }
})({
    baseUrl: '/static/core/js',
    paths: {
        jquery: 'jquery-1.11.3.min',
        stapes: 'stapes-0.8.1-min',
        cookies: 'cookies',
        model: 'model',
    }
});
