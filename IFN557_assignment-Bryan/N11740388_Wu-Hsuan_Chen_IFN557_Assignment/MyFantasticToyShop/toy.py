class Toy:
    def __init__(self, name, price, category, description):
        self.name = name
        self.price = price
        self.category = category
        self.description = description

    def get_toy_detail(self):
        return str(self)
    
    def __repr__(self):
        str = "Name: {}, Price: {}, Category: {}, description: {} \n"
        str = str.format(self.name, self.price, self.category, self.description)
        return str
    
    
    