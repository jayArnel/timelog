require(['jquery', 'cookies'], function($, cookies){
    var container = $('.container#timelog');

    /**
     * Add a log instance for the user
     * @param  {[Event]} e [description]
     * @return none
     */
    function timein(e){
        e.preventDefault();
        var pk = container.data('user');
        $.ajax({
            url: $(this).attr('href'),
            type: 'post',
            data: {'pk': pk},
            beforeSend: function(xhr, settings) {
                var csrftoken = cookies.get('csrftoken');
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            success: function(response) {
                console.log('timed in');
            },
        })
    }

    function timeout(e){
        e.preventDefault();
        var pk = container.data('user');
        $.ajax({
            url: $(this).attr('href'),
            type: 'post',
            data: {'pk': pk},
            beforeSend: function(xhr, settings) {
                var csrftoken = cookies.get('csrftoken');
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            success: function(response) {
                console.log('timed out');
            },
        })
    }

    /**
     * Bind actions in timelog page
     * @return none
     */
    (function bindActions() {
        container.find('#timein').on('click', timein);
        container.find('#timeout').on('click', timeout);
    })();

});
