$(function() {
    $('.carousel').carousel({
            interval: 550 * 10
    });
    $('[data-toggle="tooltip"]').tooltip();
});

window.onscroll = () => {scrollNavbar()};

scrollNavbar = () => {
// Target elements
    const navBar = document.getElementById("navbar");

    if (document.documentElement.scrollTop > 100) {
        navBar.classList.add('background-white');
    } else {
        navBar.classList.remove('background-white');
    }
}