// Datos de usuario (en una aplicación real, esto debería almacenarse en una base de datos)
const registrar = document.querySelector("#frm-reg");
const login = document.querySelector("#frm-log");

let users = [
  {
    username: "lrangel",
    salt: "2q6591",
    hashedPassword: "ZmVuaXhmcmVlMnE2NTkx",
  },
];

// Función para validar el formulario de inicio de sesión
const validateForm = () => {
  const usernameInput = document.getElementById("username");
  const passwordInput = document.getElementById("password");
  const username = usernameInput.value;
  const password = passwordInput.value;

  // Busca el usuario correspondiente al nombre de usuario ingresado
  const user = users.find((user) => user.username === username);
  if (!user) {
    alert("Usuario no encontrado");
    return false;
  }

  // Verifica si la contraseña ingresada es correcta
  const isValidPassword = verifyPassword(
    password,
    user.salt,
    user.hashedPassword
  );
  if (!isValidPassword) {
    alert("Contraseña incorrecta");
    return false;
  }

  // Si el nombre de usuario y la contraseña son válidos, redirige a la página de inicio
  alert("¡Inicio de sesión exitoso!");
  return true;
};

// Función para registrar un nuevo usuario
const registerUser = () => {
  const newUsernameInput = document.getElementById("newUsername");
  const newPasswordInput = document.getElementById("newPassword");
  const newUsername = newUsernameInput.value;
  const newPassword = newPasswordInput.value;

  // Verifica si el nombre de usuario ya está en uso
  const userExists = users.some((user) => user.username === newUsername);
  if (userExists) {
    alert("El nombre de usuario ya está en uso");
    return false;
  }

  // Genera una nueva sal y cifra la contraseña con la sal
  const newSalt = Math.random().toString(36).substring(2, 8);
  const newHashedPassword = hashPassword(newPassword, newSalt);

  // Agrega el nuevo usuario al arreglo de usuarios
  users.push({
    username: newUsername,
    salt: newSalt,
    hashedPassword: newHashedPassword,
  });

  alert("Registro exitoso");
  return true;
};

// Función para cifrar la contraseña
const hashPassword = (password, salt) => {
  const hash = password + salt;
  const encrypted = btoa(hash);
  return encrypted;
};

// Función para verificar la contraseña
const verifyPassword = (password, salt, hashedPassword) => {
  const hash = password + salt;
  const encrypted = btoa(hash);
  return encrypted === hashedPassword;
};

registrar.addEventListener("submit", (e) => {
  e.preventDefault();

  registerUser();
  console.log(users);
});

login.addEventListener("submit", (e) => {
  e.preventDefault();

  validateForm();
  console.log(users);
});
