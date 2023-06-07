//Función que me aplica el estilo a la opciòn seleccionada
function seleccionar(link) {
    var opciones = document.querySelectorAll("#links  a");
    opciones[0].className = "";
    opciones[1].className = "";
    opciones[2].className = "";
    opciones[3].className = "";
    link.className = "seleccionado";
  }
  // Menu responsive
  const navIcon = document.getElementById("nav-icon");
  const navbar = document.getElementById("navbar");
  const links = document.querySelectorAll("#links li a");
  
  navIcon.addEventListener("click", function () {
    navbar.classList.toggle("active");
  });
  links.forEach(function (link) {
    link.addEventListener("click", function () {
      navbar.classList.remove("active");
    });
  });