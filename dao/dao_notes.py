import os
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

app.logger.info('Try to connect to the database')
try:
    app.logger.info('Connected correctly')
    mongo = PyMongo(app)
    collection = mongo.db.notes

except:
    app.logger.info('Failed to connect')
    app.logger.info('Method insert_one init')

def insert_one(propery):
    app.logger.info('Method insert_one init')
    result_operation = collection.insert_one(propery)
    result = propery
    result['_id'] = result_operation.inserted_id
    app.logger.info(f'Result insert: {result_operation.inserted_id}')
    app.logger.info('Method insert_one ending')
    return result

def find():
    app.logger.info('Method find init')
    result_operation = list(collection.find())
    app.logger.info(f'Result search: {result_operation}')
    app.logger.info('Method find ending')
    return result_operation