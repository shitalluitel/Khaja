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
        if(parseInt(data) <= 0){
          document.title ="Khaja";
        }else{
          document.title ="("+data+") Khaja";
        }
        if(pre_data < parseInt(data) && flag){
          pre_data = parseInt(data);
          flag = true;
          toastr.warning("<i class=\"fa fa-bell\" style=\"margin-left:-30px;\"></i>&nbsp; &nbsp; &nbsp;<strong >"+ data +" </strong> &nbsp;new order detected.");
        }
        if(!flag && pre_data < parseInt(data)){
          pre_data = parseInt(data);
          flag = true;
        }
        flag = false;
      },
      type: 'GET'
    });
  },1000 * 30 );
}

async function asyncCall() {
  var result = await get_data();
}

asyncCall();
