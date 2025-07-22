import json
from datetime import datetime
from uuid import uuid4
from utils import (
    make_password, print_status,
    clr, check_firstname, check_lastname,
    cheak_username, cheak_admin, check_password, check_age, 
    check_phone, check_gender
)
from getpass import getpass

class User:

    def __init__(self, idd, username, password, phone, first_name, last_name, age, gender, joined_at=None, admin=False):
        self.id = idd
        self.username = username
        self.password = password
        self.phone = phone
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.joined_at = joined_at or datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        self.admin = admin

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'phone': self.phone,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'gender': self.gender,
            'joined_at': self.joined_at,
            'admin': self.admin
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['id'],
            data['username'],
            data['password'],
            data['phone'],
            data['first_name'],
            data['last_name'],
            data['age'],
            data['gender'],
            data['joined_at'],
            data['admin']
        )

    @classmethod
    def load_users(cls):
        with open('database/users.json') as jsonfile:
            try:
                data = json.load(jsonfile)
            except:
                data = []

        users = [User.from_dict(item) for item in data]

        return users
    
    @classmethod
    def save_users(cls, users):
        with open('database/users.json', 'w') as jsonfile:
            data = [user.to_dict() for user in users]
            json.dump(data, jsonfile, indent=2)

    @classmethod
    def create_user(cls):
        clr()
        first_name = input("First Name: ")
        while not check_firstname(first_name):
            first_name = input("Enter your first name again: ").title()
            
        clr()
        last_name = input("Last Name: ")
        while not check_lastname(last_name):
            last_name = input("Enter your last name again: ").title()

        clr()
        username = input("Enter your username: ").lower()
        result = cheak_admin(username=username)
        username = result[0]
        while not cheak_username(username, User.load_users()):
            username = input("Enter your username again: ").lower()
            result = cheak_admin(username=username)
            username = result[0]
        
        clr()
        password = getpass("Password: ")
        confirm_password = getpass("Confirm Password: ")
        while not check_password(password, confirm_password):
            password = getpass("Enter your password: ")
            confirm_password = getpass("Confirm your password: ")
        
        clr()
        phone = input("Phone - +998  ")
        while not check_phone(phone):
            phone = input("Enter your phone number again: ")
        phone = phone.replace(" ", "").replace("-", "")
        
        clr()
        age = input("Age: ")
        
        while not check_age(age):
            age = input("Enter your age again: ")
        age = int(age)
        
        gender = input("Gender: ").lower()
        while not check_gender(gender):
            gender = input("Enter your gender again: ")

        user = cls(str(uuid4()), username, make_password(password), phone, first_name, last_name, age, gender)
        return user
