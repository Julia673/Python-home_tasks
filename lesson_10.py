# Class Home
# task 1

class Person ():
    
    def __init__(self,first_name,second_name,age):
        self.first_name=first_name
        self.second_name=second_name
        self.age=age

    def talk(self):
            print('Hello, my name is '+ self.first_name+self.second_name+' and I’m '
                  +self.age+' years old')
    
pers=Person(input("Input first name "),input("Input second name "),input("Input age "))
pers.talk()
#task 2
class Dog():

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def humen_age(self):
        self.humen_age=int(self.age)*7
        print(self.humen_age)
while True: 
    name=input("Input dog name ")
    age=input("Input age ")
    if age.isdigit:
        age=int(age)
        break
    else: 
        age = 0 
dog_1=Dog(name,age)

dog_1.humen_age
#task 3

 
class TVController():
    CHANNELS = ["BBC", "Discovery", "TV1000"]
    now=0
    def first_channel(self):
        TVController.now=0
        print (TVController.CHANNELS[0]) 

    def last_channel(self):
        TVController.now=2
        print (TVController.CHANNELS[2])
     
    def  turn_channel(self,a):
        if a<=3:
           TVController.now=a
           print(TVController.CHANNELS[a])
        else:
            print("Error")
    
    def next_channel(self):
        TVController.now+=1
        print(TVController.CHANNELS[TVController.now])

    def previous_channel(self):
        TVController.now-=1
        print(TVController.CHANNELS[TVController.now])
    
    def current_channel(self):
        print(TVController.CHANNELS[TVController.now])

   
    def is_exist(self,a):
        
        if type (a)==int:
           if int(a)<=3 :
            print("Yes")
           else:
            print("No")
        else:
            count=0
            for channel in TVController.CHANNELS:
                if a ==channel  :
                    count=1
            if count==1:
                print("Yes")
            else:
                print("No")

 
controller=TVController()
controller.first_channel() # "BBC"

controller.last_channel()   #"TV1000"

controller.turn_channel(1)   # "BBC"

controller.next_channel()   #"Discovery"

controller.previous_channel()  # "BBC"

controller.current_channel()   #"BBC"
controller.is_exist(4)     #"No"

controller.is_exist("BBC")  #"Yes"


