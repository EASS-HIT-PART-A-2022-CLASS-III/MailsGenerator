from email.message import EmailMessage
import ssl
import smtplib
from typing import List

from models import GeneratedMails

emailSender = "advanceadam4@gmail.com"
password = "drsxattlvnurgumo"


def sendMail(generatedMails: GeneratedMails):
    subject = "MailGenius: Your Business Mail Generator"
    body = getMailBody(generatedMails)

    sendGmail(subject, body, generatedMails.emailAddress)


def getMailBody(generatedMails: GeneratedMails):
    explanation = "<h1 style='color: #008080; font-family: Arial, sans-serif; font-size: 24px; font-weight: bold;'>These are the generated mails:</h1>"
    mailsBody = explanation + "<br><br>".join(
        "<h2 style='color: #4C4C4C; font-family: Arial, sans-serif; font-size: 18px; font-weight: bold;'>Mail #{}:</h2>\n<p style='font-family: Arial, sans-serif; font-size: 14px;'>{}</p>".format(
            i + 1, mail.replace("\n", "<br>")
        )
        for i, mail in enumerate(generatedMails.mails)
    )

    html_content = f'<div dir="ltr">{mailsBody}</div>'

    return html_content


def sendDummyMail():
    subject = "Dummy mail for testing"
    body = " <h1> this is a dummy mail body </h1>"

    to = "advanceadam1@gmail.com"

    sendGmail(subject, body, to)


def sendGmail(subject, body, receiverAddress):
    email = EmailMessage()

    email["From"] = emailSender
    email["To"] = receiverAddress
    email["Subject"] = subject

    email.add_alternative(body, subtype="html")

    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(emailSender, password)
        smtp.sendmail(emailSender, receiverAddress, email.as_string())
