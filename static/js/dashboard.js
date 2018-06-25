//chart
var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: [],
    datasets: [{
        label: '',
        data: [],
        backgroundColor: [
            'rgb(0, 186, 156)',
          ],
          borderColor: [
              'rgb(0, 186, 156)',
          ],
    }]
  },
  options: {
    scales: {
        xAxes: [{
          ticks: {
            fontSize: 10,
          }
        }],
        yAxes: [{
            ticks: {
                beginAtZero:true,
                fontSize: 10,
            }
        }]
    }
  }
});


function get_day_total_data(){
    $.ajax({
      url: '/company/get-day-total',
      cache: false,
      error: function () {
        console.log("error");
      },
      success: function (data) {
        $('.day-total').html(data);
        // console.log(data);
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
        // console.log(data);
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
        // console.log(data);
      },
      type: 'GET'
    });
}

async function year_total() {
  var result = await get_year_total_data();
}

year_total();


function get_total_product_data(){
    $.ajax({
      url: '/company/count-product',
      cache: false,
      error: function () {
        console.log("error");
      },
      success: function (data) {
        $('.total-products').html(data);
      },
      type: 'GET'
    });
}

async function total_product() {
  var result = await get_total_product_data();
}

total_product();


function view_daily_chart(){

  $.ajax({
    url: '/company/get-day-data',
    cache: false,
    error: function () {
      console.log("error");
    },
    success: function (data) {
      myChart.data.labels = data.labels;
      myChart.data.datasets[0].data = data.data
      myChart.data.datasets[0].label = data.label
      myChart.update();
    },
    type: 'GET'
  });
}

async function get_chart(){
  var result = await view_daily_chart();
}

get_chart();
