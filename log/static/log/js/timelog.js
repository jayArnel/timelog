require(['jquery'], function($){
    var container = $('.container#timelog');
    /**
     * Bind actions in timelog page
     * @return none
     */
    (function bindActions() {
        container.find('#timein').on('click', timein);
    })();

    /**
     * Add a log instance for the user
     * @return {[type]} [description]
     */
    function timein(){
        
    }
});