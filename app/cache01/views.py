from flask import Blueprint

from app.ext import cache

cache_blue = Blueprint('cache', __name__)

@cache.cached()
@cache_blue.route('/1/')
def cache_test1():
    print('天台见')
    return '1111'