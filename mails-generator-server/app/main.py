from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from mailsGenerator import *


class BusinessInfo(BaseModel):
    companyName: str
    businessAbout: str
    clientsDream: str
    clientsAvoid: str
    clientsProblem: str
    influencer: str


class GeneratedMails(BaseModel):
    mails: List[str]


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/getmails")
async def getmails(businessInfo: BusinessInfo):
    generated = await generateAllMails(
        businessInfo.companyName, businessInfo.businessAbout, businessInfo.clientsDream,
        businessInfo.clientsAvoid, businessInfo.clientsProblem, businessInfo.influencer)

    mails = GeneratedMails(mails=generated)

    return (mails)
