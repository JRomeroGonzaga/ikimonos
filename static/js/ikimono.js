const nav = document.querySelector('.menu-navigation')

$(function() {
  $(window).scroll(function() {
    if ($(window).scrollTop() > 150) {
      nav.classList.add('bg-dark')
    } else {
      nav.classList.remove('bg-dark')
    }
  })
}) 