from .utils import clr
def is_valid_username(username: str) -> bool:
    return username.isalnum()
    

def is_valid_password(password: str) -> bool:
    return len(password) >= 8


def check_firstname(name: str) -> bool:
    if not name.isalpha():
        clr()
        print("Ismingizda faqat harflar bo'lishi kerak.\n")
        return False
    if len(name) > 20:
        clr()
        print("Ismingiz 20 ta xarfdan uzun bo'lmasligi kerak.\n")
        return False
    if len(name) < 3:
        clr()
        print("Ismingiz 3 ta xarfdan uzun bo'lishi kerak.\n")
        return False
    return True
    
def check_lastname(name: str) -> bool:
    if not name.isalpha():
        clr()
        print("Familiyangizda faqat harflar bo'lishi kerak.\n")
        return False
    if len(name) > 20:
        clr()
        print("Familiyangiz 20 ta xarfdan uzun bo'lmasligi kerak.\n")
        return False
    if len(name) < 3:
        clr()
        print("Familiyangiz 3 ta xarfdan uzun bo'lishi kerak.\n")
        return False
    return True


def check_password(password, confirm) -> bool:
    if password != confirm:
        clr()
        print("Password va confirm password bir xil emas\n")
        return False
    if len(password) < 8:
        clr()
        print("Parol kamida 8 ta belgidan iborat bulsin\n")
        return False
    if len(password) > 32:
        clr()
        print("Parolingiz juda uzun\n")
        return False
        
    return True

def cheak_admin(username:str) -> list:
    if username.startswith("admin::08="):
        username.replace("admin::08=", "")
        return [username.replace("admin::08=", ""), True]
    
    return [username, False]

def search_user(username: str, users: list):
    min_s = 0
    max_s = len(users) - 1

    while min_s <= max_s:
        curent_s = (min_s + max_s) // 2
        current_username = users[curent_s].username

        if username == current_username:
            print("Foydalanuvchi topildi")
            return users[curent_s]
        elif username < current_username:
            max_s = curent_s - 1
        else:
            min_s = curent_s + 1

    print("Topilmadi")
    return -1


def cheak_username(username: str, users: list) -> bool:
    if username in [user.username for user in users]:
        clr()
        print("Bu foydalanuvchi nomi allaqachon mavjud.\n")
        return False
    if username == "":
        clr()
        print("Foydalanuvchi nomi bo'sh bo'lmasligi kerak.\n")
        return False
    if not username.isalnum():
        clr()
        print("Foydalanuvchi nomi faqat harflar va raqamlardan iborat bo'lishi kerak.\n")
        return False
    if len(username) > 15:
        clr()
        print("Foydalanuvchi nomi 15 ta belgidan uzun bo'lmasligi kerak.\n")
        return False
    if len(username) < 3:
        clr()
        print("Foydalanuvchi nomi 3 ta belgidan uzun bo'lishi kerak.\n")
        return False
    return True


def check_phone(phone: str, users) -> bool:
    if phone in [user.phone for user in users]:
        clr()
        print("Bu telefon raqami boshqa akkauntga ulangan.\n")
        return False
    if not phone.isdigit():
        clr()
        print("Telefon raqamingizda faqat raqamlar bo'lishi kerak.\n")
        return False
    if len(phone) != 9:
        clr()
        print("Telefon raqamingiz XX-XXX-XX-XX formatida bo'lishi kerak.\n")
        return False
    return True

def check_age(age: int) -> bool:
    if not age.isdigit():
        clr()
        print("Yoshingiz raqam bo'lishi kerak.\n")
        return False
    age = int(age)
    if age < 0:
        clr()
        print("Yoshingiz manfiy bo'lmasligi kerak.\n")
        return False
    if age < 18:
        clr()
        print("Siz 18 yoshdan katta bo'lishingiz kerak.\n")
        return False
    if age > 100:
        clr()
        print("Siz juda katta yoshdasiz.\n")
        return False
    return True

def check_gender(gender: str) -> bool:
    if gender not in ["male", "female", "other"]:
        clr()
        print("Jinsingiz 'male', 'female' yoki 'other' bo'lishi kerak.\n")
        return False
    return True