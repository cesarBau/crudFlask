FROM python:3.10.5-alpine3.15

RUN mkdir -p /app

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 3000

ENV FLASK_APP=main.py
ENV HOST=0.0.0.0
ENV PORT=3000
ENV MONGO_URI='mongodb://localhost:27017/note'

CMD [ "python","main.py"]