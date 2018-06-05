
$('body').on('change','select', function(){
    var id = $(this).attr('id');
    var value = $(this).val();
    $.ajax({
        url: '/carts/api/v1/change/status?id='+ id + "&value="+value,
        error: function () {
          console.log("error");
        },
        success: function (data) {
          console.log(data);
          $('.modal-body').html(data);
          $('#response-modal').modal('show');
        },
        type: 'GET'
      });
})
