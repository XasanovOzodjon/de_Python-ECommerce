from datetime import datetime


class Product:

    def __init__(self, id=None, name=None, description=None, quantity=None, brand=None, price=None, category=None, stock=None, created_at=None):
        self.id = id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price
        self.category = category
        self.brand = brand
        self.in_stock = stock
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        self.products = []

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'category': self.category,
            'in_stock': self.in_stock,
            'created_at': self.created_at,
            'quantity': self.quantity,
            'brand': self.brand
        }

    @classmethod
    def from_dict(cls, data):
        product = cls()
        product.id = data['id']
        product.name = data['name']
        product.description = data['description']
        product.price = data['price']
        product.category = data['category']
        product.in_stock = data['in_stock']
        product.created_at = data['created_at']
        product.quantity = data['quantity']
        product.brand = data['brand']
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


    def view_product(self):
        for product in self.products:
            print(f"ID: {product.id}")
            print(f"Name: {product.name}")
            print(f"Description: {product.description}")
            print(f"Price: {product.price}")
            print(f"Category: {product.category}")
            print(f"Stock: {product.in_stock}")
            print(f"Created At: {product.created_at}")
            print("-" * 20)
        
    def retry(self):
        self.products = self.load_products()