function update_notification(){
  jQuery.ajax({
    url: '/company/notification/',
    cache: false,
    error: function () {
      console.log("error");
    },
    success: function (data) {
      $('.notification').html(data);
      document.title ="("+data+") Khaja";
      if(parseInt(data) > 0){
          toastr.warning("<i class=\"fa fa-bell\" style=\"margin-left:-30px;\"></i>&nbsp; &nbsp; &nbsp;<strong >"+ data +" </strong> &nbsp;new order detected.");
      }
    },
    type: 'GET'
  });
}

$('body').on('change','select', function(){
  var queries = {};
  $.each(document.location.search.substr(1).split('&'), function(c,q){
      var i = q.split('=');
      queries[i[0].toString()] = i[1].toString();
  });
    var id = $(this).attr('id');
    var value = $(this).val();
    $.ajax({
        url: '/carts/api/v1/change/status?id='+ id + "&value="+value+"&next="+queries["status"],
        error: function () {
          console.log("error");
        },
        success: function (data) {

          if (data != "Unable to change the state of reservation.") {
            $('.modal-body').html("<p>Successfully updated Status.</p>");
            $('#response-modal').modal('show');
            $('.order-table').html(data);
            update_notification()
          }
        },
        type: 'GET'
      });
})
