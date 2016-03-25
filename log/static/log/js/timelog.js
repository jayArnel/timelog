require(['jquery', 'cookies'], function($, cookies){
    var container = $('.container#timelog');

    /**
     * Handle logging of time
     * @param  {[Event]} e [description]
     * @return none
     */
    function time(e){
        e.preventDefault();
        var pk = container.data('user');
        var _this = $(this);
        $.ajax({
            url: '/time/',
            type: 'post',
            data: {'pk': pk},
            beforeSend: function(xhr, settings) {
                var csrftoken = cookies.get('csrftoken');
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            success: function(response) {
                var msg = JSON.parse(response);
                _this.toggleClass('timein timeout');
                _this.html(msg.text);
            },
        })
    }

    /**
     * Bind actions in timelog page
     * @return none
     */
    (function bindActions() {
        container.find('#time').on('click', time);
    })();

});
