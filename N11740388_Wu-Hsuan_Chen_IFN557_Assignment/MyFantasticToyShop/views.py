from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Toy, Order, Order_detail, ContactUs, Category
from sqlalchemy.orm import aliased
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    toys = Toy.query.order_by(Toy.name).all()
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

@bp.route('/toy/<int:toyid>/')
def toydetail(toyid):
    toys = Toy.query.order_by(Toy.name).all()
    category_alias = aliased(Category)
    toy = db.session.query(Toy.name.label('toy_name'), Toy.image, Toy.description,Toy.price, category_alias.name.label('category_name')).join(category_alias, Toy.category_id==category_alias.id).filter(Toy.id == toyid).first()
    return render_template('ProductDetailPage.html', toy = toy, toys = toys)

@bp.route('/submit', methods=['POST','GET'])
def submit():
    contactus = ContactUs(firstname = request.values.get('firstname'), 
                          lastname = request.values.get('lastname'), 
                          email = str(request.values.get('Email')), 
                          comment = request.values.get('comment'))

    try:
        
        db.session.add(contactus)
        db.session.commit()
        flash('Thank you for your submit!')

    except Exception as e:
        flash('Submit fail...')
        print(e)

    return redirect(url_for('main.index'))

# checkout function #Bryan
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

# navigate to orderdetail page #Bryan 
@bp.route('/check')
def check():
    return render_template('Orderdetail.html')

# Add toy function #Bryan
# @bp.route('/add/<int:toyid>/')
# def add(toyid):

    
#     toy = Toy.query.get_or_404(toyid)
#     #check order exist
#     if 'order_id' in session:
#         order_id = session['order_id']
#         order = db.session.scalar(db.select(Order).where(Order.id==session['order_id']).first())
#         #order_check = Order.query.where((Order.toy_id == toyid) & (Order.id == order.id))

#         if order_check is None:
#             o1 = Order()
#             o1.id = order.id
#             o1.toy_id = toyid
#             o1.amount = 1
#             o1.total_price = toy.price * o1.amount
#             db.session.add(o1)
#             session['order_id']=order.id
#         else:
#             order_check.amount += 1
#             order_check.total_price = toy.price * order_check.amount
#     else:

#         o1 = Order()
#         o1.toy_id = toyid
#         o1.amount = 1
#         o1.total_price = toy.price * o1.amount
#         db.session.add(o1)
#         session['order_id']=o1.id

#     try:
#         db.session.commit()
#         flash('add toy complete')
#     except Exception as e:
#         print(e)

#     return redirect(url_for('main.index'))  


#check toyid exist in order 
    # toy = Toy.query.filter(Toy.id == toyid).first()

    # order_check = Order.query.where((Order.toy_id == toyid) & (Order.id == order.id))
    # if order_check is None:
    #     o1 = Order()
    #     o1.toy_id = toyid
    #     o1.amount = 1
    #     o1.total_price = toy.price * o1.amount
    #     db.session.add(o1)
    #     session['order_id']=order.id
    # else:
    #     order_check.amount += 1
    #     order_check.total_price = toy.price * order_check.amount

    # try:
    #     db.session.commit()
    #     flash('add toy complete')
    # except Exception as e:
    #     print(e)
        
# check have order.id exist or not #Bryan
# def checkSession():
#     if 'order_id' in session.keys():
#         order = db.session.scalar(db.select(Order).where(Order.id==session['order_id']).first())

#     else:
#         order = None

#     if order is None:
#         # Order 在創建的時候要Order.id 與 Toy.id 一起給，兩個都是PK
#         order = Order()
#         try:
#             db.session.add(order)
#             db.session.commit()
#             session['order_id']=order.id
#         except Exception as e:
#             print(e)

#     return order
