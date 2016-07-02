function DistrictStore() {

    var self = this;

    riot.observable(this)

    self.get_requests = 0


    self.on('district_please', function(){
        console.log('district_please has been heard by another store');
        self.get_requests++;
        console.log('requests ' + self.get_requests);
        $.get('/api/districts/', function(data){
            self.districts = data.results
            self.get_requests--;
            console.log('requests ' + self.get_requests);
            self.are_we_done();
        })
        self.get_requests++;
        console.log('requests ' + self.get_requests);
        $.get('/api/subdistricts/', function(data){
            self.subdistricts = data.results
            self.get_requests--;
            console.log('requests ' + self.get_requests);
            self.are_we_done();
        })
        self.get_requests++;
        console.log('requests ' + self.get_requests);
        $.get('/api/sucos/', function(data){
            self.sucos = data.results
            self.get_requests--;
            console.log('requests ' + self.get_requests);
            self.are_we_done();
        })
        self.get_requests++;
        console.log('requests ' + self.get_requests);
        $.get('/api/aldeias/', function(data){
            self.aldeias = data.results
            self.get_requests--;
            console.log('requests ' + self.get_requests);
            self.are_we_done();
        })
        self.get_requests++;
        console.log('requests ' + self.get_requests);
        $.get('/api/visitors/', function(data){
            self.visitors = data.results
            self.get_requests--;
            console.log('requests ' + self.get_requests);
            self.are_we_done();
        })
    });

    self.are_we_done = function(){
        if(self.get_requests == 0){
            console.log("we are done");
            self.trigger("districts",{
                districts: self.districts, 
                subdistricts: self.subdistricts, 
                sucos: self.sucos,
                aldeias: self.aldeias,
                visitors: self.visitors})
        }else{
            console.log("Seidauk");
        }
    }

}
