#task 1
class Person ():
    
    def __init__(self,first_name,second_name,age):
        self.first_name=first_name
        self.second_name=second_name
        self.age=age
    
    def health(self):
        self.health=input("Input health ")
    
    def get(self):
         return( self.first_name +self.second_name+self.age )


class Pupil(Person):

     def __init__(self,first_name,second_name,age,rating):
         super(). __init__(first_name,second_name,age)
         self.rating= rating

     def chang_rat(self):
        while 1:
          new=input("Input new rating")
          if new.isdigit:
             self.rating=int(new)
             return self.rating

     def hom_task(self):
        self.task=input("Home tasks: ")
        print(self.first_name+' '+self.second_name +' Your task is : '+self.task)
     
     def get_2(self):
        print( super().get, self.rating ,self.task )

class Teacher(Person):

     def __init__(self,first_name,second_name,age,rating,salary):
         super(). __init__(first_name,second_name,age)
         self.salary= salary

     def premium(self):
         while 1:
             new=input("Input premium:")
             if new.isdigit():
              self.salary=self.salary+int(new)
              break

     def get_3(self):
         return( super().get+ self.salary)
        

Alisa=Pupil('Alisa','Gart',13,7)
Alisa.health()
Alisa.hom_task()
Alisa.get_2()

#task 2 

class Mathematician():
    
    def square_nums(self,num):
        arr=[]
        for i in num:
          i=i*i
          arr.append(i)
        print(arr)
        return arr

    def remove_positives(self,num):
        arr=[]
        for i in num:
          if i <0:
              arr.append(i)
        print(arr)
        return arr

    def filter_leaps(self,num):
        arr=[]
        for i in  num:
          if i%4==0 or i%400==0:
              arr.append(i)
        print(arr)
        return arr

m = Mathematician()
m.square_nums([7, 11, 5, 4])
 # [49, 121, 25, 16]
m.remove_positives([26, -11, -8, 13, -90])
#  [-11, -8, -90]
m.filter_leaps([2001, 1884, 1995, 2003, 2020])
# [1884, 2020]

# task 3

class Product:
   
   def __init__(self,type,name,price,number=0,profit=0):

       self.type=type
       self.name=name
       self.price=price
       self.number=number
       self.profit=profit
       self.obj_store=ProductStore()



class ProductStore:

    def add(self,product,num):
        '''додає кількість продукції '''
        product.number=product.number+num

    def get_product_info_all(self):
        '''інформація про всі доступні продукти  '''
        print(vars(Product))



    def set_discount(self,discount):
        ''' додає знижку '''
        self.price=self.price * (100-discount)


    def sell_product (self,name,sell):
        '''вилучає кількість продукції '''
        name.number= name.number-sell
        name.profit=sell * name.price

    def get_income(self):
        ''' сума прибутку  '''
        return  self.profit

    def get_product_info(self,name):
        ''' повертає інформацію про продукт у вигляді кортежу '''
        print(name.name,name.number)
        

p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore ()

s.add (p, 10)

s.add (p2, 300)

s.sell_product (p2, 10)

s.get_product_info (p2) # ('Ramen', 290)
    
#task 4
with open('logs.txt', 'w', newline='') as file:
        file.write("Error type:")
class CustomException(Exception):
    
    def __init__(self, text):
        self.txt = text
 
    
a = input("Input your login : ")
 
try:
    a = int(a)
    #12345
    if a!=12345:
        raise CustomException("Wrong login\n")
    
except ValueError:
 with open('logs.txt', 'a', newline='') as file:
        file.write("Error type of value!\n")
except CustomException as mr:
     with open('logs.txt', 'a', newline='') as file:
        file.write("Wrong login\n")
else:
    print('Hi you are wellcome')