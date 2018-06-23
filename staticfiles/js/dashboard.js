//chart
var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: [],
    datasets: [{
        label: '',
        data: [],
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'
        ],
        borderColor: [
            'rgba(255,99,132,1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'
        ],
        borderWidth: 1
    }]
  },
  options: {
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero:true
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
