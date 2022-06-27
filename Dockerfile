FROM python:3.10.5-alpine3.15

RUN mkdir -p /app

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 3000

ENV FLASK_APP=main.py
ENV HOST=0.0.0.0
ENV PORT=3000
ENV MONGO_URI='mongodb+srv://sootcrack:wEjH1nb4zffJm8F1@cluster0.8rgay.mongodb.net/notes'

CMD [ "python", "main.py"]