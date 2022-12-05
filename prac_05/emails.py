EMAILS = {}


def main():
    email = validate_email()
    names = email.split("@")



def validate_email():
    email = input("Email: ")
    if "@" not in email:
        print("Must be Valid Email")
    email = input("Email: ")
    return email
