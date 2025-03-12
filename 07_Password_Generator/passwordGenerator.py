import random

print('Welcome to Password Generator Application')

chars ='!@#$%^&*()_+1234567890\
qwertyuiopasdfghjklzxcvbnm,.;\
ABCDEFGHIJKLMNOPQRSTUVWXYZ'

number = int(input('How many passwords you want to generate? '))
length = int(input('What should be the password length? '))

print('\n Here are your passwords:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords+=random.choice(chars)
    print(passwords)

