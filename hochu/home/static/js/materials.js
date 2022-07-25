$(document).ready(function() {
   $('.material').click(function() {
      $('.material').removeClass('material__active');
      $(this).addClass('material__active');
   });
   var filterizd = $('.filtr-container').filterizr();
   filterizd.filterizr();
});