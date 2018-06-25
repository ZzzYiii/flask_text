import os

from flask import Flask
from flask_caching import Cache
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import UploadSet, configure_uploads, patch_request_class, IMAGES

db = SQLAlchemy()
migrate = Migrate()


def init_ext(app: Flask):
    config_db(app)
    db.init_app(app)
    init_cache_config(app)
    init_login_config(app)
    init_upload_config(app)
    migrate.init_app(app=app, db=db)


# 配置数据库连接的参数
def config_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'mysql+pymysql://root:root@127.0.0.1:3306/flask_text?charset=utf8'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    migrate.init_app(app, db)


cache = Cache()


# 缓存配置  flask-cache
def init_cache_config(app):
    cache.init_app(app, config={'CACHE_DEFAULT_TIMEOUT': 60,
                                'CACHE_TYPE': 'redis',
                                'CACHE_REDIS_HOST': '127.0.0.1',
                                'CACHE_REDIS_PORT': 6379,
                                'CACHE_REDIS_PASSWORD': '123456',
                                'CACHE_REDIS_DB': 1,
                                'CACHE_KEY_PREFIX': 'view_'})


# 用户模块登陆注册插件
login_manager = LoginManager()


def init_login_config(app):
    login_manager.init_app(app)


# 文件上传配置
images = UploadSet(name='images', extensions=IMAGES, default_dest=None)
'''
UploadSet（）参数说明
name：保存文件的子目录 默认是files
extensions：设置允许上传的文件类型  默认类型
default_dest：设置文件上传的根路径
'''
'''
配置信息
1> 配置文件上传的根目录
2> 

'''
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_ROOT_PATH = os.path.join(BASE_DIR, 'media/upload')


def init_upload_config(app):
    # 配置文件上传的根目录 #
    app.config['UPLOADS_DEFAULT_DEST'] = UPLOAD_ROOT_PATH
    # 生成文件的访问的url地址，可不配，可以默认生成url
    # app.config['UPLOAD_DEFAULT_URL'] = ''
    '''
    参数说明
    app：Flask对象
    uploads_set：文件上传核心类 UploadSet对象
    '''
    configure_uploads(app=app, upload_sets=images)
    # 限制文件上传的大小
    patch_request_class(app=app, size=16*1024*1024)