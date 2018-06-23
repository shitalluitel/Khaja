var pre_data = 0;

function get_data(){
  setInterval(function(){
    jQuery.ajax({
      url: '/company/notification/',
      cache: false,
      error: function () {
        console.log("error");
      },
      success: function (data) {
        $('.notification').html(data);
        if (pre_data != data){
          pre_data = data;
          toastr.warning("New order has been placed.");
        }
        // console.log(data);
      },
      type: 'GET'
    });
  },1000 * 60);
}

async function asyncCall() {
  var result = await get_data();
}

asyncCall();
