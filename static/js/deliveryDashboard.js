function get_new_order_data(){
  setInterval(function(){
    jQuery.ajax({
      url: '/delivery/new/order/',
      cache: false,
      error: function () {
        console.log("error");
      },
      success: function (data) {
        $('.new-order-table').html(data);
      },
      type: 'GET'
    });
  },1000 * 30 );
}

async function asyncCallNewOrder() {
  var result = await get_new_order_data();
  jQuery.ajax({
    url: '/delivery/new/order/',
    cache: false,
    error: function () {
      console.log("error");
    },
    success: function (data) {
      $('.new-order-table').html(data);
    },
    type: 'GET'
  });
}

asyncCallNewOrder();



function get_order_prepared_data(){
  setInterval(function(){
    jQuery.ajax({
      url: '/delivery/prepared/order/',
      cache: false,
      error: function () {
        console.log("error");
      },
      success: function (data) {
        $('.prepared-order-table').html(data);
      },
      type: 'GET'
    });
  },1000 * 30 );
}

async function asyncCallOrderPrepared() {
  var result = await get_order_prepared_data();
  jQuery.ajax({
    url: '/delivery/prepared/order/',
    cache: false,
    error: function () {
      console.log("error");
    },
    success: function (data) {
      $('.prepared-order-table').html(data);
    },
    type: 'GET'
  });
}

asyncCallOrderPrepared();


$('body').on('click','.display-cart',function(){
  // var id =$(this).closest('tr').attr("id");
  var id =$(this).attr("id");
  // alert($(this).closest('tr').attr("id"));
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
