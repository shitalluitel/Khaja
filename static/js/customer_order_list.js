// function callOrderCart(){
//   var id = $(this);
//   console.log(id);
// }


$('body').on('click','.display-cart',function(){
  var id =$(this).attr("id");
  jQuery.ajax({
    url: '/customer/order/'+id+"/cart",
    cache: false,
    error: function () {
      console.log("error");
    },
    success: function (data) {

      $('.modal').modal('show');
      $('.modal-dialog').addClass('modal-lg modal-dialog-centered');
      $('.modal-body').html(data);
      $('.modal-title').hide();
      $('.modal-footer').html('<button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>  <a class="btn btn-danger" href="/">Shop More</a>');
    },
    type: 'GET'
  });
})
