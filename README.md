# MailsGenerator

To build the project with Docker-compose use:

```
docker-compose up
```
 after that you can enter into the frontend site with the "http://localhost:8501/" path in broswer

# Project Tree
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
