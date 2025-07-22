FROM python:latest

WORKDIR /app

COPY . .

RUN pip install  -r requirements.txt


ENV PORT=8081

EXPOSE 8081

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8081", "app:app"]
