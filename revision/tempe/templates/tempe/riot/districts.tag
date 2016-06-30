<districts>
    <h1>Districts</h1>
    <div each={ districts }>
      { name }
    </div>

    var self = this
    self.districts = []

    self.on('mount', function(){
        RiotControl.trigger('request_districts')
    })

    RiotControl.on('districts', function(data){
        self.districts = data
        self.update()
    })
</districts>
