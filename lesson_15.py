# task 1
import re 
from functools import wraps

class Email:

    def __init__(self,email):

        self.email =  email
   
    def get_email (self):

        return self.email

    def validate (self):
      
        if len(self.email) > 6:
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            if(re.search(regex,self.email)):
                 pass
            else:
               self.email = 'False email'

    our_propert = property(validate,get_email) 
email_1=Email("ankitrai326@gmail.com")
email_2 = Email("my.ownsite@ourearth.org")
email_3=Email( "ankitrai326.com")
email_1.our_propert
email_2.our_propert
email_3.our_propert
print(email_1.email,email_2.email,email_3.email,sep='\n')

# task 2

class Boss:
    
    def __init__(self, id_, name, company,workers):

        self.id = id_
        self.name = name
        self.company = company
        self.workers = workers
    @property
    def get(self):
        return self.workers
    @get.getter
    def get(self):
        return self.workers

class Worker:

    def __init__(self, id_, name, company, boss):

        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss
    
    @property
    def new_boss(self):
    
        return self.boss

    @new_boss.setter
    def new_boss(self, value):

        self.boss = value

    
    
    @property
    def get(self):

        return self.name

    @get.getter
    def get(self):

        return self.name
boss_1 = Boss(145245245,'Alex','POP',['Stepan','Nick','Alan','Kate'])
boss_2 = Boss(156355445,'Bob','POP',['Ralf','Kate','Bill'])
empl_1 = Worker(145662556,'Kate','POP',boss_2)
emppl_2 = Worker(146535556,'Stepan','POP',boss_1)
if empl_1.name in  boss_1.workers:
   empl_1.boss=boss_1
print(empl_1.boss.name)

# task 3

class TypeDecorators:

    def to_int(func):
        @wraps(func)
        def change(string):
            if string.isdigit():
                string=int(string)
            return func(string)
        return change

    def to_bool(func):
        @wraps(func)
        def change(string):
            string=bool(string)
            return func(string)
        return change


@TypeDecorators.to_int
def do_nothing(string):
     return string
@TypeDecorators.to_bool
def do_something(string):

       return string

print(do_nothing('25') )
 # 25
print(do_something('True'))
 #is True