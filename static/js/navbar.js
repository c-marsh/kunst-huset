$( document ).ready(function() {
    
    // Function to change the nav-bar on scroll
    $(window).scroll(function(){
        ($(window).scrollTop() >= 100) ? (
            $('.fixed-nav-bar').addClass('scrolled'),
            $('.the-bass').addClass('scrolled')
        ) : (
            $('.fixed-nav-bar').removeClass('scrolled'),
            $('.the-bass').removeClass('scrolled')
        );
    });
    
    // Drop Down Function
    $('#menuButton').on('change', function(){
        ($('#menuButton').is(':checked')) ? (
            $('.the-bass').addClass('dropped')
        ) : (
            $('.the-bass').removeClass('dropped')
        );
    });
    
});



const app = (() => {
  let body;
  let menu;
  let menuItems;

  const init = () => {
    body = document.querySelector('body');
    menu = document.querySelector('#menuButton2');
    menuItems = document.querySelectorAll('.sub-nav__list-item');

    applyListeners();
  };

  const applyListeners = () => {
    menu.addEventListener('click', () => toggleClass(body, 'sub-nav-active'));
  };

  const toggleClass = (element, stringClass) => {
    if (element.classList.contains(stringClass))
    element.classList.remove(stringClass);else

    element.classList.add(stringClass);
  };

  init();
})();