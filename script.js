
const input = document.getElementById("imageInput");
const preview = document.getElementById("previewImage");
const result = document.getElementById("result");

input.addEventListener("change", () => {
    const file = input.files[0];

    if (file) {
        preview.src = URL.createObjectURL(file);
        preview.style.display = "block";
        result.textContent = "Image uploaded successfully!";
    }
});
