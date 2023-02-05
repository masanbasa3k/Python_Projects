import random

# Enter lenght
password_lenght = int(input('Enter lentght of your password : '))

# alphabet, numbers and symbols
string = '''abcdrfghijklmnopqrtstuvwxyz0123456789ABCDRFGHIJKLMNOPQRTSTUVWXYZ!'+%&/()=*?-_<>'''

# creating password with random
password = ''.join(random.sample(string,password_lenght))
print(password)


