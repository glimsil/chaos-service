from flask import request, jsonify
from chaos_service.api import api, config

import random 
import sys

GET_REQUEST_COUNTER=0
GET_REQUEST_ERROR=False
POST_REQUEST_COUNTER=0
POST_REQUEST_ERROR=False

CHAOS = [500, 501, 502, 503, 504, 505, 400, -1]

@api.route('/v1/chaos/get', methods=['GET'])
def chaos_get():
    global GET_REQUEST_COUNTER, GET_REQUEST_ERROR
    GET_REQUEST_COUNTER = GET_REQUEST_COUNTER + 1
    error_code = config.get_config()['error_code']
    if(config.get_config()['start_at_request'] is not None and GET_REQUEST_COUNTER >= config.get_config()['start_at_request']):
        GET_REQUEST_ERROR = True
    if(config.get_config()['chance_of_sucess'] is not None and config.get_config()['chance_of_sucess'] < 100):
        if(random.randint(0, 100) > config.get_config()['chance_of_sucess']):
            if(config.get_config()['error_code'] == 0):
                random_int = random.randint(0, len(CHAOS)-1)
                error_code = CHAOS[random_int]
                print(str(error_code) + " - " + str(random_int))
            
            print(str(error_code) + " = is -1? " + str(error_code == -1))
            if(error_code == -1):
                sys.exit()
            return jsonify({ 'status': config.get_config()['type'], "request_counter": GET_REQUEST_COUNTER }),error_code
    if(config.get_config()['chance_of_sucess_until_hit'] is not None and config.get_config()['chance_of_sucess_until_hit'] < 100):
        if(random.randint(0, 100) > config.get_config()['chance_of_sucess_until_hit']):
            GET_REQUEST_ERROR = True

    if(GET_REQUEST_ERROR):
        if(error_code == -1):
            sys.exit()
        return jsonify({ 'status': config.get_config()['type'], "request_counter": GET_REQUEST_COUNTER }),error_code
    return jsonify({ 'status': 'ok', "request_counter": GET_REQUEST_COUNTER })




@api.route('/v1/chaos/post', methods=['POST'])
def chaos_post():
    global POST_REQUEST_COUNTER, POST_REQUEST_ERROR
    POST_REQUEST_COUNTER = POST_REQUEST_COUNTER + 1
    body = request.json
    error_code = config.get_config()['error_code']
    if(config.get_config()['start_at_request'] is not None and POST_REQUEST_COUNTER >= config.get_config()['start_at_request']):
        POST_REQUEST_ERROR = True
    if(config.get_config()['chance_of_sucess'] is not None and config.get_config()['chance_of_sucess'] < 100):
        if(random.randint(0, 100) > config.get_config()['chance_of_sucess']):
            if(config.get_config()['error_code'] == 0):
                random_int = random.randint(0, len(CHAOS)-1)
                error_code = CHAOS[random_int]
                print(str(error_code) + " - " + str(random_int))
            
            print(str(error_code) + " = is -1? " + str(error_code == -1))
            if(error_code == -1):
                sys.exit()
            return jsonify({ 'status': config.get_config()['type'], "request_counter": POST_REQUEST_COUNTER, "request_body": body }),error_code
    if(config.get_config()['chance_of_sucess_until_hit'] is not None and config.get_config()['chance_of_sucess_until_hit'] < 100):
        if(random.randint(0, 100) > config.get_config()['chance_of_sucess_until_hit']):
            POST_REQUEST_ERROR = True

    if(POST_REQUEST_ERROR):
        if(error_code == -1):
            sys.exit()
        return jsonify({ 'status': config.get_config()['type'], "request_counter": POST_REQUEST_COUNTER, "request_body": body }),error_code
    return jsonify({ 'status': 'ok', "request_counter": POST_REQUEST_COUNTER, "request_body": body })