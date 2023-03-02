<?php
if (isset($_POST['submit'])) {
  $name = $_POST['name'];
  $email = $_POST['email'];
  $phone = $_POST['phone'];
  $message = $_POST['message'];

  $to = 'vitinls387@gmail.com';
  $subject = 'Orçamento de serviço pelo site';
  $message = "Nome: " . $name . "\n\nEmail: " . $email . "\n\nTelefone: " . $phone . "\n\nMensagem: " . $message;
  $headers = "De: " . $email;

  if (mail($to, $subject, $message, $headers)) {
    echo 'Sua solicitação de orçamento foi enviada com sucesso. Obrigado! :)';
  } else {
    echo 'Houve um erro ao enviar a sua solicitação de orçamento. Por favor, tente novamente.';
  }
    header("Location: " . $_SERVER['REQUEST_URI']);
}
?>
