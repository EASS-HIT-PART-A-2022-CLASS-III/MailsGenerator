from email.message import EmailMessage
import ssl
import smtplib

email_sender = "advanceadam4@gmail.com"
password = "drsxattlvnurgumo"
email_receiver = "advanceadam1@gmail.com"

subject = "MailGenius: Your Business Mail Generator"


def sendMail(a):
    a = 1


body = """
check this video out:
https://www.youtube.com/watch?v=g_j6ILT-X0k&t=1s&ab_channel=ThePyCoach
"""
email = EmailMessage()
email["From"] = email_sender
email["To"] = email_receiver
email["Subject"] = subject
email.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, password)
    smtp.sendmail(email_sender, email_receiver, email.as_string())
