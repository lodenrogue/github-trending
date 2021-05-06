FROM python:3.6-slim

COPY ./requirements.txt /app/requirements.txt

COPY ./trending.py /app/trending.py

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD python trending.py
