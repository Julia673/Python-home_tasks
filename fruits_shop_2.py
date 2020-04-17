# Day 7

#  Second option

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

# price and count products

shop_sal=[]
for i in range(36):
 coun=[randint(5,80)for i in range(36)]
 price=[]
for i in range(36):
    price.append(randint(20,100))
    
#money for the product
    
money=[]
for i in range(36):
   money.append(price[i]*coun[i])
    
#tuple information about sale
    
shop_sal= zip(price,coun,money)
shop_sal=list( shop_sal)
print(shop_sal)
#dict customers and their order

product={}
cust={}
j=0
for k in pers:
    for i in prod:
       product[i]=shop_sal[j]
       j+=1
    cust[k]=product
    print(k,cust[k],sep='\n')
suma_price=[]
suma=[]
p=[]
for i in pers:
 print(i)
 for j in prod:
  a=cust[i].get(j)
  suma.append(a[0])
  p.append(a[2])
      #print(suma,p,sep='\n')

   
print(suma)

#money for all products









 

    
