/*
Template Name: Veltrix - Admin & Dashboard Template
Author: Themesdesign
Website: https://themesdesign.in/
Contact: themesbrand@gmail.com
File: Table responsive Init Js File
*/

$(function() {
    $(".table-responsive").responsiveTable({
        addDisplayAllBtn: "btn btn-secondary"
    });

    $(".btn-toolbar [data-toggle=dropdown]").attr("data-bs-toggle", "dropdown");
});
