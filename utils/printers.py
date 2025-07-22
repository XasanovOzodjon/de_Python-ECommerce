from termcolor import colored


def print_status(text, status):
    status_map = {
        'error': 'red',
        'succes': 'green'
    }
    text = colored(text, status_map.get(status, 'red'))
    print(text)
    
def print_login_menu():
    print(colored("1. Login", "cyan"))
    print(colored("2. Register", "cyan"))
    print(colored("3. Exit", "cyan"))
    
    
def print_market_menu_user():
    print(colored("1. View Products", "cyan"))
    print(colored("2. View Cart", "cyan"))
    print(colored("3. View Orders", "cyan"))
    print(colored("4. View Profile", "cyan"))
    print(colored("5. Logout", "cyan"))
    
def print_market_menu_admin():
    print(colored("1. View Products", "cyan"))
    print(colored("2. Add Product", "cyan"))
    print(colored("3. Update Product", "cyan"))
    print(colored("4. Delete Product", "cyan"))
    print(colored("5. View Orders", "cyan"))
    print(colored("6. View Users", "cyan"))
    print(colored("7. Logout", "cyan"))