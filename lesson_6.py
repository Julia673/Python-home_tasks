#Day 7
#task
from random import randint
a='orange'
b='pear'
c='mango'
d='grapefruit'
e='kiwi'
f='plum'
print(a,b,c,d,e,f,sep='\n')
print(a,b,c,d,e,f,sep=',',end='.')
#list 
prod=[]
prod.extend([a,b,c,d,e,f])
print('\n',prod)
for i in range(len(prod)-1):
    print(i,prod[i],sep=':')
#customers
pers=['Alex','Bella','Stiven','Bill','Kate','Sara']
print(pers)
#is word repeated in the list
for i in prod :
    coun=prod.count(i)
    if coun>1:
        print('The word is repeated in the list:%s'%i)
for i in pers:
    coun=pers.count(i)
    if coun>1:
        print('The word is repeated in the list:%s'%i)
#price and count products
price=[]
shop_sal=[]
coun=[randint(20,100)for i in range(6)]
for i in prod:
 price.append(randint(20,100))
#money for the product
money=[]
for i in range(6):
    money.append(price[i]*coun[i])
#tuple information about sale
shop_sal= zip(prod,price,coun,money)
shop_sal=list( shop_sal) 
#dict customers
cust={}
j=0
while(j<len(shop_sal)):
 for i in pers:
  cust[i]=shop_sal[j]
  j+=1
#money for all products    
suma_money=sum(money)
#suma products
suma_prod=sum(coun)
#put suma for dikt
cust['Suma']=(suma_prod,suma_money)
for i in cust.keys():
    print(i,cust[i],sep='\n')


 

    
