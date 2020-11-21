import json
import os
from pathlib import Path

class ConfigStorage:
    DATA = {}

    def get_config(self):
        return self.DATA
    
    def create_config(self, chaos_type, start_at_request, chance_of_sucess, chance_of_sucess_until_hit):
        if(start_at_request is not None):
            start_at_request = int(start_at_request)
        if(chance_of_sucess is not None):
            chance_of_sucess = int(chance_of_sucess)
            if(chance_of_sucess > 100):
                chance_of_sucess = 100
            elif(chance_of_sucess < 0):
                chance_of_sucess = 0
        if(chance_of_sucess_until_hit is not None):
            chance_of_sucess_until_hit = int(chance_of_sucess_until_hit)
            if(chance_of_sucess_until_hit > 100):
                chance_of_sucess_until_hit = 100
            elif(chance_of_sucess_until_hit < 0):
                chance_of_sucess_until_hit = 0
        error_code = 0
        if(chaos_type == 'internal_server_error'):
            error_code = 500
        if(chaos_type == 'bad_request'):
            error_code = 400
        if(chaos_type == 'connection_refused'):
            error_code = -1
        self.DATA = { 
                "type" :  chaos_type,
                "start_at_request" : 10 if (start_at_request is None and chance_of_sucess is None and chance_of_sucess_until_hit is None) else start_at_request,
                "chance_of_sucess" : chance_of_sucess,
                "chance_of_sucess_until_hit" : chance_of_sucess_until_hit,
                "error_code" : error_code
                }
        print("create_config " + str(self.DATA) )
        return self.DATA