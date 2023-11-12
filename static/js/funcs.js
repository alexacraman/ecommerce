
function parallax(){
    var parallaxOne = document.getElementById('parallax-1');
    parallaxOne.style.top = (window.pageYOffset / 6) + 'px';
}
document.addEventListener('scroll', parallax, false)

function parallax2(){
    var parallaxTwo = document.getElementById('parallax-2');
    parallaxTwo.style.top = (window.pageYOffset / 2) + 'px';
}
document.addEventListener('scroll', parallax2, false)