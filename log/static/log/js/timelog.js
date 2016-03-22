require(['jquery', 'cookies'], function($, cookies){
    var container = $('.container#timelog');

    /**
     * Add a log instance for the user
     * @param  {[Event]} e [description]
     * @return none
     */
    function time(e){
        e.preventDefault();
        var pk = container.data('user');
        $.ajax({
            url: '/time/',
            type: 'post',
            data: {'pk': pk},
            beforeSend: function(xhr, settings) {
                var csrftoken = cookies.get('csrftoken');
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            success: function(response) {
                console.log('timed');
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
