from flask import Flask
from dao.dao_notes import insert_one, find

app = Flask(__name__)

def controller_notes_get():
    app.logger.info('Method controller_notes_get init')
    message = find()
    result = message
    app.logger.info('Method controller_notes_get ending')
    return result

def controller_notes_post(body):
    app.logger.info('Method controller_notes_post init')
    app.logger.info(f'Petition body : {body}')
    message = insert_one(body)
    result = message
    app.logger.info('Method controller_notes_post ending')
    return result

def controller_notes_put(note_id, body):
    app.logger.info('Method controller_notes_put init')
    app.logger.info(f'Path param : {note_id}')
    app.logger.info(f'Petition body : {body}')
    result = body
    app.logger.info('Method controller_notes_put ending')
    return result

def controller_notes_deleted(note_id, body):
    app.logger.info('Method controller_notes_deleted init')
    app.logger.info(f'Path param : {note_id}')
    result = body
    app.logger.info('Method controller_notes_deleted ending')
    return result

def controller_notes_patch(note_id, body):
    app.logger.info('Method controller_notes_patch init')
    app.logger.info(f'Path param : {note_id}')
    app.logger.info(f'Petition body : {body}')
    result = body
    app.logger.info('Method controller_notes_patch ending')
    return result
