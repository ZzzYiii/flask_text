from flask import Blueprint, render_template, request, redirect

from app.ext import db
from .models import Shop

shop = Blueprint('shop', __name__)


@shop.route('/save/')
def save_all():
    objects = []
    for i in range(1, 101):
        objects.append(Shop(name='念旧' + str(i)))
    db.session.bulk_save_objects(objects)
    db.session.commit()
    return 'ok'


@shop.route('/limit/<int:page>/<int:size>/')
def query_limit(page, size):
    paginate = Shop.query.order_by(Shop.sid).paginate(page=page, per_page=size, error_out=False)
    shops = paginate.items
    return render_template('shop/index.html', shops=shops, paginate=paginate)


# @shop.route('/add/',methods=['POST'])
# def add_shop():
#     if request.method == 'GET':
#         pass
#     elif request.method == 'POST':
#         pass

# @shop.route('/search/<int:page>/<int:size>/', methods=['POST'])
# def search_shop(page, size):
#     content = request.form.get('content')
#     shops = Shop.query.filter(Shop.name.like('%' + content + '%'))
#     paginate = shops.query.order_by(Shop.sid).paginate(page=page, per_page=size, error_out=False)
#     shops = paginate.items
#     return render_template('shop/search.html', shops=shops, paginate=paginate)


@shop.route('/add/', methods=['get', 'post'])
def add_shop():
    if request.method == 'GET':
        sid = request.values.get('sid')
        shop = Shop.query.get(sid)
        return render_template('shop/add_shop.html', shop=shop)
    elif request.method == 'POST':
        name = request.values.get('name')
        price = request.values.get('price')
        expiration_date = request.values.get('expiration_date')
        status = request.values.get('status')
        shop = Shop(name=name,
                    price=price,
                    expiration_date=expiration_date,
                    status=status)
        db.session.add(shop)
        db.session.commit()
        return redirect('/shop/limit/1/10/')


@shop.route('/change/', methods=['get', 'post'])
def change_shop():
    if request.method == 'GET':
        sid = request.values.get('sid')
        shop = Shop.query.get(sid)
        return render_template('shop/change_shop.html', shop=shop)
    elif request.method == 'POST':
        sid = request.values.get('sid')
        name = request.values.get('name')
        price = request.values.get('price')
        expiration_date = request.values.get('expiration_date')
        status = request.values.get('status')
        Shop.query.filter(Shop.sid == sid).update({Shop.name: name,
                                                   Shop.price: price,
                                                   Shop.expiration_date: expiration_date,
                                                   Shop.status: status})
        db.session.commit()
        return redirect('/shop/limit/1/10/')
