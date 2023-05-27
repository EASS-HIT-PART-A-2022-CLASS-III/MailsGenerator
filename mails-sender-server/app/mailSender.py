from email.message import EmailMessage
import ssl
import smtplib
from typing import List

from models import GeneratedMails

email_sender = "advanceadam4@gmail.com"
password = "drsxattlvnurgumo"


def sendMail(generatedMails: GeneratedMails):
    subject = "MailGenius: Your Business Mail Generator"
    body = getMailBody(generatedMails)

    email = EmailMessage()

    email["From"] = email_sender
    email["To"] = generatedMails.emailAddress
    email["Subject"] = subject

    email.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, password)
        smtp.sendmail(email_sender, generatedMails.emailAddress, email.as_string())


def getMailBody(generatedMails: GeneratedMails):
    explanation = "These are the generated mails:\n\n"
    mails_body = explanation + "\n".join(
        f"This is the {i+1} mail: {mail}" for i, mail in enumerate(generatedMails.mails)
    )

    return mails_body


def sendDummyMail():
    subject = "Dummy mail for testing"
    body = " this is a dummy mail body"

    to = "advanceadam1@gmail.com"

    email = EmailMessage()

    email["From"] = email_sender
    email["To"] = to
    email["Subject"] = subject

    email.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, password)
        smtp.sendmail(email_sender, to, email.as_string())
