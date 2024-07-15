(() => {
  'use strict'

  const forms = document.querySelectorAll('.needs-validation');

  Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
          if (!form.checkValidity()) {
              event.preventDefault();
              event.stopPropagation();
          }

          form.classList.add('was-validated');
      }, false);

      // Validación personalizada para el campo "Nombre"
      const nameField = form.querySelector('#inputname');
      nameField.addEventListener('input', () => {
          const namePattern = /^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$/;
          if (!namePattern.test(nameField.value)) {
              nameField.setCustomValidity('Invalid');
          } else {
              nameField.setCustomValidity('');
          }
      });

      // Validación personalizada para el campo "Email"
      const emailField = form.querySelector('#email');
      emailField.addEventListener('input', () => {
          // Validación básica de formato de correo
          const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          if (!emailPattern.test(emailField.value)) {
              emailField.setCustomValidity('Invalid');
          } else {
              emailField.setCustomValidity('');
          }
      });

      // Validación personalizada para el campo "Asunto"
      const subjectField = form.querySelector('#subject');
      subjectField.addEventListener('input', () => {
          const subjectPattern = /\S/; // Verifica que el campo no esté vacío o solo tenga espacios
          if (!subjectPattern.test(subjectField.value)) {
              subjectField.setCustomValidity('Invalid');
          } else {
              subjectField.setCustomValidity('');
          }
      });

      // Validación personalizada para el campo "Mensaje"
      const messageField = form.querySelector('#message');
      messageField.addEventListener('input', () => {
          const messagePattern = /\S/; // Verifica que el campo no esté vacío o solo tenga espacios
          if (!messagePattern.test(messageField.value)) {
              messageField.setCustomValidity('Invalid');
          } else {
              messageField.setCustomValidity('');
          }
      });
  });
})();



 // Validaciones personalizadas
 function validateForm(form) {
  let valid = true;

  // Validar "Nombre de Usuario" (solo letras)
  const usernameField = form.querySelector('input[type="text"][placeholder="Nombre de Usuario"]') || form.querySelector('input[type="text"][placeholder="Username"]');
  const usernameError = form.querySelector('#signin-username-error') || form.querySelector('#signup-username-error');
  if (usernameField) {
      const usernamePattern = /^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$/;
      if (!usernamePattern.test(usernameField.value.trim())) {
          usernameError.textContent = "Solo se permiten letras para el nombre de usuario.";
          valid = false;
      } else {
          usernameError.textContent = "";
      }
  }

  // Validar "Email" (formato estándar de correo)
  const emailField = form.querySelector('input[type="text"][placeholder="Email"]');
  const emailError = form.querySelector('#signup-email-error');
  if (emailField) {
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailPattern.test(emailField.value.trim())) {
          emailError.textContent = "Por favor ingrese un correo válido.";
          valid = false;
      } else {
          emailError.textContent = "";
      }
  }

  // Validar "Contraseña" (mínimo 8 caracteres y al menos un número)
  const passwordField = form.querySelector('input[type="password"]');
  const passwordError = form.querySelector('#signin-password-error') || form.querySelector('#signup-password-error');
  if (passwordField) {
      const passwordPattern = /^(?=.*\d).{8,}$/;
      if (!passwordPattern.test(passwordField.value)) {
          passwordError.textContent = "La contraseña debe tener al menos 8 caracteres y contener al menos un número.";
          valid = false;
      } else {
          passwordError.textContent = "";
      }
  }

  return valid;
}

// Listener para el formulario de "Iniciar Sesión"
const signInForm = document.querySelector('.sign-in-form');
if (signInForm) {
  signInForm.addEventListener('submit', event => {
      event.preventDefault();
      if (validateForm(signInForm)) {
          // Aquí se puede manejar el envío del formulario (AJAX, redirección, etc.)
          alert('Formulario de Iniciar Sesión enviado correctamente.');
      } else {
          alert('Por favor corrija los errores en el formulario de Iniciar Sesión.');
      }
  });
}

// Listener para el formulario de "Registrarse"
const signUpForm = document.querySelector('.sign-up-form');
if (signUpForm) {
  signUpForm.addEventListener('submit', event => {
      event.preventDefault();
      if (validateForm(signUpForm)) {
          // Aquí se puede manejar el envío del formulario (AJAX, redirección, etc.)
          alert('Formulario de Registrarse enviado correctamente.');
      } else {
          alert('Por favor corrija los errores en el formulario de Registrarse.');
      }
  });
}