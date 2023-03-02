<?php
if (isset($_POST['submit'])) {
  $name = $_POST['name'];
  $email = $_POST['email'];
  $subject = $_POST['subject'];
  $message = $_POST['message'];

  $to = 'vitinls387@gmail.com';
  $subject = 'Página de Contato';
  $message = "Nome: " . $name . "\n\nEmail: " . $email . "\n\nAssunto: " . $subject . "\n\nMensagem: " . $message;
  $headers = "De: " . $email;

  if (mail($to, $subject, $message, $headers)) {
    echo 'Sua mensagem foi enviada com sucesso. Obrigado! :)';
  } else {
    echo 'Houve um erro ao enviar a sua solicitação de orçamento. Por favor, tente novamente.';
  }
    header("Location: " . $_SERVER['REQUEST_URI']);
}
?>
