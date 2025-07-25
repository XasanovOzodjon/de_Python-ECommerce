from models.user import User
from models.product import Product
from utils import clr, print_status, cheak_username, search_user, make_password
from getpass import getpass
class Manager:
    def __init__(self):
        self.users = User.load_users()
        self.current_user = None

    def register_user(self):
        user = User.create_user()
        if user:
            self.users.append(user)
            User.save_users(self.users)
            return True
        return False

    def Login(self):
        username = input("Enter your username: ").lower()
        password = getpass("Enter your password: ")
        clr()
        user = search_user(username, self.users)
        if user != -1:
            if user.password == make_password(password):
                self.current_user = user
                clr()
                print_status(f"Xush kelibsiz, {user.first_name}!", "succes")
                return True
            else:
                clr()
                print_status("Noto'g'ri parol. Iltimos, qaytadan urinib ko'ring.", "error")
                return False
        else:
            clr()
            print_status("Foydalanuvchi topilmadi.", "error")
            return False
        
    def show_products(self):
        if not self.current_user:
            clr()
            print_status("Siz tizimga kirmagansiz.", "error")
            return
        
        products = Product.load_products()
        if not products:
            clr()
            print_status("Hozirda mahsulotlar mavjud emas.", "info")
            return
        
        clr()
        print("Mahsulotlar:")
        for ii in range(len(products)):
            product = products[ii]
            print(f"{ii + 1}. {product.name} - {product.price} so'm")

        choice = input("\nMahsulotni tanlang (1-{}): ".format(len(products)))
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(products):
                product = products[choice - 1]
                clr()
                print(f"---------{product.name}----------")
                print(f"ID: {product.id}")
                print(f"Narxi: {product.price} so'm")
                print(f"Kategoriyasi: {product.category}")
                print(f"Qisqacha: {product.description}")
                print(f"Qoldiq: {product.in_stock} dona")
                print(f"Yaratilgan: {product.created_at}\n")
                in_cart = input("Siz ushbu mahsulotni savatchaga qo'shmoqchimisiz? (1: ha / Enter : yo'q): ")
                if in_cart == '1':
                    if product.in_stock > 0:
                        self.current_user.in_cart.append(product)
                        product.in_stock -= 1
                        Product.save_products(Product.load_products())
                        User.save_users(self.users)
                        clr()
                        print_status(f"{product.name} savatchaga qo'shildi.", "succes")
                    else:
                        clr()
                        print_status("Mahsulotning qoldig'i tugagan.", "error")
            else:
                print("Noto'g'ri tanlov.")
        else:
            print("Iltimos, raqam kiriting.")

    def view_cart(self):
        if not self.current_user:
            clr()
            print_status("Siz tizimga kirmagansiz.", "error")
            return
        
        if not self.current_user.in_cart:
            clr()
            print_status("Savatchangiz bo'sh.", "info")
            return
        
        clr()
        print("Savatchangiz:")
        for ii, product in enumerate(self.current_user.in_cart, start=1):
            print(f"{ii}. {product.name} - {product.price} so'm")
        
        choice = input("Savatchani tozalash uchun 't' ni bosing yoki Enter ni bosing: ")
        if choice.lower() == 't':
            self.current_user.in_cart.clear()
            User.save_users(self.users)
            clr()
            print_status("Savatcha tozalandi.", "succes")
    
    def is_admin(self):
        if self.current_user and self.current_user.admin:
            return True
        return False