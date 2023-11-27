import random


r = 'y'

while r == 'y':
    no = random.randint(1,6)
    i = input('Do you want to roll the dice   ')
    if(i == 'yes'):
        r='y'
    elif(i=='no'):
        r='n'
    else:
        print('please type yes or no')
    if(r=='y'):
        if(no == 1):
            print('[   ]')
            print('[ 0 ]')
            print('[   ]')
        elif(no == 2):
            print('[ 0 ]')
            print('[   ]')
            print('[ 0 ]')
        elif(no == 3):
            print('[ 0 ]')
            print('[ 0 ]')
            print('[ 0 ]')
        elif(no == 4):
            print('[0 0]')
            print('[   ]')
            print('[0 0]')
        elif(no == 5):
            print('[0 0]')
            print('[ 0 ]')
            print('[0 0]')
        elif(no == 6):
            print('[0 0]')
            print('[0 0]')
            print('[0 0]')
    

