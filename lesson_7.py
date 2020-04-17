# Auction
# Tour first

from random import randint

# goods

prod=['orange','pear','mango','apple','kiwi','plum']

# buyers

pers=['Alex','Bella','Stiven','Bill','Kate','Sara']

#price

price=[randint(20,100)for i in range(len(prod))]

# count fruns
count_fru=[randint(200,1000)for i in range(len(prod))]

#new buyers
print('''    Hello !
      We are glad to welcome you to the Fruit Paradise auction.
         Enter your name:'''
      )
p=input()
p=p.capitalize()

count=0
for i in pers:
    if i == p:
        print(' Welcome to the auction.  We are glad to see % s again.'% p)
        break
    else:
        count+=1       
if count==len(pers):
          print('Congratulations on registering for the auction.Good to see you here. % s'% p)
          pers.append(p)
          pers.sort()
print('Input yours money limit:','\n')
money=input()
if money.isdigit():
    money=int(money)
else:
    money=0
if money>0:
    print('\n','Bidders are:','\n')
    for i in pers:
      print(i,sep='\n')

    print('\n',' List of fruits to be auctioned today:','\n')
    print('Fruits','Number/kg','Price/UAH',sep='\t',end='\n')
    j=0
    for i in prod:
      print(i,count_fru[j],price[j],sep='\t\t',end='\n')
      j+=1
      
    count=0
    i=1
    order=[]
    while i>0 :    
      print('\n','Input what fruit do you want to duy :')
      f=input()
      f=f.lower()
      if prod.count(f)>0:
          if order.count(f)==0:
              order.append(f)
          print('Your application has been accepted.Do you want buy more?(Your answer Yes/No)',end='\n')
          answer=input()
          answer.lower()
          if answer!='yes':
              i-=1
      else:
             print("Sorry this fruit isn't auctioned today.")
             i-=1     
    order_frut={}
    if len(order)>0 :
        for i in order:
          ind=prod.index(i)
          print('How many % s do you want to duy :'%i)
          coun=int(input())
          if coun<count_fru[ind] or coun==count_fru[ind]:
              order_frut[i]=coun
             
          else:
              print('''Sorry we have not enouth fruits for you.
                    Do you want take only % i?(Answer Yes/No)'''%count_fru[ind])
              answer=input()
              answer.lower()
              if answer == 'yes':
                  order_frut[i]=count_fru[ind]
              else:
                  
                  continue
      
       
        print('The operation is confirmed.  Thank you for your purchase.')   
        print('\n',' Check :','\n')
        print('Fruits','Number/kg','Price/UAH',sep='\t',end='\n')
        col=0

        for i in order_frut:
            col+=order_frut[i]
            ind=prod.index(i)
            price_fru=price[ind]*order_frut[i]
            print(i,order_frut[i],price[ind],sep='\t\t',end='\n')
        print('Suma',col,price_fru,sep='\t\t')
        an=10

        if price_fru>money:
           print('''You have only% i .Your request does not match your funds limit.
                  Do you want to chande your request?(Answer Yes/No)'''% money)
           answer=input()
           answer.lower()
           if answer=='yes':
                print('''You can change one position if it does not help you,
                       please write your order again.
                       What do you want to change?
                      If number of fruits. Input : 1
                      If you want remove one kind of fruits.Input: 0''')
                an=int(input())
        if an==0:
            print('Input fruit what you want remove:')
            rem=input()
            if order.count(rem)>0:
              ind=order .index(rem)
              order.pop(ind)
            if len(order)<1:
               print('Your data wrong.') 
            else:
              print('Your data wrong.')
        elif an==1:
            
            print('Input fruit what you want less:')
            f=input()
            if order.count(f)>0:
             print('Your order was % i. Input your new number of fruits:'% order_frut[f])
             order_frut[f]=int(input())
             
        for i in order:
          ind=prod.index(i)
          price_fru_2=price[ind]*order_frut[i]
          if price_fru_2<price_fru:

                  print('The operation is confirmed.  Thank you for your purchase.')
                  print('\n',' Check :','\n')
                  print('Fruits','Number/kg','Price/UAH',sep='\t',end='\n')
                  col=0
                  for i in order_frut:
                    col+=order_frut[i]
                    ind=prod.index(i)
                    price_fru=price[ind]*order_frut[i]
                  print(i,order_frut[i],price[ind],sep='\t\t')
                  print('Suma',col,price_fru,sep='\t\t')
    else:
        #print('\n','Thank you for your visit.',end='\n')
        print('Your data wrong.')
else:
        print('Your data wrong.')

# Tour 2
sell=[]
print('Do you want to sell?(Answer Yes/No)',end='\n')
answer=input()
answer.lower()
if answer=='yes':
     print('How many kind of fruits do you want to sell:')
     num=input()
     if num.isdigit():
         num=int(num)
     else:
         num=0
     while num>0: 
        print ('What fruits do you want to sell:',end='\n')
        f=input()
        if prod.count(f)<1:
            prod.append(f)
        print('How many fruits do you want to sell:',end='\n')
        coun=input()
        if coun.isdigit():
          count_fru.append(int(coun))
        else:
          coun=0
          count_fru.append(coun)
        print ('Input   price fruit: ')
        pr=input()
        if pr.isdigit():
          price.append(int(pr))
        else:
          price=0
          price.append(pr)
        num-=1
if count>0:
    print('\n','Bidders are:','\n')
    for i in pers:
      print(i,sep='\n')
    print('\n',' List of fruits to be auctioned today:','\n')
    print('Fruits','Number/kg','Price/UAH',sep='\t',end='\n')
    j=0
    for i in prod:
      print(i,count_fru[j],price[j],sep='\t\t',end='\n')
      j+=1

    

