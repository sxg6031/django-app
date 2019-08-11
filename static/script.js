var $heading = $(".heading");
var $headin2 = $(".heading2");

$heading.waypoint(function(){
    $(".heading").css("visibility", "visible");
    $(".heading").addClass("animated fadeInLeft");
}, {offset: "80%"});

$headin2.waypoint(function(){
    $(".heading2").css("visibility", "visible");
    $(".heading2").addClass("animated fadeInLeft");
}, {offset: "80%"});