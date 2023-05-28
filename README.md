# Mail Genius - Your Mail Generator

Welcome to MailGenius!


Streamline your business email creation process with MailGenius. Answer a series of questions about your business, target audience, and your unique expertise, and let us generate personalized and professional emails for you.

Say goodbye to the hassle of composing emails from scratch. Our intelligent platform leverages your inputs to create customized email that align with your business objectives and resonate with your target audience.

Our system will send the emails to your designated email address when the composing is complete.
Streamline your email workflow, save valuable time, and make a lasting impression with MailGenius - your go-to solution for professional business email generation.



## How To Install

1. clone the repo:
```
git clone https://github.com/EASS-HIT-PART-A-2022-CLASS-III/MailsGenerator
```

2. Build the project with Docker-compose:

```
docker-compose up
```

 after that you can enter into the frontend site with the "http://localhost:8501/" path in broswer


## Project Tree
```
├── common
│   ├── models.py
├── front
│   ├── app.py
│   ├── Dockerfile
│   ├── README.md
│   ├── requirements.txt
├── mails-generator-server
│   ├── app
│   │   ├── mailsGenerator.py
│   │   ├── main.py
│   │   ├── prompts.py
│   │   ├── unit_test.py
│   ├── Dockerfile
│   ├── README.md
│   ├── requirements.txt
├── mails-sender-server
│   ├── app
│   │   ├── mailSender.py
│   │   ├── main.py
│   ├── Dockerfile
│   ├── README.md
│   ├── requirements.txt
├── main-server
│   ├── app
│   │   ├── main.py
│   ├── Dockerfile
│   ├── README.md
│   ├── requirements.txt
├── .gitignore
├── docker-compose.yml
├── README.md
```
