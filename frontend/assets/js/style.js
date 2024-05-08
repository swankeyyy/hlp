
// for the header, adds a class: headernav-scroll
window.addEventListener('scroll', function () {
    document.getElementById('header-nav').classList.toggle('headernav-scroll', window.scrollY > 50);
});