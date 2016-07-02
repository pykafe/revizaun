function AlldistrictStore() {

    riot.observable(this)

    var self = this;



    self.on('add_districts', function(newdistrict) {
        debugger;
        $.post('/api/districts/', newdistrict, function(newdistrict){
        });
        $(document).ajaxSuccess(function() {
            $( ".district_log" ).text( "You are successfull to add district." );
        });
        $( document ).ajaxError(function() {
            $( ".district_error_log" ).text( "You aren't successfull to add district." );
        });

    });

}
