import random
import string

ascci       = string.ascii_letters
digits      = string.digits
punctuation = string.punctuation
options     = ascci + digits + punctuation

while True:
    number_user = input('\nInforme o tamanho da senha que deseja: ')

    if number_user.isdigit():
        number_user = int(number_user)
        break
    else:
        print('\nInforme um valor numérico!')
        continue

password    = ''

for i in range (0, number_user):
    choice_c    = random.choice(options)
    password    = password + choice_c

print(f'\nSenha gerada com sucesso: \n\n{password}\n')
