#25.02

from random import randint 
from random import randrange 
from random import random 

#task 1
#version a)

arr=[] 
maxi=0 
for i in range(10): 
    arr.append(randint(1,100)) 
    if maxi<arr[i]: 
        maxi=arr[i] 
print(arr,maxi)

#version b)
arr=[] 
for i in range(10): 
    arr.append(randint(1,100)) 
print (arr,max(arr))

#version c)
arr=[] 
for i in range(10):
    arr.append(randrange(10, 50, 5)) 
print (arr,end='') 
arr.sort() 
print(arr[9])

#version d)
arr = [int(random()*100) for i in range(10)] 
print (arr,end='') 
arr.sort() 
arr.reverse() 
print(arr[0])

#task2

#version a)
num1=[int(random()*10) for i in range(10)] 
num2=[] 
num=[] 
for i in range(10): 
    num2.append(randrange(11)) 
j=0 
for i in range(10): 
    if num1[i]!=num2[i]: 
        k=0 
        n=0 
        for j in range(len(num)): 
            if num[j]==num1[i]: 
                k=1 
            elif num[j]==num2[i]: 
                    n=1 
                    if k==0: 
                        num.append(num1[i]) 
                        if n==0: 
                            num.append(num2[i])

print(num1,num2,num,sep='\n')

#version b)
num1=[int(random()*10) for i in range(10)] 
num2=[int(random()*10) for i in range(10)] 
num=num1.copy() 
num3=num2[:] 
num.sort() 
num.sort()#-1 2 3 
num3.sort() 
num.sort(reverse=True) #-10 9 8 
i=0 
for i in range(10):
   j=0 
   while True: 
       if num3[i]==num[j]: 
           break 
       if j ==9: 
           num.append(num3[i]) 
           break 
j+=1 
for i in range(11): 
    if i in num: 
       k=num.count(i) 
       if k>1: 
           k=num.index(i) 
           num.pop(k) 
           num.remove(i) 
print(num1,num2,num,sep='\n')

#task 3
#version a)

num=[] 
num1= list(range(1, 100))# задає просту послідовність 1 2 3 4 .... 
for i in num1: 
    if i%7==0 and i%5!=0: 
        num.append(i) 
print (num,end='\n')

#version b)
num=[] 
num1= list(range(1, 100)) 
for i in range(101): 
    if i%7==0 and i%5!=0: 
        num.append(i) 
print (num)