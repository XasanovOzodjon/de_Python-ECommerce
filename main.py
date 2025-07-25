
from utils import print_login_menu, print_status, clr, print_market_menu_user, print_market_menu_admin
from manager import Manager


def user_market(manager: Manager):
    while True:
        print_market_menu_user()
        choice = input(">> ")

        if choice == '1':
            manager.show_products()
        elif choice == '2':
            manager.view_cart()
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            clr()
            print("Siz Akkauntdan chiqdingiz.")
            break
        else:
            clr()
            print_status("Noto'g'ri tanlov. Iltimos, qaytadan urinib ko'ring.", "error")
                

def main():
    manager = Manager()
    while True:
        print_login_menu()
        choice = input(">> ")
        
        if choice == '1':
            if manager.Login():
                if manager.is_admin():
                    clr()
                    print_status("Xush kelibsiz, Admin!", "succes")
                    print_market_menu_admin()
                else:
                    clr()
                    user_market(manager)

        elif choice == '2':
            if manager.register_user():
                clr()
                print_status("Foydalanuvchi muvaffaqiyatli ro'yxatdan o'tdi.", "succes")
            else:
                clr()
                print_status("Foydalanuvchi ro'yxatdan o'tishda xatolik yuz berdi.", "error")
                
        elif choice == '3':
            clr()
            print("Siz Dasturdan chiqdingiz.")
            break
        else:
            clr()
            print_status("Noto'g'ri tanlov. Iltimos, qaytadan urinib ko'ring.", "error")


if __name__ == "__main__":
    main()