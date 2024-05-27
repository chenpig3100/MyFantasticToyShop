class Toy:
    def __init__(self, id, image, name, price, category, description):
        self.id = id
        self.image = image
        self.name = name
        self.price = price
        self.category = category
        self.description = description

    def get_toy_detail(self):
        return str(self)
    
    def __repr__(self):
        str = "ID: {}, Image: {}, Name: {}, Price: {}, Category: {}, description: {} \n"
        str = str.format(self.id, self.image, self.name, self.price, self.category, self.description)
        return str
        
    