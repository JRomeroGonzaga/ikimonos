// Ikono de cargar 
// while ($(window).load) {
//   $(window).load(function() {
//     $(".loader").fadeOut("slow");
//   })
// }



// Cambiar el color de la barra de navegación
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

// Buscador en la barra de navegacion
const search_box = document.querySelector('#search-box')
const btn_search = document.querySelector('#btn-search')

const series = [

]



const filtrar = () => {
  
}

btn_search.addEventListener('click', filtrar)

