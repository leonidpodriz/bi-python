import random

pc_wins = 0
my_wins = 0
ties = 0
my_choice = input("Enter your choice: ")  # Take a look on this line
result = ''

while my_choice != 'quit':
    my_list = ['scissor', 'paper', 'rock']
    pc = random.choice(my_list)
    if pc == 'scissor':
        if my_choice == 'paper':
            result = 'PC win'
        elif my_choice == 'rock':
            result = 'You win'
        elif my_choice == 'scissor':
            result = 'Tie'
    elif pc == 'paper':
        if my_choice == 'rock':
            result = 'PC win'
        elif my_choice == 'scissor':
            result = 'You win'
        elif my_choice == 'paper':
            result = 'Tie'
    elif pc == 'rock':
        if my_choice == 'scissor':
            result = 'PC win'
        elif my_choice == 'paper':
            result = 'You win'
        elif my_choice == 'rock':
            result = 'Tie'
    else:
        print('Undefined')
    print('PC choose:', pc)
    if result == 'PC win':
        pc_wins += 1
    elif result == 'You win':
        my_wins += 1
    elif result == 'Tie':
        ties += 1
    print('PC wins:', pc_wins)
    print('Your wins:', my_wins)
    print('Ties:', ties)

    my_choice = input("Enter your choice: ")  # Take a look on this line

wins = [pc_wins, my_wins, ties]
max_wins = max(wins)
if max_wins == pc_wins:
    print('The winner is PC')
elif max_wins == my_wins:
    print('You are the winner')
else:
    print('Friendship wins')
