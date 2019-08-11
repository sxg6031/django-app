var $trigger2 = $(".trigger2");

$trigger2.waypoint(function(){
    $(".left_tile").css("visibility", "visible");
    $(".right_tile").css("visibility", "visible");
    $(".left_tile").addClass("animated fadeInLeftBig");
    $(".right_tile").addClass("animated fadeInRightBig");
}, {offset: "50%"});