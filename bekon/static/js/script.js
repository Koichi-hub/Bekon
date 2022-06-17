$(document).ready(function() {
    $(".menu-btn").on("click", function() {
        $(this).toggleClass("menu-btn_pressed");
        $(".side-menu").toggleClass("side-menu_active");
    });
});
