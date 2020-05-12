# Day 7
# task 1

def  favorite_movie(n):
  print('My favorite movie is named {}'.format(n))

favorite_movie(input())

# task 2
def dicte(**kwargs):
   return kwargs

def make_country ():
    name=input()
    capital=input()
    return dicte(name= name,capital=capital)

country=make_country ()
print(country)

#task 3

def input_date():
    st=list(input())
    return st
  
def make_operation(a,st):
  i=int()
  if a=='+':
      s=0
      for i in st:
       i=int(i)
       s+=i
      return s
  elif  a=='-':
      for i in st:
       i=int(i)
       s-=(-i)
      return s
  elif a=='*':
      s=1
      for i in st:
       i=int(i)
       s*=i
      return s
    
st=input_date()
a=st.pop(0)
x=make_operation(a,st)
print(x)
