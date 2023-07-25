from random import randint
from emoji import emojize

print('=-=' * 20)
print('\033[31mJo\033[m-\033[33mKen\033[m-\033[36mPo\033[m')
print('=-=' * 20)

cpu = randint(1, 3)

play = str(input('''\n\033[31mRock\033[m \033[33mPaper\033[m \033[36mScissors\033[m 
       ''')).strip().lower()

if cpu == 1 and play == 'rock':
    print('AGAIN!')
elif cpu == 1 and play == 'paper':
    print(emojize("You win! I'm rock :cry:", use_aliases=True))
elif cpu == 1 and play == 'scissors':
    print(emojize("You loose! I'm rock :grin:", use_aliases=True))

elif cpu == 2 and play == 'rock':
    print(emojize("You loose! I'm paper :grin:", use_aliases=True))
elif cpu == 2 and play == 'paper':
    print('AGAIN!')
elif cpu == 2 and play == 'scissors':
    print(emojize("You win! I'm paper :cry:", use_aliases=True))

elif cpu == 3 and play == 'rock':
    print(emojize("You win! I'm scissors :cry:", use_aliases=True))
elif cpu == 3 and play == 'paper':
    print(emojize("You loose! I'm scissors :grin:", use_aliases=True))
else:
    print('AGAIN!')
