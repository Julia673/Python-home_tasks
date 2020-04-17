# Phonbook
from random import randint
def input_names(f_name):
    # read  full names
    if f_name.readable():
     list_name=f_name.readlines()
     f_name.close()
     return   list_name
    else:
      print('Error')

    
def input_numper(f_num,count):
    # create number
  list_number=[]
  while count>0:
    num='+380'
    for i in range(8):
        i=str(randint(0,10))
        num=num+i
    list_number+=[num]
    count-=1
  if f_num.writable():
      for i in range(0,len(list_number)):
        f_num.write(list_number[i]+'\n')
      f_num.close()
      return list_number
  else:
      print('Error')
    
def sity(count,f_sity):
    #read if need creat sity  
  if f_sity.readable():
       sity=f_sity.readlines()
       f_sity.close()
       if count>len(sity):
            len_sit=len(sity)
            num=count-len_sit
            f_sity=open('sity.txt','a',encoding='utf-8')
            if f_sity.writable():
                while num>0:
                    i=randint(0,len_sit)
                    print(i)
                    tem=sity[i]
                    sity.append(tem)
                    f_sity.write(sity[i])
                    num-=1
                f_sity.close()
                return sity
            else:
                 print('Error')
       else:
            return sity
  else:
      print('Error')
def dict_phon(sity,name,num,f_phon):
    # make new file for save   all information
    if f_phon.writable():
        for i in range(0,len(name)):
          f_phon.write(name[i]+num[i]+'\n'+sity[i])
        f_phon.close()
        
def user_input():
  count=0
  while count==0:
        print ('''Do you want to change or delete information?
               Answer : 0-change , 1 -delete , 2-find''')
        answer=input()
        if answer.isdigit():
              answer=int(answer)
              if answer==0 or answer==1 or answer==2:
                 break
              else:
               print('Error')   
        else:
            print('Error')
  return answer

def user_input_2(answer):
 if answer==0:
    # more informatiob about change
  while True:
    print('''Input  what do you want to change ?
        (Answer:0-Full name
                1- number
                2-sity
                3-sure name
                4-name
                5-all)''')                             
    answer_2=input()
    if answer_2.isdigit():
        answer_2=int(answer_2)
        if 0<=answer_2<6:
            break
        else:
            print('Error')
    else:
        print('Error')

 elif answer==1:
   while True:
    print('''Input  what do you want to delete ?
                         (Answer : 0-Full name
                                   1- number
                                   2-sity
                                  3-sure name
                                  4-name
                                  5-all)''')
    answer_2=input()
    if answer_2.isdigit():
        answer_2=int(answer_2)
        if 0<=answer_2<6:
             break
                        
        else:
             print('Error')
   else:
        print('Error') 
            
def user_input_3(answer,answer_2,):
  print('Input  your word:')
  answer_3=input()
  answer_3.capitalize()
  print(answer_3)
  return answer_3


def create_dict(f_phon):
  f_phon=open('phon.txt')
  book={}
  word=f_phon.readline()
  j=0
  while word:
     s=[]
     j=j+1
     for i in range(3):
         s+=[word]
         word=f_phon.readline()
     book[j]=s
  f_phon.close()
  return book

def delete(answer_2,answer_3,book):
    answe_3=str(answer_3)+'\n'
    if answer_2==0:
        for i in book:
            if book[i][0]==answer_3:
                book[i].pop(0)
    elif answer_2==1:
        for i in book:
            if book[i][1]==answer_3:
                book[i].pop(1)
    elif answer_2==2:
        for i in book:
            if book[i][2]==answer_3:
                book[i].pop(2)
    elif answer_2==3:
        for i in book:
            if book[i][0].startswith(answer_3):
                name=book[i].pop(0)
                name=name.split()
                name.pop(0)
                book[i][0]=name
    elif answer_2==4:
        for i in book:
            if book[i][0].endswith(answer_3):
                name=book[i].pop(0)
                name=name.split()
                name.pop(1)
                book[i][0]=name
    elif answer_2==5:
            for i in book:
                for j in book.values():
                  if book[i][j]==answer_3:
                      book.pop(i)
    print( book)
     
def change(answer_2,answer_3,book):
    answe_3=str(answer_3)+'\n'
    if answer_2==0:
        print('Input new contact:')
        for i in book:
            if book[i]==answer_3:
                print('Specify your option:')
                book[i][0]=input()
    elif answer_2==1:
        print('Input new contact:')
        for i in book:
            if book[i]==answer_3:
                print('Specify your option:')
                book[i][1]=input()
    elif answer_2==2:
        for i in book:
            print('Input new contact:')
            if book[i]==answer_3:
                print('Specify your option:')
                book[i][2]=input()
    elif answer_2==3:
        print('Input new contact:')
        for i in book:
            if book[i]==answer_3:
                name=book[i].pop(0)
                name=name.split()
                name.pop(0)
                word=input()
                name=word+' ' +name+'\n'
                book[i][0]=name
    elif answer_2==4:
        print('Input new contact:')
        for i in book:
            if book[i]==answer_3:
                name=book[i].pop(0)
                name=name.split()
                name.pop(1)
                word=input()
                name=name+' '+word+'\n'
                book[i][0]=name
                
    elif answer_2==5:
        print('Input new contact:')
        for i in book:
                for j in book.values():
                  if book[i]==answer_3:
                     book[i]=input()
    print(book)
     

def finid(answer_3,book):
   answer_3=str(answer_3)+'\n'
   for i in book:
         for j in book.values():
            if book[i][j]==answer_3:
                print(book[i])
                
def check(answer_3,book):
    answer_3=str(answer_3)+'\n'
    for i in book:
            if book[i].count(answer_3)>0:
                  return True
            
    return False
 
def new_contac_answer():
    while True:
        print('''You input wrong data.Do you want to add new contact?
              Answer: 0-Not,1-Yes''')
        answer_4=input()
        if answer_4.isdigit():
            answer_4=int(answer_4)
            if answer_4==0 or answer_4==1:
                 break
                            
            else:
                 print('Error')
        else:
            print('Error') 
    return answer_4        
    
def new_contac(answer,name,book):
    if answer==1:
        i=0
        while True:
            i+=1
            print('Input new contact:')
            cont=input().capitalize()+' ',input()+' ',input().capitalize()+'\n'
            book[len(name)+i]=cont
            print('Do you want add more?Answer not/yes')
            con=input()
            if con.lower()!='yes':
                break
        return book

    else:
        print('Error')
        
def new_file(f_phon,book):
    f_phon=open('phon.txt','w')
    if f_phon.writable():
      for i in book:  
         f_phon.writelines(book[i])
      f_phon.close()
    
  
f_name=open('names.txt')
f_sity=open('sity.txt',encoding='utf-8')
f_phon=open('phon.txt','w')
f_num=open('num.txt','w')
name=input_names(f_name)
count=len(name)
num=input_numper(f_num,count)
sity=sity(count,f_sity)
dict_phon(sity,name,num,f_phon)
answer=user_input()
answer_2=user_input_2(answer)
answer_3=user_input_3(answer,answer_2)
book={}
book=create_dict(f_phon)
if check(answer_3,book):
    if answer==0:
        change(answer_2,answer_3,book)
    elif answer==1:
        delete(answer_2,answer_3,book)
    else:
        finid(answer_3,book)
else:
    answer_4=new_contac_answer()
    book=new_contac(answer_4,name,book)
    new_file(f_phon,book)
for j in book:
    print(j,book[j])

    
    
