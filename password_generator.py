import random

password_lenght = int(input('Enter lentght of your password : '))

string = '''abcdrfghijklmnopqrtstuvwxyz0123456789ABCDRFGHIJKLMNOPQRTSTUVWXYZ!'+%&/()=*?-_<>'''

password = ''.join(random.sample(string,password_lenght))
print(password)


