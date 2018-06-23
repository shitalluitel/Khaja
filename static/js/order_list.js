
$('body').on('change','select', function(){
    var id = $(this).attr('id');
    var value = $(this).val();
    $.ajax({
        url: '/carts/api/v1/change/status?id='+ id + "&value="+value+"&next="+window.location.search,
        error: function () {
          console.log("error");
        },
        success: function (data) {

          if (data != "Unable to change the state of reservation.") {
            $('.modal-body').html("<p>Successfully updated Status.</p>");
            $('#response-modal').modal('show');
            $('.order-table').html(data);
          }
        },
        type: 'GET'
      });
})
