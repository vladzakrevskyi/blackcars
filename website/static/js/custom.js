if ($(window).width() < 576) {
    $("#myCarousel, #carousel-example-generic").swipe({

        swipe: function(event, direction, distance, duration, fingerCount, fingerData) {

            if (direction === 'left') $(this).find('.right.carousel-control').click();
            if (direction === 'right') $(this).find('.left.carousel-control').click();

        },
        allowPageScroll:"vertical"

    });
}


$('#agree').on('change', function () {
    if ($(this).is(':checked')) $('.contact_button').attr('disabled', false);
    else $('.contact_button').attr('disabled', true);
});
$(document).ready(function() {
    $("#lightMainSlider").lightSlider({
        item: 1,
        autoWidth: false,
        slideMove: 1,
        slideMargin: 5,
    });
    $("#lightSlider").lightSlider({
        item: 1,
        autoWidth: false,
        slideMove: 1,
        slideMargin: 5,
    });
});
// if ($('#date_start')[0]) {
//     if ( $('#date_start')[0].type != 'date' ) {
//         $('#date_start').datetimepicker();
//     }
// }

// thumbnails.carousel.js jQuery plugin
(function (window, $, undefined) {

    var conf = {
        center: true,
        backgroundControl: false
    };

    var cache = {
        $carouselContainer: $('.thumbnails-carousel').parent(),
        $thumbnailsLi: $('.thumbnails-carousel li'),
        $controls: $('.thumbnails-carousel').parent().find('.carousel-control')
    };

    function init() {
        cache.$carouselContainer.find('ol.carousel-indicators').addClass('indicators-fix');
        cache.$thumbnailsLi.first().addClass('active-thumbnail');

        if (!conf.backgroundControl) {
            cache.$carouselContainer.find('.carousel-control').addClass('controls-background-reset');
        } else {
            cache.$controls.height(cache.$carouselContainer.find('.carousel-inner').height());
        }


    }

    function refreshOpacities(domEl) {

        let prev_index = cache.$thumbnailsLi.parent().find('.active-thumbnail').index();
        let next_index = $(domEl).index();
        let elWidth = cache.$thumbnailsLi.width();
        let leftPos = $('#carousel-example-generic .thumbnails-carousel').scrollLeft();

        if (next_index > prev_index) {
            $("#carousel-example-generic .thumbnails-carousel").animate({
                scrollLeft: leftPos + elWidth
            }, 800);
        } else if (next_index < prev_index) {
            $("#carousel-example-generic .thumbnails-carousel").animate({
                scrollLeft: leftPos - elWidth
            }, 800);
        }

        cache.$thumbnailsLi.removeClass('active-thumbnail');
        cache.$thumbnailsLi.eq($(domEl).index()).addClass('active-thumbnail');
    }

    function bindUiActions() {
        cache.$carouselContainer.on('slide.bs.carousel', function (e) {
            refreshOpacities(e.relatedTarget);
        });

        cache.$thumbnailsLi.click(function () {
            cache.$carouselContainer.carousel($(this).index());
        });
    }

    $.fn.thumbnailsCarousel = function (options) {
        conf = $.extend(conf, options);

        init();
        bindUiActions();

        return this;
    }

})(window, jQuery);

$('.thumbnails-carousel').thumbnailsCarousel();



function func1(){
    document.getElementById('open_men').style.display="none";
    document.getElementById('close_men').style.display="block";
    $('.navbar-collapse').slideDown();
}
function func(){
    document.getElementById('open_men').style.display="block";
    document.getElementById('close_men').style.display="none";
    $('.navbar-collapse').slideUp().removeClass('in');
}


$("#card_number").mask("9999-9999-9999-9999");


function isNumberKey(evt){
    var charCode = (evt.which) ? evt.which : event.keyCode
    if (charCode > 31 && (charCode < 48 || charCode > 57))
        return false;
    return true;
}

function noDigits(event) {
    if ("1234567890./,@''|@#$%^&*()_+=-".indexOf(event.key) != -1)
        event.preventDefault();
}


const slider = document.querySelector('.thumbnails-carousel');
let isDown = false;
let startX;
let scrollLeft;
if(slider) {
    slider.addEventListener('mousedown', (e) => {
        isDown = true;
        slider.classList.add('active');
        startX = e.pageX - slider.offsetLeft;
        scrollLeft = slider.scrollLeft;
    });

    slider.addEventListener('mouseleave', () => {
        isDown = false;
        slider.classList.remove('active');
    });
    slider.addEventListener('mouseup', () => {
        isDown = false;
        slider.classList.remove('active');
    });
    slider.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - slider.offsetLeft;
        const walk = (x - startX) * 3; //scroll-fast
        slider.scrollLeft = scrollLeft - walk;
    });
}


$(document).ready(function () {
    $('.thumbnails-carousel').mousewheel(function(e, delta) {
        this.scrollLeft -= (delta * 10);
        this.scrollRight -= (delta * 10);
        e.preventDefault();
    });

});


const mediaQuery = window.matchMedia('(min-width: 768px)')
const mediaQuery_for_fixed_button = window.matchMedia('(max-width: 500px)')

if (mediaQuery.matches) {
    // Then trigger an alert
    $('.menus').addClass("dropdown");
}
else {
    $('.menus').removeClass("dropdown");
}

$('#menu-open').click(function() {
    $('.menus').toggleClass("clos open");

    $(this).toggleClass("no_rotate rotate_180")
});

/* Bootstrap Cookie Alert */
(function () {
    "use strict";

    let cookieAlert = document.querySelector(".cookiealert");
    let acceptCookies = document.querySelector(".acceptcookies");

    if (!cookieAlert) {
       return;
    }

    cookieAlert.offsetHeight; // Force browser to trigger reflow (https://stackoverflow.com/a/39451131)

    // Show the alert if we cant find the "acceptCookies" cookie
    if (!getCookie("acceptCookies")) {
        cookieAlert.classList.add("show");
    }

    // When clicking on the agree button, create a 1 year
    // cookie to remember user's choice and close the banner
    acceptCookies.addEventListener("click", function () {
        setCookie("acceptCookies", true, 365);
        cookieAlert.classList.remove("show");

        // dispatch the accept event
        window.dispatchEvent(new Event("cookieAlertAccept"))
    });

    // Cookie functions from w3schools
    function setCookie(cname, cvalue, exdays) {
        var d = new Date();
        d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
        var expires = "expires=" + d.toUTCString();
        document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
    }

    function getCookie(cname) {
        var name = cname + "=";
        var decodedCookie = decodeURIComponent(document.cookie);
        var ca = decodedCookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) === ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(name) === 0) {
                return c.substring(name.length, c.length);
            }
        }
        return "";
    }
})();
