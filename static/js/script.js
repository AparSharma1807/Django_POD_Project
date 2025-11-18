// Simple animation on page load
document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    form.style.opacity = 0;

    setTimeout(() => {
        form.style.transition = "0.6s";
        form.style.opacity = 1;
    }, 100);

    console.log("Form ready!");
});

// Optional: alert when image is selected
const fileInput = document.querySelector("input[type='file']");
if (fileInput) {
    fileInput.addEventListener("change", () => {
        if (fileInput.files.length > 0) {
            alert("Image selected: " + fileInput.files[0].name);
        }
    });
}
