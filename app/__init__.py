from flask import Flask

from app.ext import init_ext, cache
from app.shop.views import shop
from app.upload.views import upload_blue

app = Flask(__name__)
app.debug = True


def create_app():
    init_ext(app=app)
    register_blue()
    return app


def register_blue():
    app.register_blueprint(shop, url_prefix='/shop')
    app.register_blueprint(cache, url_prefix='/cache')
    app.register_blueprint(upload_blue, url_prefix='/upload_blue')