from flask import request, jsonify
from chaos_service.api import api, config

import random 
import sys

GET_REQUEST_COUNTER=0
GET_REQUEST_ERROR=False


@api.route('/v1/chaos/get', methods=['GET'])
def chaos_get():
    global GET_REQUEST_COUNTER, GET_REQUEST_ERROR
    GET_REQUEST_COUNTER = GET_REQUEST_COUNTER + 1
    
    if(config.get_config()['start_at_request'] is not None and GET_REQUEST_COUNTER >= config.get_config()['start_at_request']):
        GET_REQUEST_ERROR = True
    if(config.get_config()['chance_of_sucess'] is not None and config.get_config()['chance_of_sucess'] < 100):
        if(random.randint(0, 100) > config.get_config()['chance_of_sucess']):
            if(config.get_config()['error_code'] == -1):
                sys.exit()
            return jsonify({ 'status': config.get_config()['type'], "request_counter": GET_REQUEST_COUNTER }),config.get_config()['error_code']
    if(config.get_config()['chance_of_sucess_until_hit'] is not None and config.get_config()['chance_of_sucess_until_hit'] < 100):
        if(random.randint(0, 100) > config.get_config()['chance_of_sucess_until_hit']):
            GET_REQUEST_ERROR = True

    if(GET_REQUEST_ERROR):
        if(config.get_config()['error_code'] == -1):
            sys.exit()
        return jsonify({ 'status': config.get_config()['type'], "request_counter": GET_REQUEST_COUNTER }),config.get_config()['error_code']
    return jsonify({ 'status': 'ok', "request_counter": GET_REQUEST_COUNTER })
