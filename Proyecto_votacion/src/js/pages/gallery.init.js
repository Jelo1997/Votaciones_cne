/*
Template Name: Veltrix - Admin & Dashboard Template
Author: Themesdesign
Website: https://themesdesign.in/
Contact: themesbrand@gmail.com
File: Rating Js File
*/


$('.gallery-popup').magnificPopup({
    type: 'image',
    closeOnContentClick: true,
    mainClass: 'mfp-fade',
    gallery: {
        enabled: true,
        navigateByImgClick: true,
        preload: [0,1] // Will preload 0 - before current, and 1 after the current image
    }
});