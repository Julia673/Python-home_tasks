#Home task 
# task 1

from fractions import Fraction

class Animal:

    def __init__(self,name):
         self.name = name

    # aбстракний метод

    def talk(self):
        raise NotImplementedError("Must be implemented by sub class")

class Cat(Animal):
    def talk(self):
        print(self.name+" meow !!")

class Dog(Animal):
    def talk(self):
        print(self.name+" woof woof !!")

Animals=[Cat('Barsik'),Dog('Reks')]
for animal in Animals:
    animal.talk()

#task 2

class Library:

    def __init__(self,name, books, authors):


        self.name = name
        self.books = books
        self.authors = authors
    
    def __str__(self):

        return f'{self.name},{self.books},{self.authors}'
    
    def __repr__(self):
    
        return self.__str__

    def new_book (name,year,author):

        new_book = Book(name,year,author)
        print(new_book)
        return new_book

    def  group_by_author(self,Author,Author_list):
     
      book = list(filter(lambda x: x['name'] == Author, Author_list))
      print(book)
      return book


    def group_by_year(self,year,books_list):

       book = list(filter(lambda x: x['year'] == year, books_list))
       print(book)
       return book
    
        
class Book:

    def __init__(self,name, year, obj_author):

        self.nam = name
        self.year = year
        self.obj_author = obj_author

    def __str__(self):
        
         return f'{self.name},{self.year},{self.obj_author}'
    
    def __repr__(self):
    
         return self.__str__


class Author:

    def __init__(self,name,country, birthday, books ):
        self.name=name
        self.country=country
        self.birthday=birthday
        self.books=books

    def __str__(self):
        
         return f'{self.name},{self.country},{self.birthday},{self.books}'
    
    def __repr__(self):
    
         return self.__str__
    
lib_1=Library('Karga',['Stop','Cool','Red'],['Gard','Lubcko','Karl'])
author_1=Author('Grand','England',1985,['Cool','Boom','Soon'])
author_2=Author('Karl','England',1975,['Red','Black','Green'])
author_3=Author('Lubcko','England',1965,['Stop','Run','Live'])
book_1=Book('Red',1995,author_1)
book_2=Book('Black',1998,author_1)
book_3=Book('Green',2000,author_1)
book_4=Book('Cool',1996,author_2)
book_5=Book('Boom',1998,author_2)
book_6=Book('Soon',2003,author_2)
book_7=Book('Stop',1991,author_3)
book_8=Book('red',2000,author_3)
book_9=Book('red',2009,author_3)
book_list=[book_1,book_2,book_3,book_4,book_5,book_6,book_7,book_8,book_9]
author_list=[author_1,author_2,author_3]

list_1 = lib_1.group_by_author('Karl',author_list)
list_2 = lib_1.group_by_year(2000,book_list)

#task 3
class Fractions :

    try:

        def __init__(self,number):

          self.number =  Fraction( number)

    except (ZeroDivisionError , Exception) as e:
      print(e)

    def add(number_1,number_2):

       num= number_1.number + number_2.number
       return num
   
    def subtraction(number_1,number_2):

      num= number_1.number - number_2.number
      return num

    try:

       def  division(number_1,number_2):

        num= number_1.number / number_2.number
        return num

    except (ZeroDivisionError , Exception) as e:
      print(e)

    def multiplication(number_1,number_2):

        num= number_1.number / number_2.number
        return num
     
a = Fractions(1/2)
b = Fractions(1/4)
num=add(a,b)
print(num)
     


