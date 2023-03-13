from django.shortcuts import render, redirect
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        to = 'vitinls387@gmail.com'

        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = to
        msg['Subject'] = subject

        body = f"Nome: {name}\n\nEmail: {email}\n\nMensagem: {message}"
        msg.attach(MIMEText(body, 'plain'))

        try:
            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.login('seuemail@gmail.com', 'suasenha')
            smtp_server.sendmail(email, to, msg.as_string())
            smtp_server.close()
            return render(request, 'form.html', {'success': True})
        except Exception as e:
            print(f'Houve um erro ao enviar o e-mail. Erro: {e}')
            return render(request, 'form.html', {'error': True})

    return render(request, 'form.html')


