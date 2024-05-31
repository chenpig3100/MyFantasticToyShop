from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Toy, Order_detail, Order
from . import db
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

@bp.route('/category/<int:category>')
def category(category):
    match category:
        case 1:
            toys = Toy.query.filter(Toy.category_id == category).all()
        case 2:
            toys = Toy.query.filter(Toy.category_id == category).all()
        case 3:
            toys = Toy.query.filter(Toy.category_id == category).all()
        case 4:
            toys = Toy.query.order_by(Toy.name).all()

    return render_template('Homepage.html', toys = toys)
    
@bp.route('/toys')
def search():
    search = request.args.get('search')
    search = '%{}%'.format(search)
    toys = Toy.query.filter(Toy.name.like(search)).all()
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



#orderDetail function (Ian)
@bp.route('/checkout', methods=['POST','GET'])
def checkout():
    order_detail = Order_detail(order_id = request.values.get('order_id'), 
                                firstname = request.values.get('firstname'), 
                                lastname = request.values.get('lastname'),
                                email = request.values.get('email'),
                                address = request.values.get('address'))
    
    try:
        db.session.add(order_detail)
        db.session.commit()
        flash('Thanks for order')
        return redirect(url_for('main.index'))
    
    except:
        flash('There was an issue completing your order')
        return redirect(url_for('main.index'))    

@bp.route('/check')
def check():
    return render_template('Orderdetail.html')

# @bp.route('/add')
# def ADD():
#     checkSession()
#     if toyid == None
#         toy= Order()
#         toy.id = order.id
#         toy.amount =
#         toy.toy_id = 
#         toy.total_price =

def checkSession():
    if 'order_id' in session.keys():
        order = db.session.scalar(db.select(Order).where(Order.id==session['order_id']))

    else:
        order = None

    if order is None:
        order = Order()
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id']=order.id
        except Exception as e:
            print(e)
            print('Fail')


