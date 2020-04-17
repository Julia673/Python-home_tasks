# Home task

import json

class Goods():
 """ Створення класу товару для складу магазину"""

 

def __init__(self,name,number,cod,order):
    self.name = name
    self.number = number
    self.cod = cod
    self.order=order



f=open("shop.json","w")
count = 1
i=1
while count > 0:
    while True:
      a = input("Input how many goods do you want to safe? ")
      if a.isdigit():
         print(a)
         count = int(a)
         break
      else:
          continue
    name = input("Input name goods: ").capitalize
    number = input("Input number goods: ")
    while True:
       number = input("Input number goods: ")
      if number.isdigit():
        number = int(number)
        break
    cod = input("Input cod goods ")
    order = 0
    Goods(name,number,cod,order)
    
        



    
  