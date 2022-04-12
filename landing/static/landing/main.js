$( document ).ready(function() {
    
    // To trigger dropdown in the navbar
    $(".dropdown-trigger").dropdown({
        hover:true,
    });

    // To trigger navbar menu for mobile
    $('.sidenav').sidenav();

});