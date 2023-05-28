# Mails Generator - main backend service

Mails Generator is a service that creates personalized emails for your business. 

This server side is the main backend service that manages the network between all other containers.

## Installation Instructions:

Clone this repository and navigate to the project directory.

Build the Docker image:
`docker build -t main_server .`

Run the Docker container:

`docker run -it -p 8001:8001 main_server`
