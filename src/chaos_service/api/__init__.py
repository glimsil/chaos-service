from flask import Blueprint
from chaos_service.config.config_storage import ConfigStorage
api = Blueprint('api', __name__)
config = ConfigStorage()
from chaos_service.api.v1.chaos_api import *