$(function () {

    var curSlide = 0;
    var maxSlide = $('.banner-single').length - 1;
    var delay = 3;

    initSlider();
    changeSlide();

    function initSlider() {
        $('.banner-single').hide();
        $('.banner-single').eq(0).show();
    }

    function changeSlide() {
        setInterval(function () {
            $('.banner-single').eq(curSlide).fadeOut(2000);
            curSlide++;
            if (curSlide > maxSlide)
                curSlide = 0;
            $('.banner-single').eq(curSlide).fadeIn(2000);
        }, delay * 1000);
    }

})


$(function () {

    var message = document.querySelector('#body-message');
    message.addEventListener('input', updateMessage);

    function updateMessage() {
        var post = document.querySelector('#body-message');

        var characters = post.value.length;

        var count = document.querySelector('#number-characters');
        count.innerHTML = characters;
    }

})


const MENU_BTN = document.querySelector(".menu-btn");
const NAVIGATION = document.querySelector(".navbar-links");

MENU_BTN.addEventListener("click", () => {
    MENU_BTN.classList.toggle("active");
    NAVIGATION.classList.toggle("active");
});


$(document).ready(function () {
    load_data();
    function load_data(query) {
        $.ajax({
            url: "/company_search",
            method: "POST",
            data: { query: query },
            success: function (data) {
                $('#result').html(data);
                $("#result").append(data.htmlcompanyresponse);
            }
        });
    }
    $('#search_text').keyup(function () {
        var search = $(this).val();
        if (search != '') {
            load_data(search);
        } else {
            load_data();
        }
    });
});


