from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from app.mailsGenerator import *

from models import BusinessInfo, singleMail, GeneratedMails


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/getmails")
async def getmails(businessInfo: BusinessInfo):
    generated = await generateAllMails(
        businessInfo.companyName,
        businessInfo.businessAbout,
        businessInfo.clientsDream,
        businessInfo.clientsAvoid,
        businessInfo.clientsProblem,
        businessInfo.influencer,
    )

    mails = GeneratedMails(mails=generated)

    return mails
