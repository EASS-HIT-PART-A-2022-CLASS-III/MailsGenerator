from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import httpx

from mailSender import *

from models import BusinessInfo, GeneratedMails


app = FastAPI()


@app.get("/")
async def root():
    print("sender service get root", flush=True)
    return {"message": "sender Server Hello World"}


@app.get("/dummymail")
async def dummymail():
    sendDummyMail()

    return True


# called from main server to send the generated mail via email
@app.post("/sendmails")
async def sendmails(generatedMails: GeneratedMails):
    print("sender sendmails called", flush=True)
    sendMail(generatedMails)

    return True
