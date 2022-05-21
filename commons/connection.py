
from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)
MONGO_URI=os.environ.get('MONGO_URI')
app.logger.info(MONGO_URI)
mongo_connection = ''
app.logger.info('Try connection to db')

try:
    mongo_connection = MongoClient(MONGO_URI)
    app.logger.info('Connection to db succesfull')
    
except:
    app.logger.info('Error to connection')