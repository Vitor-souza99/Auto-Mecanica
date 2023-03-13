import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

app = Flask(__name__)


if "submit" in request.form:
    name = request.form["name"]
    email = request.form["email"]
    subject = request.form["subject"]
    message = request.form["message"]

    to = "vitinls387@gmail.com"

    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = to
    msg["Subject"] = "Página de Contato"

    body = "Nome: {}\n\nEmail: {}\n\nAssunto: {}\n\nMensagem: {}".format(name, email, subject, message)
    msg.attach(MIMEText(body, "plain"))

    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.starttls()
    smtp_server.login(email, password)
    smtp_server.sendmail(email, to, msg.as_string())
    smtp_server.quit()

    return "Sua mensagem foi enviada com sucesso. Obrigado! :)"

    if __name__ == '__main__':
    app.run(debug=True)

