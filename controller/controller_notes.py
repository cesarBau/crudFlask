from flask import Flask
from bson.objectid import ObjectId
from bson.errors import InvalidId
from dao.dao_notes import insert_one
from services.services_notes import service_notes_get, service_notes_deleted, service_notes_put

app = Flask(__name__)


def controller_notes_get(params):
    app.logger.info('Method controller_notes_get init')
    result = {'message': 'Debe de existir page y perpage para usar paginado'}
    status = 200
    count_all = 0
    if 'perpage' in params and 'page' not in params:
        status = 400
    elif 'page' in params and 'perpage' not in params:
        status = 400
    else:
        result, count_all = service_notes_get(params)
    app.logger.info('Method controller_notes_get ending')
    return result, status, count_all


def controller_notes_post(body):
    app.logger.info('Method controller_notes_post init')
    app.logger.info(f'Petition body : {body}')
    result = insert_one(body)
    app.logger.info('Method controller_notes_post ending')
    return result


def controller_notes_put(note_id, body):
    app.logger.info('Method controller_notes_put init')
    app.logger.info(f'Path param : {note_id}')
    app.logger.info(f'Petition body : {body}')
    result = service_notes_put(note_id, body)
    app.logger.info('Method controller_notes_put ending')
    return result


def controller_notes_deleted(note_id):
    app.logger.info('Method controller_notes_deleted init')
    status = 204
    app.logger.info(f'Path param : {note_id}')
    try:
        validation = ObjectId(note_id)
        app.logger.info(validation)
        result = service_notes_deleted(note_id)
    except InvalidId:
        result = {'message': 'id no valido'}
        status = 400
        app.logger.info(result)
    app.logger.info('Method controller_notes_deleted ending')
    return result, status
