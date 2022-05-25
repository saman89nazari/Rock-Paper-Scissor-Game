import random

choise = ['r','p','s']

choise_meani = {
    'r': 'Rock',
    'p': 'Paper',
    's': 'Scissor',
}

user_score = 0
ai_score = 0

for i in range(5):
    user_input = input('Your choise from Rock, Paper, Scissor (r, p , s): ')
    
    ai_choises = random.choice(choise)

    if user_input in choise:
        print(f'Your chois is: {choise_meani[user_input]}. / AI choies is {choise_meani[ai_choises]}.')
        if user_input == ai_choises:
            print ('Tei')
        elif user_input == 'r' and ai_choises == 's':
            print('user+1!')
            user_score += 1
        elif user_input == 'p' and ai_choises == 'r':
            print('user+1!')
            user_score += 1
        elif user_input == 's' and ai_choises == 'p':
            print('user+1!')
            user_score += 1
        else:
            print('AI+1!')
            ai_score += 1
    else:
        print('Invalid Input')
        
    print(f'User Score: {user_score} // AI Score: {ai_score}.')
    print('-' * 10, '\n')    
if user_score > ai_score:
    print(f'User won with {user_score} . ')
elif user_score < ai_score:
    print(f'AI won with {ai_score} . ')
else:
    print(f'Its a Tei with {ai_score} Score.')
    