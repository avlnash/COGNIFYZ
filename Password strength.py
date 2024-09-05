def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~" for char in password):
        strength += 1
    if strength == 5:
        return "Strong password!"
    elif 3 <= strength < 5:
        return "Moderate password."
    else:
        return "Weak password. Consider adding more variety in characters."
password = input("Enter a password to check its strength: ")
print(check_password_strength(password))

