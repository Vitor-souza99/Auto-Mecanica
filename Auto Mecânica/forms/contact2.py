import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

if "submit" in request.form:
    name = request.form["name"]
    email = request.form["email"]
    subject = request.form["subject"]
    message = request.form["message"]

    to = "vitinls387@gmail.com"
    sender = "vitinls387@gmail.com"
    password = "Vls3199jmv"

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = to
    msg["Subject"] = "Página de Contato"

    body = "Nome: {}\n\nEmail: {}\n\nAssunto: {}\n\nMensagem: {}".format(name, email, subject, message)
    msg.attach(MIMEText(body, "plain"))

    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.starttls()
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, to, msg.as_string())
    smtp_server.quit()

    return "Sua mensagem foi enviada com sucesso. Obrigado! :)"
