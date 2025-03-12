import random

points_user     = 0
points_computer = 0

print('\nSeja bem-vindo ao jogo Pedra, Papel e Tesoura!\n')

while True:
    choice          = ['r', 't', 'p']
    n_computer      = random.randint(0, 2)
    choice_computer = choice[n_computer]
    choice_user = input('Escolha R(pedra), T(tesoura), P(papel) ou Q(sair))').lower()

    if choice_user == 'q':
        print('OK, saindo!\n')
        break

    if choice_user not in choice:
        continue

    if choice_user == choice_computer:
        print('\nEmpate!\n')
    elif choice_user == 'r' and choice_computer == 't':
        print('\nVocê ganhou!\n')
        points_user += 1
    elif choice_user =='t' and choice_computer == 'p':
        print('\nVocê ganhou!\n')
        points_user += 1
    elif choice_user == 'p' and choice_computer == 'r':
        print('\nVocê ganhou!\n')
        points_user += 1
    else:
        print('\nVocê perdeu!\n')
        points_computer += 1
    
print(f'O jogo acabou!\n\nO placar final foi {points_user}x{points_computer}\n\nObrigado por jogar!\n')

if points_user > points_computer:
    print('VITÓRIA!!!\n')
elif points_user == points_computer:
    print('EMPATE!!!\n')
else:
    print('DERROTA!!!\n')