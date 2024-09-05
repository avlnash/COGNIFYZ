def validate_email(email):
    if email.count('@') != 1:
        return False
    local_part, domain = email.split('@')
    if not local_part or not domain:
        return False
    if '.' not in domain:
        return False
    if domain.startswith('.') or domain.endswith('.'):
        return False
    return True
email = input("Enter an email address: ")
if validate_email(email):
    print("This is a valid email address.")
else:
    print("This is not a valid email address.")
