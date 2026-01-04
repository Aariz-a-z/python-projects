import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def signup():
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed = hash_password(password)

    with open("users.txt", "a") as file:
        file.write(f"{username},{hashed}\n")

    print("Signup successful!")


def login():
    username = input("Username: ")
    password = input("Password: ")

    hashed = hash_password(password)

    try:
        with open("users.txt", "r") as file:
            for line in file:
                saved_user, saved_pass = line.strip().split(",")
                if username == saved_user and hashed == saved_pass:
                    print("Login successful!")
                    return
        print("Invalid credentials!")
    except FileNotFoundError:
        print("No users found.")


while True:
    print("\n1. Signup")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        signup()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
