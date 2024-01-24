#21 number game

print('Welcome to 21 number game.\n')

while True:

    mode=int(input('Press 1:Play with Computer.\nPress 2: Play with Friends \nPress 3: exit.\n Choose mode:'))

    if(mode==1):
        print('Welcome!. Computer vs Player1')

        num_list=[]
        while len(num_list)<=21:
            choice=input('Press 1:Play first.\n Press 2:Play second \nEnter choice:')


    elif(mode==2):
        print('This is mode 2')
    elif(mode==3):
        exit()
    else:
        print('Enter valid character!')