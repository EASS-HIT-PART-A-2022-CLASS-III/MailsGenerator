FROM python:3.8

WORKDIR /backend-sender

COPY ./mails-sender-server .
COPY common .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0","--port", "8002"]