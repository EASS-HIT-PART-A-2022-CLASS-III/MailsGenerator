from pydantic import BaseModel
from typing import List


class BusinessInfo(BaseModel):
    companyName: str
    businessAbout: str
    clientsDream: str
    clientsAvoid: str
    clientsProblem: str
    influencer: str


class singleMail(BaseModel):
    title: str
    mail: str


class GeneratedMails(BaseModel):
    mails: List[str]
