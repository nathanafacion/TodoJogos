from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import uuid
from tinydb import TinyDB, Query

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
db = TinyDB('db.json')

CORS(app, resources={r'/*': {'origins': '*'}})

JOGOS = db.all()

@app.route('/jogos', methods=['GET', 'POST'])
def all_jogos():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        JOGOS.insert({
             'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'type': post_data.get('type'),
        })
        response_object['message'] = 'Jogo adicionado'
    else:
        response_object['jogos'] = JOGOS
    return jsonify(response_object)

@app.route('/jogos/<jogo_id>', methods=['GET', 'PUT', 'DELETE'])
def single_jogo(jogo_id):
    response_object = {'status': 'success'}
    if request.method == 'GET':
        return_jogo = ''
        for jogo in JOGOS:
            if jogo['id'] == jogo_id:
                return_jogo = jogo
        response_object['jogo'] = return_jogo
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_jogo(jogo_id)
        JOGOS.insert({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'type': post_data.get('type'),

        })
        response_object['message'] = 'Jogo updated!'
    if request.method == 'DELETE':
        remove_jogo(jogo_id)
        response_object['message'] = 'Jogo removed!'
    return jsonify(response_object)

def remove_jogo(jogo_id):
    for jogo in JOGOS:
        if jogo['id'] == jogo_id:
            JOGOS.remove(jogo)
            return True
    return False

if __name__ == '__main__':
    app.run()