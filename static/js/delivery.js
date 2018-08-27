$('body').on('click','.display-cart',function(){
  var id =$(this).closest('tr').attr("id");
  jQuery.ajax({
    url: '/delivery/cart-detail-info/?cart_id=' + id,
    cache: false,
    error: function () {
      console.log("error");
    },
    success: function (data) {

      $('.modal').modal('show');
      $('.modal-dialog').addClass('modal-lg modal-dialog-centered');
      $('.modal-body').html(data);
      $('.modal-title').hide();
      $('.modal-footer').html('<button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>');
    },
    type: 'GET'
  });
})

$('body').on('click','.display-paid-cart',function(){
  var id =$(this).closest('tr').attr("id");
  jQuery.ajax({
    url: '/delivery/paid/cart-detail-info/?cart_id=' + id,
    cache: false,
    error: function () {
      console.log("error");
    },
    success: function (data) {

      $('.modal').modal('show');
      $('.modal-dialog').addClass('modal-lg modal-dialog-centered');
      $('.modal-body').html(data);
      $('.modal-title').hide();
      $('.modal-footer').html('<button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>');
    },
    type: 'GET'
  });
})
