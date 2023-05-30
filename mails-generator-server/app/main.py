from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import httpx
import asyncio


from mailsGenerator import *

from models import BusinessInfo, GeneratedMails


app = FastAPI()


@app.get("/")
async def root():
    print("generator service get root", flush=True)
    return {"message": "Hello World"}


async def generateMailsAndSend(businessInfo: BusinessInfo):
    print("generator , generateMailsAndSend", flush=True)

    generated = await generateAllMails(
        businessInfo.companyName,
        businessInfo.businessAbout,
        businessInfo.clientsDream,
        businessInfo.clientsAvoid,
        businessInfo.clientsProblem,
    )

    mails = GeneratedMails(emailAddress=businessInfo.email, mails=generated)

    url = "http://main-service:8001/sendmails"
    data = mails.dict()
    httpx.post(url, json=data)

    print("generator end generating, post main-service:8001/sendmails", flush=True)


@app.post("/getmails")
async def getmails(businessInfo: BusinessInfo):
    print("generator getmails called", flush=True)

    asyncio.create_task(generateMailsAndSend(businessInfo))

    return True
