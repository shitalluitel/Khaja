function get_data(){
  var pre_data = 0;
  var flag = false;
  setInterval(function(){
    jQuery.ajax({
      url: '/company/notification/',
      cache: false,
      error: function () {
        console.log("error");
      },
      success: function (data) {
        $('.notification').html(data);
        if(pre_data < data && flag){
          pre_data = data;
          toastr.warning("<i class=\"fa fa-bell\" style=\"margin-left:-30px;\"></i>&nbsp; &nbsp; &nbsp;<strong >"+ data +" </strong> &nbsp;new order detected.");
        }else if(!flag){
          pre_data = data;
        }
        flag = true;
      },
      type: 'GET'
    });
  },1000 * 60);
}

async function asyncCall() {
  var result = await get_data();
}

asyncCall();
