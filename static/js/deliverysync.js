function get_order_data(){
  var pre_data = 0;
  var flag = false;
  setInterval(function(){
    jQuery.ajax({
      url: '/delivery/notification/',
      cache: false,
      error: function () {
        console.log("error");
      },
      success: function (data) {
        $('.notification-new').html(data['new']);
        $('.notification-prepared').html(data['prepared']);
      },
      type: 'GET'
    });
  },1000 * 30);
}

async function asyncdeliveryCall() {
  var result = await get_order_data();
  jQuery.ajax({
    url: '/delivery/notification/',
    cache: false,
    error: function () {
      console.log("error");
    },
    success: function (data) {
      $('.notification-new').html(data['new']);
      $('.notification-prepared').html(data['prepared']);
    },
    type: 'GET'
  });
}

asyncdeliveryCall();
