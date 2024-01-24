#You have to guess at which index position 0 is present.1

from random import shuffle

def shuffleList(guess_list=''):
    shuffle(guess_list)
    return guess_list

def checkGuess(guess,shuffled_guess_list=''):
    if(shuffled_guess_list[guess]==0):
        print('You guessed right!')
    else:
        print('You guessed wrong.Try again!')
        guess=int(input('Guess postion of zero from 0,1,2:'))
        checkGuess(guess,shuffled_guess_list)



guess_list=[1,0,2]
shuffled_guess_list=shuffleList(guess_list)

guess=int(input('Guess postion of zero from 0,1,2:'))

checkGuess(guess,shuffled_guess_list)