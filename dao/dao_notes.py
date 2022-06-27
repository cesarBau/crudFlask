import os
import traceback
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.logger.info('Try to connect to the database')
try:
    app.logger.info('Connected correctly')
    mongo = PyMongo(app)
    collection = mongo.db.notes
except Exception:
    traceback.print_exc()


def insert_one(propery):
    app.logger.info('Method insert_one init')
    result_operation = collection.insert_one(propery)
    result = propery
    result['_id'] = result_operation.inserted_id
    app.logger.info(f'Result insert: {result_operation.inserted_id}')
    app.logger.info('Method insert_one ending')
    return result


def find(select, propery):
    app.logger.info('Method find init')
    app.logger.info(f'Query mongo: {propery}')
    app.logger.info(f'projection mongo: {select}')
    result_operation = list(collection.find(filter=propery, projection=select))
    count_all = len(result_operation)
    app.logger.info(f'Result search: {result_operation}')
    app.logger.info(f'Count find: {count_all}')
    app.logger.info('Method find ending')
    return result_operation, count_all


def find_paginated(select, propery, pages):
    app.logger.info('Method find_subdocument init')
    skip = (pages['page'] - 1) * pages['perpage']
    app.logger.info(f'Query mongo: {propery}')
    app.logger.info(f'projection mongo: {select}')
    app.logger.info(f'Skip: {skip} and limit: {pages["perpage"]}')
    count_all = collection.count_documents(propery)
    result_operation = list(collection.find(
        filter=propery, projection=select).skip(skip).limit(pages['perpage']))
    app.logger.info(f'Result search: {result_operation}')
    app.logger.info(f'Count find: {count_all}')
    app.logger.info('Method find_subdocument ending')
    return result_operation, count_all


def update_one(note_id, propery):
    app.logger.info('Method insert_one init')
    result_operation = collection.update_one(note_id, propery, upsert=True)
    app.logger.info(f'result_operation: {result_operation.raw_result}')
    app.logger.info('Method insert_one ending')
    return result_operation


def delete_one(note_id):
    app.logger.info('Method delete_one init')
    result_operation = collection.delete_one(note_id)
    app.logger.info(result_operation.raw_result)
    app.logger.info('Method delete_one ending')
    return result_operation
