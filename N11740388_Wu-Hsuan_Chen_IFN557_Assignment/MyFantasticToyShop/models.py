# class Toy:
#     def __init__(self, id, image, name, price, category, description):
#         self.id = id
#         self.image = image
#         self.name = name
#         self.price = price
#         self.category = category
#         self.description = description

#     def get_toy_detail(self):
#         return str(self)
    
#     def __repr__(self):
#         str = "ID: {}, Image: {}, Name: {}, Price: {}, Category: {}, description: {} \n"
#         str = str.format(self.id, self.image, self.name, self.price, self.category, self.description)
#         return str

from . import db

class Toy(db.Model):
    __tablename__ = 'toys'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    image = db.Column(db.String(64), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    description = db.Column(db.String(500), nullable=False, default='There is no description.')

    def __repr__(self):
         str = "ID: {}, Name: {}, Image: {}, Price: {}, Category_id: {}, Description: {}\n"
         str = str.format(self.id, self.name, self.image, self.price, self.category_id, self.description)
         return str

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True) 
    toy_id = db.Column(db.Integer, db.ForeignKey('toys.id'), primary_key=True)
    order_detail_id = db.Column(db.Integer, db.ForeignKey('order_details.id'))
    amount = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        str = "ID: {}, Toy ID: {}, Order Detail ID: {}, Amount: {}, Total Price: {}\n" 
        str = str.format(self.id, self.toy_id, self.order_detail_id, self.amount, self.total_price)
        return str
    
    
class Order_detail(db.Model):
    __tablename__ = 'order_details'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), nullable=False)
    lastname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        str = "ID: {}, First Name: {}, Last Name: {}, Email: {}, Address: {}\n" 
        str = str.format(self.id, self.firstname, self.lastname, self.email, self.address)
        return str
    
class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)

    def __repr__(self):
        str = "ID: {}, Name: {}\n"
        str = str.format(self.id, self.name)
        return super().__repr__()
    