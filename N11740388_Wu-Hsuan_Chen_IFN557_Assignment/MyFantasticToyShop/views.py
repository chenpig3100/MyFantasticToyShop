from flask import Blueprint, render_template, url_for, request, session, flash
from .models import Toy

# This data will eventually be stored in a database
# HelloKitty = Toy(1, 'HelloKitty.jpg', 'HelloKitty', '$10', 'plushi','This adorable Hello Kitty plushie features soft, cuddly fabric and a cute pink bow. With her friendly smile, she is perfect for hugs, decoration, and gifting to Hello Kitty fans of all ages.')
# IronMan = Toy(2, 'ironMan.jpg', 'IronMan', '$100', 'collection', 'Marvel at the ultimate Iron Man collection: suits, gadgets, and comics galore, embodying heroism, innovation, and technological prowess.')
# toys = [HelloKitty, IronMan]

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    toys = Toy.query.order_by(Toy.name).all()
    # return render_template('Homepage.html', toybox = toys)
    return render_template('Homepage.html', toys = toys)

# @bp.route('/ProductDetailPage/<int:toyid>/')
# def toys(toyid):
#     newToyBoxs = []
#     for Toy in toys:
#         if int(Toy.id) == int(toyid):
#             newToyBoxs.append(Toy)
#     return render_template('ProductDetailPage.html', toybox = newToyBoxs)

@bp.route('/toy/<int:toyid>/')
def toydetail(toyid):
    toys = Toy.query.all()
    toy = Toy.query.filter(Toy.id == toyid).first()
    print(toy.image)
    return render_template('ProductDetailPage.html', toy = toy, toys = toys)

