from hashlib import sha256


def make_password(password: str) -> str:
    return sha256(password.encode()).hexdigest()
    
def clr():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
