import secrets
import string

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))
    print("Generated Password:", generate_password(password_length))
