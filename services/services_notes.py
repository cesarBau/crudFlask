from flask import Flask
from bson.objectid import ObjectId
from dao.dao_notes import insert_one, find, find_paginated, delete_one, update_one
from commons.utils import create_select

app = Flask(__name__)


def service_notes_get(params):
    app.logger.info('Method service_notes_get init')
    select, params = create_select(params)
    if 'page' in params and 'perpage' in params:
        app.logger.info('find paginate')
        pages = {
            'page': int(params['page']),
            'perpage': int(params['perpage'])
        }
        del params['page']
        del params['perpage']
        result, count_all = find_paginated(select, params, pages)
    else:
        app.logger.info('find all')
        result, count_all = find(select, params)
    app.logger.info('Method service_notes_get ending')
    return result, count_all


def service_notes_post(body):
    app.logger.info('Method service_notes_post init')
    app.logger.info(f'Petition body : {body}')
    message = insert_one(body)
    result = message
    app.logger.info('Method service_notes_post ending')
    return result


def service_notes_put(note_id, body):
    app.logger.info('Method service_notes_put init')
    app.logger.info(f'Path param : {note_id}')
    app.logger.info(f'Petition body : {body}')
    result = update_one({'_id': ObjectId(note_id)}, {
        '$set': body
    })
    app.logger.info('Method service_notes_put ending')
    return result


def service_notes_deleted(note_id):
    app.logger.info('Method service_notes_deleted init')
    app.logger.info(f'note_id : {note_id}')
    result = delete_one({'_id': ObjectId(note_id)})
    app.logger.info('Method service_notes_deleted ending')
    return result


def service_notes_patch(note_id, body):
    app.logger.info('Method service_notes_patch init')
    app.logger.info(f'Path param : {note_id}')
    app.logger.info(f'Petition body : {body}')
    result = body
    app.logger.info('Method service_notes_patch ending')
    return result
