<?php
  // Datos del formulario
  $nombre = $_POST['nombre'];
  $apellido = $_POST['apellido'];
  $correo = $_POST['correo'];
  $mensaje = $_POST['mensaje'];

  // Configuración correo electrónico
  $destinatario = 'tanoni44@gmail.com'; // reemplaza con tu correo electrónico
  $asunto = 'Mensaje enviado desde el formulario de contacto';
  $cuerpo = "Nombre: $nombre\nApellido: $apellido\nEmail: $correo\nMensaje: $mensaje";
  $cabeceras = "From: $correo";

  // Enviar correo electrónico
  mail($destinatario, $asunto, $cuerpo, $cabeceras);

  // Confirmación
  $response = array('success' => true);
  echo json_encode($response);
?>