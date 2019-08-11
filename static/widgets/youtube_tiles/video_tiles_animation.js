var $trigger3 = $(".trigger3");

$trigger3.waypoint(function(){
    $(".video-card").css("visibility", "visible");
    $(".heading3").css("visibility", "visible")
    $(".heading3").addClass("animated fadeInUp");
    $(".video-card").addClass("animated fadeInUp");
}, {
    offset: "50%"
});