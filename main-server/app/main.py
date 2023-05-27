from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import httpx

from models import BusinessInfo, GeneratedMails


app = FastAPI()


@app.get("/")
async def root():
    print("main service get root", flush=True)
    return {"message": "Main Server Hello World"}


# called from frontend with all the needed data, and send all the data to the mails-generator-server
# to generate all the needed mails
@app.post("/getmails")
async def getmails(businessInfo: BusinessInfo):
    print("main - getmails called", flush=True)

    url = "http://mails-generator-service:8000/getmails"
    data = businessInfo.dict()
    httpx.post(url, json=data)

    print("main, post http://mails-generator-service:8000/getmails", flush=True)

    return True


# called from mails-generetor-server after it generated all the mails, and move them to the
# mail-sender-server to send it via email
@app.post("/sendmails")
async def sendmails(generatedMails: GeneratedMails):
    print("main - sendmails called", flush=True)

    url = "http://mails-sender-service:8002/sendmails"
    data = generatedMails.dict()
    httpx.post(url, json=data)

    print("main, post http://mails-sender-service:8002/sendmails", flush=True)

    return True
