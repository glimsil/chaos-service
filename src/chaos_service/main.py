import click
from flask import Flask
from chaos_service.api import api, config
from chaos_service.config.config_storage import ConfigStorage


@click.group()
@click.version_option("0.0.1")
def cli():
    """
    First version of chaos service.
    """



@cli.command()
@click.option('--start-at-request', help='Start returning 500 error at request number N. (This is the default option starting at 10)', required=False)
@click.option('--chance-of-sucess', help='Probability of returning error(0-100). If 100 informed it has 100 percent of chance of returning 200.', required=False)
@click.option('--chance-of-sucess-until-hit', help='Probability of starting to return error(0-100). If 100 informed it has 100 percent of chance of returning 200. When the first error hits, the next calls will be errors', required=False)
def bad_request(start_at_request, chance_of_sucess, chance_of_sucess_until_hit):
    """Start api for to test bad request failures."""
    config.create_config("bad_request", start_at_request, chance_of_sucess, chance_of_sucess_until_hit)
    app = Flask(__name__)
    app.register_blueprint(api)
    app.run(port=8080)

@cli.command()
@click.option('--start-at-request', help='Start returning 500 error at request number N. (This is the default option starting at 10)', required=False)
@click.option('--chance-of-sucess', help='Probability of returning error(0-100). If 100 informed it has 100 percent of chance of returning 200.', required=False)
@click.option('--chance-of-sucess-until-hit', help='Probability of starting to return error(0-100). If 100 informed it has 100 percent of chance of returning 200. When the first error hits, the next calls will be errors', required=False)
def internal_server_error(start_at_request, chance_of_sucess, chance_of_sucess_until_hit):
    """Start api to test internal server error failures."""
    config.create_config("internal_server_error", start_at_request, chance_of_sucess, chance_of_sucess_until_hit)
    app = Flask(__name__)
    app.register_blueprint(api)
    app.run(port=8080)

@cli.command()
@click.option('--start-at-request', help='Start returning 502 error at request number N. (This is the default option starting at 10)', required=False)
@click.option('--chance-of-sucess', help='Probability of returning error(0-100). If 100 informed it has 100 percent of chance of returning 200.', required=False)
@click.option('--chance-of-sucess-until-hit', help='Probability of starting to return error(0-100). If 100 informed it has 100 percent of chance of returning 200. When the first error hits, the next calls will be errors', required=False)
def bad_gateway(start_at_request, chance_of_sucess, chance_of_sucess_until_hit):
    """Start api for to test bad gateway failures."""
    config.create_config("bad_gateway", start_at_request, chance_of_sucess, chance_of_sucess_until_hit)
    app = Flask(__name__)
    app.register_blueprint(api)
    app.run(port=8080)

@cli.command()
@click.option('--start-at-request', help='Start returning 503 error at request number N. (This is the default option starting at 10)', required=False)
@click.option('--chance-of-sucess', help='Probability of returning error(0-100). If 100 informed it has 100 percent of chance of returning 200.', required=False)
@click.option('--chance-of-sucess-until-hit', help='Probability of starting to return error(0-100). If 100 informed it has 100 percent of chance of returning 200. When the first error hits, the next calls will be errors', required=False)
def service_unavailable(start_at_request, chance_of_sucess, chance_of_sucess_until_hit):
    """Start api for to test service unavailable failures."""
    config.create_config("service_unavailable", start_at_request, chance_of_sucess, chance_of_sucess_until_hit)
    app = Flask(__name__)
    app.register_blueprint(api)
    app.run(port=8080)

@cli.command()
@click.option('--start-at-request', help='Start returning 504 error at request number N. (This is the default option starting at 10)', required=False)
@click.option('--chance-of-sucess', help='Probability of returning error(0-100). If 100 informed it has 100 percent of chance of returning 200.', required=False)
@click.option('--chance-of-sucess-until-hit', help='Probability of starting to return error(0-100). If 100 informed it has 100 percent of chance of returning 200. When the first error hits, the next calls will be errors', required=False)
def gateway_timeout(start_at_request, chance_of_sucess, chance_of_sucess_until_hit):
    """Start api for to test gateway timeout failures."""
    config.create_config("gateway_timeout", start_at_request, chance_of_sucess, chance_of_sucess_until_hit)
    app = Flask(__name__)
    app.register_blueprint(api)
    app.run(port=8080)

@cli.command()
@click.option('--start-at-request', help='Start returning 500 error at request number N. (This is the default option starting at 10)', required=False)
@click.option('--chance-of-sucess', help='Probability of returning error(0-100). If 100 informed it has 100 percent of chance of returning 200.', required=False)
@click.option('--chance-of-sucess-until-hit', help='Probability of starting to return error(0-100). If 100 informed it has 100 percent of chance of returning 200. When the first error hits, the next calls will be errors', required=False)
def connection_refused(start_at_request, chance_of_sucess, chance_of_sucess_until_hit):
    """Start api to test connection refused failures. It will shut down the server when error criteria appers."""
    config.create_config("connection_refused", start_at_request, chance_of_sucess, chance_of_sucess_until_hit)
    app = Flask(__name__)
    app.register_blueprint(api)
    app.run(port=8080)
    

@cli.command()
@click.option('--start-at-request', help='Start returning 500 error at request number N.', required=False)
@click.option('--chance-of-sucess', help='Probability of returning error(0-100). If 100 informed it has 100 percent of chance of returning status 200 OK. (For chaos this is the default option with 90 percent of success rate)', required=False)
@click.option('--chance-of-sucess-until-hit', help='Probability of starting to return error(0-100). If 100 informed it has 100 percent of chance of returning 200. When the first error hits, the next calls will be errors', required=False)
def chaos(start_at_request, chance_of_sucess, chance_of_sucess_until_hit):
    """Start api to test all types of failures randomically. It will shut down the server when error criteria appers."""
    if(start_at_request is None and chance_of_sucess is None and chance_of_sucess_until_hit is None):
        chance_of_sucess = 90
    config.create_config("chaos", start_at_request, chance_of_sucess, chance_of_sucess_until_hit)
    app = Flask(__name__)
    app.register_blueprint(api)
    app.run(port=8080)