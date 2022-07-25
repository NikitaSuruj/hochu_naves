(function() {
    const openingBtn = document.querySelector('.burger__link');
    const closingBtn = document.querySelector('.cross__link');
    const sidebar = document.querySelector('.menu');
    
    openingBtn.addEventListener("click", function() {
        sidebar.classList.add('menu--active');
    });
    
    closingBtn.addEventListener("click", function() {
        sidebar.classList.remove('menu--active');
    });
    }())
