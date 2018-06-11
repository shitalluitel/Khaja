// $(document).ready(function(){
//   $.ajax({
//     url: '/carts/api/v1/change/status?id='+ id + "&value="+value,
//     error: function () {
//       console.log("error");
//     },
//     success: function (data) {
//       console.log(data);
//       $('.modal-body').html(data);
//       $('#response-modal').modal('show');
//     },
//     type: 'GET'
//   });
// });

function get_day_total_data(){
    $.ajax({
      url: '/company/get-day-total',
      cache: false,
      error: function () {
        console.log("error");
      },
      success: function (data) {
        $('.day-total').html(data);
        console.log(data);
      },
      type: 'GET'
    });
}

async function day_total() {
  var result = await get_day_total_data();
}

day_total();

function get_month_total_data(){
    $.ajax({
      url: '/company/get-month-total',
      cache: false,
      error: function () {
        console.log("error");
      },
      success: function (data) {
        $('.month-total').html(data);
        console.log(data);
      },
      type: 'GET'
    });
}

async function month_total() {
  var result = await get_month_total_data();
}

month_total();

function get_year_total_data(){
    $.ajax({
      url: '/company/get-year-total',
      cache: false,
      error: function () {
        console.log("error");
      },
      success: function (data) {
        $('.year-total').html(data);
        console.log(data);
      },
      type: 'GET'
    });
}

async function year_total() {
  var result = await get_year_total_data();
}

year_total();
