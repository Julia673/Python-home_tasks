#23.02 

from random import choice 
from string import ascii_letters 
from random import randint 
from itertools import permutations 
from datetime import datetime

#task 1 

number = randint(1, 11) 
print ('Try to guess the number:') 
i=0 
while 1: 
    if i==3: 
        print ('You lost!The number was% i'%number) 
        break 
    else:
         number_user=int(input()) 
         if number_user<number: 
             print('The number is greater. Try again !') 
         elif number_user>number: 
             print('The numberis less. Try again !') 
         else:
              print('WE Congratulate you the Winner !') 
              break 
    i+=1 
    
#task 2 

name=input() 
age=int(input()) 
print('Hello %s, on your next birthday you’ll be% i years.' % (name,age+1))

#task 3 #all possible words from letters word = input() n=len(word) print(*[''.join(i) for i in permutations(sorted(word),int(n))],sep=' ')
