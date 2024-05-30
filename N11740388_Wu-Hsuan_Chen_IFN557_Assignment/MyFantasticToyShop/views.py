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


