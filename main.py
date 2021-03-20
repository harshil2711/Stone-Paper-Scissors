# Import random module for computer sides input.
import random

a = ['rock', 'paper', 'scissors']

com = random.choice(a)

# non-customizable variables.

i = 1

user_point = 0

com_point = 0

remain_chance = 10


print('Welcome to the  rock paper scissors game.......\U0001F600\U0001F600\U0001F600')
print()
print('Here total chances are 10 and the winner who will get highest points ')
print()


# Total chances are 10 and here total 10 round starts.
while i < 11:
    
# Ask for user side input.
    user = input('Enter your input....(rock , paper , scissors) \n')
    user = user.lower()
    
# checking conditions.
    if com == 'rock' and user == 'scissors':
        print(f'compuer :{com}  and you :{user} huh...you loss')
        com_point = com_point + 1
        print(f'computer`s point are :{com_point}')
        print(f'your point are :{user_point}')
        remain_chance = remain_chance - 1
        print(f'total remaining chances are :{remain_chance}')

    elif com == 'scissors' and user == 'paper':
        print(f'compuer :{com}  and you :{user} huh...you loss')
        com_point = com_point + 1
        print(f'computer`s point are :{com_point}')
        print(f'your point are :{user_point}')
        remain_chance = remain_chance - 1
        print(f'total remaining chances are :{remain_chance}')

    elif com == 'paper' and user == 'rock':
        print(f'compuer :{com}  and you :{user} huh...you loss')
        com_point = com_point + 1
        print(f'computer`s point are :{com_point}')
        print(f'your point are :{user_point}')
        remain_chance = remain_chance - 1
        print(f'total remaining chances are :{remain_chance}')

    elif com == 'scissors' and user == 'rock':
        print(f'compuer :{com}  and you :{user} hurray....you win')
        user_point = user_point + 1
        print(f'user`s points are :{user_point}')
        print(f'computer`s point are :{com_point}')
        remain_chance = remain_chance - 1
        print(f'total remaining chances are : {remain_chance}')

    elif com == 'rock' and user == 'paper':
        print(f'compuer :{com}  and you :{user} hurray....you win')
        user_point = user_point + 1
        print(f'user`s points are :{user_point}')
        print(f'computer`s point are :{com_point}')
        remain_chance = remain_chance - 1
        print(f'total remaining chances are : {remain_chance}')

    elif com == 'paper' and user == 'scissors':
        print(f'compuer :{com}  and you :{user} hurray....you win')
        user_point = user_point + 1
        print(f'user`s points are :{user_point}')
        print(f'computer`s point are :{com_point}')
        remain_chance = remain_chance - 1
        print(f'total remaining chances are : {remain_chance}')

    elif com == user:
        print('you and com select same sign....match tie')
        remain_chance = remain_chance - 1
        print(f'user`s points are :{user_point}')
        print(f'computer`s point are :{com_point}')
        print(f'total remaining chances are :{remain_chance}')

    i = i + 1

print()
# counting total points and declare the result out of 10 rounds.

if com_point > user_point:
    print('huh...you loss the game')

elif user_point > com_point:
    print('hurray....you win the game')

elif com_point == user_point:
    print('match is tie')
print()

# printing the individual points of user and computer.

print(f'your total points are {user_point}')
print()
print(f'computer total points are {com_point}')
print()
print('game over')
