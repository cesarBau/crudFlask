from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from controller.controller_notes import controller_notes_get, controller_notes_post, controller_notes_put, controller_notes_deleted, controller_notes_patch
import json

app = Flask(__name__)
CORS(app)

def body_response(body={}, status=200):
    return Response(json.dumps(body,default=str), mimetype="application/json", status=status)

@app.route('/')
def home_page():
    return jsonify(hello='world')

@app.route('/notes',methods=['GET','POST'])
def notes():
    app.logger.info('Method notes init')
    if request.method == 'GET':
        app.logger.info('GET')
        params = dict(request.args)
        app.logger.info(f'Params: {params}')
        message, status, count_all= controller_notes_get(params)
        result = body_response(message, status)
        result.headers['X-Total-Count'] = count_all
    else:
        app.logger.info('POST')
        body = dict(request.json)
        message = controller_notes_post(body)
        result = body_response(message,201)
    return result

@app.route('/notes/<note_id>',methods=['PUT', 'DELETE', 'PATCH'])
def notes_id(note_id):
    app.logger.info('Method notes_id init')
    if request.method == 'PUT':
        app.logger.info('PUT')
        body = dict(request.json)
        message = controller_notes_put(note_id, body)
        result = body_response(message,204)
    elif request.method == 'DELETE':
        app.logger.info('DELETE')
        message, status = controller_notes_deleted(note_id)
        result = body_response(message,status)
    else:
        app.logger.info('PATCH')
        body = dict(request.json)
        message, status = controller_notes_patch(note_id, body)
        result = body_response(message, status)
    app.logger.info('Method notes_id ending')
    return result

@app.errorhandler(404)
def not_found(error=None):
    app.logger.info('Error: not_found')
    message = {
        'url': request.url,
        'error': error
    }
    app.logger.error(message)
    result = body_response(message,404)
    return result

@app.errorhandler(405)
def method_not_allowed(error=None):
    app.logger.info('Error: method_not_allowed')
    message = {
        'url': request.url,
        'error': error
    }
    app.logger.error(message)
    result = body_response(message,405)
    return result

@app.errorhandler(400)
def method_bat_request(error=None):
    app.logger.info('Error: method_bat_request')
    message = {
        'url': request.url,
        'error': error
    }
    app.logger.error(message)
    result = body_response(message,405)
    return result
    
