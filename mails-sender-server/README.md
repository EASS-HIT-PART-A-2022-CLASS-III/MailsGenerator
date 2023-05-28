# Mails Sender - second backend service

Mails Generator is a service that creates personalized emails for your business. 

This server side is responsible for receiving the generated mails and sending them to the business owner.

## Installation Instructions:

Clone this repository and navigate to the project directory.

Build the Docker image:
`docker build -t sender_server .`

Run the Docker container:

`docker run -it -p 8002:8002 sender_server`
