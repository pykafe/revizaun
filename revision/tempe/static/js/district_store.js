function DistrictStore(){

    var self = this;

    riot.observable(self)


    self.on('request_districts', function(){
        $.get('/api/districts/', function(data){
            RiotControl.trigger('districts', data.results)
        })
    })

}
