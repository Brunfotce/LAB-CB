#!/usr/bin/env python3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json

data = {}
# {
# "user": "jose.hernandezsal@uanl.edu.mx"
# "pass": "password_super_secreto"
# }
#
#
with open("pass.json") as f:
    data = json.load(f)
# create and setup the parameters of the message
email_msg = MIMEMultipart()
email_msg["From"] = data["user"]
receipents = ["jose.hernandezsal@uanl.edu.mx"]
email_msg["To"] = ", ".join(receipents)
email_msg["Subject"] = "Salu2"

# add in the message body
message = "Enviado desde la clase de los sabados a las 8am siendo las 10:06 pm del 30/04/22."
email_msg.attach(MIMEText(message, "plain"))

# create server
server = smtplib.SMTP("smtp.office365.com:587")
server.starttls()
# Login Credentials for sending the mail
server.login(data["user"], data["pass"])


# send the message via the server.
try:
    server.sendmail(email_msg["From"], receipents, email_msg.as_string())
    server.quit()
    print("successfully sent email to %s:" % (email_msg["To"]))
except:
    print("algo salio mal con el envio de correos")
    server.quit()