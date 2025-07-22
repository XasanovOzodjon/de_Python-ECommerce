from models.user import User
from utils import clr, print_status, cheak_username, search_user
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
            if user.password == password:
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
        
        
    def is_admin(self):
        if self.current_user and self.current_user.admin:
            return True
        return False