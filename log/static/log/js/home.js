require(['jquery'], function($){

    var form = $('form#login');
    form.on('submit', function(e) {
        e.preventDefault();
        var url = this.action;
        var data = $(this).serialize();
        $.post(url, data, function(response) {
            var msg = JSON.parse(response);
            if (msg.status === 401) {
                form.find('#error-message').text(msg.error);
            } else if (msg.status === 200){
                window.location.href = msg.redirect_url
            }

        });
    });

});
