#word guessing game

import random

words=['Hello','Hii','Basic','opera','dive','veggie']

random_word=random.choice(words)

name=input('Enter your name:')

while True:
   
   is_play=input(f'Hello {name}.\nDo you want to continue?yes[Y/y] no[N/n]')
   
   if (is_play=='y'or is_play=='Y'):
      
      count=12
      word=''
      i=0
      random_letter=''

      while i<len(random_word) :

        print(f'Chances remaining:{count}')
        random_letter=input('Guess a letter:')

        if(random_word[i]==random_letter):
            i+=1
            count-=1
            word+=random_letter
            print(f'Right! word=\'{word}\'')
           
        else:
           is_true=False
           count-=1
           print(f'Wrong! word=\'{word}\'')
           if(count!=0):
              print('Wrong!Try again')
        
       

        if(count!=0 and i==len(random_word)):
           print('You won!')
           exit()

        if(count==0 and i!=len(random_word)):
           print('You lose!')
           exit()
   elif (is_play=='n' or is_play=='N'):
      exit()
   else:
       print('Enter valid character!')
   
   
   
