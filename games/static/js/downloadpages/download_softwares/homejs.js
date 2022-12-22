//Get the button:
mybutton = document.getElementById("navBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}
// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

function sticky_relocate() {
  var window_top = $(window).scrollTop() ;
  var footer_top = $(".footer").offset().top - 30;
  var div_top = $('#sticky-anchor').offset().top;
  var div_height = $(".sidebar").height();
  var leftHeight = $('.left-container').height(); 

  if (window_top + div_height > footer_top){
      $('.sidebar').removeClass('stick');
      $('.sidebar').removeClass('abs');
      $('.right-conatainer').css('min-height', leftHeight + 'px');
    }
  else if (window_top > div_top) {
      $('.sidebar').addClass('stick');
      $('.sidebar').removeClass('abs');
  } else {
      $('.sidebar').addClass('stick');
      $('.sidebar').removeClass('abs');
  }
}

$(function () {
  $(window).scroll(sticky_relocate);
  sticky_relocate();
});

/* When the user scrolls down, hide the navbar. When the user scrolls up, show the navbar */
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-5px";
  }
  prevScrollpos = currentScrollPos;
}



