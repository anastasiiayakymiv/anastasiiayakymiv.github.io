const nav = document.querySelector('.header-top');
function fixNavbar() {
  if (window.scrollY > nav.offsetTop) {
    nav.classList.add('fixed');
  } else {
    nav.classList.remove('fixed');
  }
}
window.addEventListener('scroll', fixNavbar);