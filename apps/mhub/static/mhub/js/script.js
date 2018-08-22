$(document).ready(function() {
    $(".search_results").hide();
    $('.loading_pingpong').hide();

    $(".gobutton").click(function(e) {
        e.preventDefault();
        // $('.loading_pingpong').show('slow');
        // $('.loading_pingpong').hide('slow');
        $(".searchbar").css("margin-top","50px");
        $(".search_results").show("slow");
    })


})

