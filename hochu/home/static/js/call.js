(function () {
    const openingBtn = document.querySelectorAll('.form__active');
    const closingBtn = document.querySelector('.cross__link__second');
    const sidebar = document.querySelector('.specialist__form__container');

    for (let btn of openingBtn) {
        btn.addEventListener("click", () => sidebar.classList.add('specialist__form__container--active'));
    }

    closingBtn.addEventListener("click", function () {
        sidebar.classList.remove('specialist__form__container--active');
    });
}())