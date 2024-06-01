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
    amount = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        str = "ID: {}, Toy ID: {}, Order Detail ID: {}, Amount: {}, Total Price: {}\n" 
        str = str.format(self.id, self.toy_id, self.order_detail_id, self.amount, self.total_price)
        return str
    
    
class Order_detail(db.Model):
    __tablename__ = 'order_details'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
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
        return str

class ContactUs(db.Model):
    __tablename__ = 'contactus'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    email = db.Column(db.String(64))
    comment = db.Column(db.String(500))

    def __repr__(self):
        str = "ID: {}, First Name: {}, Last Name: {}, Email: {}, Comment: {}\n"
        str = str.format(self.id, self.firstname, self.lastname, self.email, self.comment)
        return str

    