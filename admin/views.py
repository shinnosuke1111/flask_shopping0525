# flask関連のパッケージを取得
from flask import render_template, request, url_for, session, redirect, flash

# 「__init__.py」で宣言した変数appを取得
from admin import app

# Itemモデルを取得
from lib.models import TestItem, TestCategory

# SQLAlchemyを取得
from lib.db import db

# デコレーターに使用
from functools import wraps

# 商品一覧を表示
@app.route('/test_item')
def index():
  test_items = TestItem.query.order_by(TestItem.id.desc()).all()
  item_list = []
  for i in test_items:
    item_list.append(i.id)
    item_list.append(i.name)
    item_list.append(i.price)
  return item_list
  # return render_template('items/index.html', items=test_items)

  #商品カテゴリの表示
@app.route('/test_categorys')
def show_list():
  test_categorys = TestCategory.query.order_by(TestCategory.id.desc()).all()
  categorys_list = []
  for i in test_categorys:
    categorys_list.append(i.id)
    categorys_list.append(i.name)
  return categorys_list


@app.route('/items/<int:id>')
def show(id):
  item = TestItem.query.get(id)
  result = {}
  result["name"] = item.name
  result["price"] = item.price
  return result