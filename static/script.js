// Redirect function
function redirectPage() {
    window.location.href = "/course/";  
    // If using Django URL pattern like path('course/', views.course, name='course')
}

// Optional: Preloader effect
window.addEventListener("load", function() {
    const preloader = document.querySelector(".preloader");
    if (preloader) {
        preloader.style.display = "none";
    }
});