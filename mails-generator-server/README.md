# Mails Generator - first backend service

Mails Generator is a service that creates personalized emails for your business. 

This server side is responsible for receiving the information about the business, 
building smart prompts and generating emails from the information with the help of AI.

## Installation Instructions:

Clone this repository and navigate to the project directory.

Build the Docker image:
`docker build -t generator_server .`

Run the Docker container:

`docker run -it -p 8000:8000 generator_server`
