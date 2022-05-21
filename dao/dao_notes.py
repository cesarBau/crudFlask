import os
from flask import Flask
from commons.connection import mongo_connection

app = Flask(__name__)

collection = mongo_connection.db.notes


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