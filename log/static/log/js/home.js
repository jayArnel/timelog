require(['jquery'], function($){

    var form = $('form#login');
    form.on('submit', function(e) {
        e.preventDefault();
        $.ajax({
            url: this.action,
            type: this.method,
            data: $(this).serialize(),
            success: function(response) {
                var msg = JSON.parse(response);
                if (msg.status === 401) {
                    form.find('input#password').val('');
                    form.find('.btn').val('Submit');
                    form.find('.btn').prop('disabled', false);
                    form.find('input#username').focus();
                    form.find('#error-message').text(msg.error);
                } else if (msg.status === 200){
                    window.location.href = msg.redirect_url
                }
            },
            xhr: function() {
                var request = $.ajaxSettings.xhr();
                form.find('.btn').prop('disabled', true);
                form.find('.btn').val('Logging in');
                return request;
            }
        });
    });


});
