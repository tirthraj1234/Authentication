import random
import string
print("welcome password genrator")
def password_genrator():
    length = int(input("Enter the password of length: "))
    lowerupper = string.ascii_letters
    digit = string.digits
    symbols = string.punctuation
    combine = lowerupper+digit+symbols
    x = random.sample(combine, length)
    password = "".join(x)
    print(password)
    print("sakshi.....")
password_genrator()
