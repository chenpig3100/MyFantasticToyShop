from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Toy, Order, Order_detail, ContactUs, Category
from sqlalchemy.orm import aliased
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    toys = Toy.query.order_by(Toy.name).all()
    orders = checkorder()
    return render_template('Homepage.html', toys = toys, orders = orders)

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
    toy = db.session.query(Toy.id, Toy.name.label('toy_name'), Toy.image, Toy.description,Toy.price, category_alias.name.label('category_name')).join(category_alias, Toy.category_id==category_alias.id).filter(Toy.id == toyid).first()

    orders = checkorder()
    return render_template('ProductDetailPage.html', toy = toy, toys = toys, orders = orders)

@bp.route('/submit', methods=['POST','GET'])
def submit():
    contactus = ContactUs(firstname = request.values.get('firstname'), 
                          lastname = request.values.get('lastname'), 
                          email = str(request.values.get('Email')), 
                          comment = request.values.get('comment'))
    
    db.session.add(contactus)

    try:
        db.session.commit()
        flash('Thank you for your submit!')

    except Exception as e:
        db.session.rollback()
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
    
    db.session.add(order_detail)

    try:
        db.session.commit()
        flash('Thanks for order')
        return redirect(url_for('main.index'))
    
    except:
        db.session.rollback()
        flash('There was an issue completing your order')
        return redirect(url_for('main.index')) 


# navigate to orderdetail page #Bryan 
@bp.route('/check')
def check():
    return render_template('Orderdetail.html')


# Add function
@bp.route('/add/<int:toyid>', methods=['POST'])
def add(toyid):
    toy = Toy.query.get_or_404(toyid)

    # Check if order exists in session
    if 'order_id' in session:
        order_id = session.get('order_id')
        order = Order.query.get(order_id)
        if order is None:
            flash('Order not found.')
            order = Order()
            db.session.add(order)
            db.session.flush()
            session['order_id'] = order.id
            
    else:
        # If no order exists in session, create a new order
        order = Order()
        db.session.add(order)
        db.session.flush() # Ensure the new order gets an ID before using it
        session['order_id'] = order.id

    # Check if the toy is already in the order
    order_detail = Order_detail.query.filter_by(order_id=order.id, toy_id=toyid).first()
    if order_detail is None:
        # If the toy is not already in the order, add it
        new_order_detail = Order_detail(order_id=order.id, toy_id=toyid, amount=1, total_price=toy.price)
        db.session.add(new_order_detail)
    else:
        # If the toy is already in the order, increase the amount
        order_detail.amount += 1
        order_detail.total_price = toy.price * order_detail.amount

    try:
        db.session.commit()
        flash('Toy added to the order successfully!')
    except Exception as e:
        db.session.rollback()
        flash(f'Error adding toy to the order: {e}')

    return redirect(url_for('main.index'))

@bp.route('/subtract/<int:toyid>', methods=['POST'])
def subtract(toyid):
    if 'order_id' not in session:
        flash('No active order found.')
        return redirect(url_for('main.index'))
    
    order_id = session.get('order_id')
    order_detail = Order_detail.query.filter_by(order_id=order_id, toy_id=toyid).first()

    if order_detail is None:
        flash('Toy not found in the order.')
        return redirect(url_for('main.index'))
    
    if order_detail.amount > 1:
        order_detail.amount -= 1
        order_detail.total_price = order_detail.toy.price * order_detail.amount

    else:
        db.session.delete(order_detail)

    try:
        db.session.commit()
        flash('Toy amount updated successfully!')
    except Exception as e:
        db.session.rollback()
        flash(f'Error updating toy amount: {e}')

    return redirect(url_for('main.index'))


def checkorder():
    order = Order_detail.query.order_by(Order_detail.order_id.desc()).first()
    if order is not None:
        orders = Order_detail.query.filter(Order_detail.order_id == order.order_id).all()
    else:
        orders = []
    return orders