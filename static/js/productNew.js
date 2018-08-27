// to display product image on select
function readIMG(input) {
   if (input.files && input.files[0]) {
       var reader = new FileReader();

       reader.onload = function (e) {
           $('#product-image').attr('src', e.target.result);
       }

       reader.readAsDataURL(input.files[0]);
   }
}

$('body').on('change','#id_image',function(){
 readIMG(this);
});
