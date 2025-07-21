FROM python:latest

WORKDIR /app

COPY . .

RUN pip install  -r requirements.txt


ENV PORT=8081

EXPOSE 8081

CMD [ "python", "app.py"]