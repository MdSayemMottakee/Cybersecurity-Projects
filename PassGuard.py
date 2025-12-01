import string
import getpass
import hashlib
import requests

def check_breach(password):
    """Check if password has been exposed in a known breach."""
    sha1pwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1pwd[:5], sha1pwd[5:]
    url = f"https://api.pwnedpasswords.com/range/{first5}"
    res = requests.get(url)
    
    if res.status_code != 200:
        print("Error checking password breach.")
        return False
    
    hashes = (line.split(":") for line in res.text.splitlines())
    for h, count in hashes:
        if h == tail:
            print(f"This password has appeared in {count} breaches! Change it immediately!")
            return True
    
    print("This password has NOT been found in known breaches.")
    return False

def check_pwd():
    password = getpass.getpass("Enter Password: ")
    strength = 0
    suggestions = []
    lower_count = upper_count = num_count = special_count = 0

    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char in string.punctuation:
            special_count += 1

    # Strength evaluation
    if lower_count >= 1:
        strength += 1
    else:
        suggestions.append("Add lowercase letters")
    if upper_count >= 1:
        strength += 1
    else:
        suggestions.append("Add uppercase letters")
    if num_count >= 1:
        strength += 1
    else:
        suggestions.append("Add numbers")
    if special_count >= 1:
        strength += 1
    else:
        suggestions.append("Add special characters")
    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Make password at least 8 characters long")

    # Strength remarks
    remarks_dict = {
        1: "Very Bad Password!!! Change ASAP",
        2: "Not A Good Password!!! Change ASAP",
        3: "Weak password, consider changing",
        4: "Good password, but can be stronger",
        5: "Strong password"
    }
    remarks = remarks_dict.get(strength, "Unknown strength")

    # Print results
    print("\nYour password has:")
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numeric characters")
    print(f"{special_count} special characters")
    print(f"Length: {len(password)} characters")
    print(f"\nPassword Strength: {strength}/5")
    print(f"Remark: {remarks}")
    if suggestions:
        print("Suggestions: " + ", ".join(suggestions))

    # Breach check
    check_breach(password)

def ask_pwd(another_pwd=False):
    while True:
        prompt = 'Do you want to enter another password (y/n): ' if another_pwd else 'Do you want to check a password (y/n): '
        choice = input(prompt).strip().lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == '__main__':
    print('Welcome to Password Strength Checker\n')
    ask_pw = ask_pwd()
    while ask_pw:
        check_pwd()
        print("\n--------------------------------\n")
        ask_pw = ask_pwd(True)
