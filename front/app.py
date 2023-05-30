import streamlit as st
import requests
import re
import httpx
from pydantic import BaseModel
from typing import List

from models import BusinessInfo


def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, email):
        return True
    else:
        return False


st.title("MailGenius: Your Business Mail Generator")
st.markdown(
    """
        <div style="background-color:#f0f0f0; padding: 20px; border-radius: 10px;">
            <h2>Welcome to MailGenius</h2>
            <p>
            Streamline your business email creation process with MailGenius. Answer a series of questions about your business, target audience, and your unique expertise, and let us generate personalized and professional emails for you.
            </p>
            <p>
            Say goodbye to the hassle of composing emails from scratch. Our intelligent platform leverages your inputs to create customized email that align with your business objectives and resonate with your target audience.
            </p>
            <p>
            Our system will send the emails to your designated email address when the composing is complete.
            </p>
            <p>
            Streamline your email workflow, save valuable time, and make a lasting impression with MailGenius - your go-to solution for professional business email generation.
            </p>
        </div>
        """,
    unsafe_allow_html=True,
)

st.text("")
st.text("")
st.text("")

email_address = st.text_input(
    label="Your Email address", placeholder="example@mail.com"
)

second_email_address = st.text_input(
    label="please enter your Email address again", placeholder="example@mail.com"
)

business_name = st.text_input(
    label="Business Name",
)

business_about = st.text_input(
    label="What is the business about?", placeholder="e.g. dog training"
)

clients_dream = st.text_input(
    label="What is the dream of your clients?",
    placeholder="e.g. to address their dog's behavioral issues",
)

clients_avoid = st.text_input(
    label="What are your clients regularly avoiding?",
    placeholder="e.g. to say no to their dog",
)

clients_problem = st.text_input(
    label="What is the biggest problem of your clients?",
    placeholder="e.g. their dog bites people he doesn't know",
)


buttonClicked = st.button(
    label="Submit",
    type="primary",
    # on_click=generate_mails,
    # args=(email_address, business_name),
)


if buttonClicked == 1:
    # check if all fields are ok
    if "httpx_sent" not in st.session_state:
        if is_valid_email(email_address) == False:
            st.error("Please Enter a valid email")
        elif second_email_address != email_address:
            st.error("The email addresses do not match")
        else:
            if (
                business_name == ""
                or business_about == ""
                or clients_dream == ""
                or clients_avoid == ""
                or clients_problem == ""
            ):
                st.error("Please answer all questions")

            else:
                businessInfo = BusinessInfo(
                    email=email_address,
                    companyName=business_name,
                    businessAbout=business_about,
                    clientsDream=clients_dream,
                    clientsAvoid=clients_avoid,
                    clientsProblem=clients_problem,
                )
                url = "http://main-service:8001/getmails"
                data = businessInfo.dict()
                response = httpx.post(url, json=data)

                st.session_state["httpx_sent"] = True
                st.success(
                    "Form subbmited successfully! we will send you the info in the given email!"
                )
                # st.write(response)
    else:
        st.success("Form already submitted!")
