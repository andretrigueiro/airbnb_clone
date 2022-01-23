import os

from flask import Flask, jsonify
from flask_cors import CORS

# configuration
DEBUG = True

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'api.sqlite'),
    )

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # sanity check route
    @app.route('/ping', methods=['GET'])
    def ping_pong():
        return jsonify('pong!')

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app

# from flask import Flask, jsonify
# from flask_cors import CORS

# # configuration
# DEBUG = True

# # instantiate the app
# app = Flask(__name__)
# app.config.from_object(__name__)

# # enable CORS
# CORS(app, resources={r'/*': {'origins': '*'}})


# # sanity check route
# @app.route('/ping', methods=['GET'])
# def ping_pong():
#     return jsonify('pong!')

# @app.route('/GuestUser', methods=['GET'])
# def guest_user():
#     return jsonify({
#         'status': 'success',
#     })

# if __name__ == '__main__':
#     app.run()
