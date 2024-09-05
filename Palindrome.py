def is_palindrome(string):
    cleaned_string = string.replace(" ", "").lower()
    if cleaned_string == cleaned_string[::-1]:
        return True
    else:
        return False
string = input("Enter a word or phrase to check if it's a palindrome: ")
if is_palindrome(string):
    print(string,"is a palindrome")
else:
    print(string,"is not a palindrome")
