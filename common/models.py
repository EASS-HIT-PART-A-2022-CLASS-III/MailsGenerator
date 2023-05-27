from pydantic import BaseModel
from typing import List


class BusinessInfo(BaseModel):
    email: str
    companyName: str
    businessAbout: str
    clientsDream: str
    clientsAvoid: str
    clientsProblem: str


class GeneratedMails(BaseModel):
    emailAddress: str
    mails: List[str]
