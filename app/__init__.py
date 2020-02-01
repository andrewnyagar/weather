from flask import Flask, jsonify
from app.views.views import views


def pageNotFound(error):
    return jsonify({
        "status":404,
        "message":"Page not found"
    }
    )


def createApp():
    pass
    app = Flask(__name__)
    app.register_blueprint(views,url_prefix="/")
    return app