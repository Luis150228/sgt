const users = []; // Aquí almacenaremos los usuarios registrados

// Función para registrar un usuario
function registerUser(username, password) {
  const salt = Math.random().toString(36).substring(2, 15);
  const hashedPassword = hashPassword(password, salt);
  const user = { username: username, password: hashedPassword, salt: salt };
  users.push(user);
}

// Función para autenticar a un usuario
function authenticateUser(username, password) {
  const user = users.find((user) => user.username === username);
  if (user == null) {
    return false;
  }
  const hashedPassword = hashPassword(password, user.salt);
  return hashedPassword === user.password;
}

// Función para cifrar una contraseña con una sal
function hashPassword(password, salt) {
  const hash = crypto.createHash("sha256");
  hash.update(password + salt);
  return hash.digest("hex");
}

// Event listener para el formulario de registro
const registerForm = document.getElementById("register-form");
registerForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const username = registerForm.elements["username"].value;
  const password = registerForm.elements["password"].value;
  registerUser(username, password);
  registerForm.reset();
});

// Event listener para el formulario de inicio de sesión
const loginForm = document.getElementById("login-form");
loginForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const username = loginForm.elements["username"].value;
  const password = loginForm.elements["password"].value;
  if (authenticateUser(username, password)) {
    alert("Login successful!");
    loginForm.reset();
  } else {
    alert("Incorrect username or password");
  }
});
