var $trigger1 = $(".trigger1");

$trigger1.waypoint(function () {
    var temp = 100;
    $(".tile").each(function () {
        $(this).css("animation-delay", temp + "ms");
        temp = temp + 100;
    });
    $(".tile").css("visibility", "visible");
    $(".tile").addClass("animated fadeInRightBig");
}, {
    offset: "30%"
});
