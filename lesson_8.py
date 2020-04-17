# Home work
# task 1
def oops(lis):
    try:
        for i in range(10):
            a=lis[i]
    except IndexError:
        print ('Oops!  That index was not found')

lis=[1,2,3,4]
lis_2={1:'uv',2:'ouuh',3:'iyg',4:'kjb '}
try:
    oops(lis)
    oops(lis_2)
except KeyError :
    print ('Oops!  That key was not found ')

#task 2
while True:
    try:
     a=int(input("Please enter a first number: "))
     b=int(input("Please enter a  second number: "))
     c=a*a/b
     print(c)
     break
    except ValueError:
     print("Oops!  That was no valid number.  Try again...")
    except ZeroDivisionError:
        print("Oops!  That was zero number.  Try again...")

