from flask import Blueprint, request, render_template

from app.ext import images

upload_blue = Blueprint('upload', __name__)
'''
文件上传必须是post请求  form—data格式
'''
'''
UploadSet方法
1.save（）
参数：1.request.files（字典）
2.url
'''


@upload_blue.route('/img/', methods=['GET', 'POST'])
def upload_img():
    if request.method == 'POST':
        images.save(request.files['img'])
        return ''
    # 文件上传对象
    # request.files
    elif request.method == 'GET':
        return render_template('upload/upload.html')
