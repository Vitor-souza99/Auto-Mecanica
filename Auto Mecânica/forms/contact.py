from django.shortcuts import redirect
import smtplib

if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']

    to = 'vitinls387@gmail.com'
    subject = 'Orçamento de serviço pelo site'
    body = f"Nome: {name}\n\nEmail: {email}\n\nTelefone: {phone}\n\nMensagem: {message}"
    headers = f"De: {email}\r\n"

    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login('vitinls387@gmail.com', 'Vls3199jmv')
        smtp_server.sendmail(email, to, body)
        smtp_server.close()
        print('Sua solicitação de orçamento foi enviada com sucesso. Obrigado! :)')
    except Exception as e:
        print(f'Houve um erro ao enviar a sua solicitação de orçamento. Erro: {e}')

    return redirect(request.path_info)
