$(function(){
  $('.search-field').autocomplete({
    source: function(request, response){
            $.get("/search/api/find/product", {
                term:request.term
                }, function(data){
                response($.map(data, function(item) {
                    return {
                        label: item.data,
                        value: item.value
                    }
                }))
            }, "json");
        },
    minLength: 2,
    cache: false,
    dataType: "json",
    autoFocus: true,
    select: function(event, ui){
      $(".search-field").val(ui.item.value)
    },
  })
});
