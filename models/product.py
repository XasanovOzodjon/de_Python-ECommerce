from datetime import datetime


class Product:

    def __init__(self, id=None, name=None, description=None, price=None, category=None, stock=None, created_at=None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.stock = stock
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        self.products = self.load_products()
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'category': self.category,
            'stock': self.stock,
            'created_at': self.created_at,
        }   
        
    @classmethod
    def from_dict(cls, data):
        product = cls()
        product.id = data['id']
        product.name = data['name']
        product.description = data['description']
        product.price = data['price']
        product.category = data['category']
        product.stock = data['stock']
        product.created_at = data['created_at']
        return product
    
    @classmethod
    def load_products(cls):
        import json
        try:
            with open('database/products.json') as jsonfile:
                data = json.load(jsonfile)
        except FileNotFoundError:
            data = []
        return [cls.from_dict(item) for item in data]
    
    
    @classmethod
    def save_products(cls, products):
        import json
        with open('database/products.json', 'w') as jsonfile:
            data = [product.to_dict() for product in products]
            json.dump(data, jsonfile, indent=2)
            
    @classmethod
    def create_product(cls):
        id = input("ID: ")
        name = input("Product Name: ")
        description = input("Description: ")
        price = float(input("Price: "))
        category = input("Category: ")
        stock = int(input("Stock: "))
        
        return cls(id, name, description, price, category, stock)
    