const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
    container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
    container.classList.remove("sign-up-mode");
});


function togglePasswordVisibility() {
    const passwordInput = document.getElementById("password");
    const eyeIcon = document.querySelector(".input-field i");
  
    if (passwordInput.type === "password") {
      passwordInput.type = "text";
      eyeIcon.classList.remove("fas fa-eye");
      eyeIcon.classList.add("fas fa-eye-slash");
    } else {
      passwordInput.type = "password";
      eyeIcon.classList.remove("fas fa-eye-slash");
      eyeIcon.classList.add("fas fa-eye");
    }
  }

  function goToIndex() {
    // Redirige al usuario al índice (index.html)
    window.location.href = "index.html";
  }