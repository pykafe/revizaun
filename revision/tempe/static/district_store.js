function DistrictStore() {

    var self = this;

    riot.observable(self)

    self.on('district_please', function(){
        console.log('district_please has been heard by another store');
    });
}
