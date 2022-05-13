// document.addEventListener("DOMContentLoaded", () => {
//   var sum = 0;
//   var subtotal = document.getElementById('my_subtotal');
//   var price_list = document.getElementsByClassName('my_price');
//   var total = document.getElementById('my_total');
//   var quantity_list = document.getElementsByClassName('my_quantity');
//   for (var i = 0, j = price_list.length; i<j; i++){
//     var price = parseInt(price_list[i].getElementsByTagName('span')[0].innerHTML);
//     var quantity = parseInt(quantity_list[i].getElementsByTagName('input').value);
//     sum += price * price * quantity;

//   }
//   subtotal.innerHTML = sum;
//   });
// document.addEventListener("DOMContebtLoaded", () => {
//   var minus = document.getElementById("minus-btn");
//   minus.onclick((e) =>{
//     e.preventDefault();
//     var $this = $(this);
//     var $input = $this.closest('div').find('input');
//     var value = parseInt($input.val());
//     console.log(value);
//   })
// })
// $('.minus-btn').on('click', function(e) {
//   e.preventDefault();
//   var $this = $(this);
//   var $input = $this.closest('div').find('input');
//   var value = parseInt($input.val());

//   if (value &amp;amp;gt; 1) {
//       value = value - 1;
//   } 
//   else {
//       value = 0;
//   }

// $input.val(value);

// });

// $('.plus-btn').on('click', function(e) {
//   e.preventDefault();
//   var $this = $(this);
//   var $input = $this.closest('div').find('input');
//   var value = parseInt($input.val());

//   if (value &amp;amp;lt; 100) {
//       value = value + 1;
//   } else {
//       value =100;
//   }

//   $input.val(value);
// });