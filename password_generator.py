import random
import string

def password_generator():
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.ascii_letters
    s4 = string.digits
    s5 = string.punctuation
    pass_length = int(input("Enter the password length:\n"))
    s= []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    s.extend(list(s5))
    random.shuffle(s)
    random_password = ("".join(s[0:pass_length]))
    print(random_password)

password_generator()