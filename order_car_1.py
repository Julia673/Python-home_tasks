import csv
from random import randint
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


class Order:
    '''зразок замовлення'''
    def __init__(self,count_car,speed,distance_max,weight_min,weight_max,size_min,size_max, cost,price):
        self.count_car = count_car
        self.speed = speed
        self.distance_max = distance_max
        self.weight_min=weight_min
        self._weight_max=weight_max
        self.size_min=size_min
        self._size_max=size_max
        self.cost=cost
        self.price=price
        

    def order_good(self,order):
        '''перевірка на можливість виконати замовлення'''
        
        if(self.size_min<=order[1]<=self._size_max and order[2]>=self.cost and self.weight_min<=order[3]<=self._weight_max ):
            if(self.distance_max*order[5]>=order[4]):
                return 1
            else: 
                return 0
        else: 
            return 0


    def order_profit(self,order):
        '''визначаю чистий прибуток з кожного перевезення ''' 
        
        money=[]
        costs=self.price*order[4]
        profit=order[2]-costs
        #time=round(order[4]/self.speed,2)
        money.append(profit)
        money.append(costs)
        #order.append(time)
        return money


    def enough_car(self,number):
        '''чи достатньо машин для виконання всіх замовлень'''
        if(self.count_car>=number):
           return  1
        else:
            return 0


    def car_have(self):
        '''сортую замовлення ''' 

        return self.count_car


    def sort_order_add(self,orders):
        '''Визначення одного напрямку руху'''
        for key in orders:
            if (len(orders[key])>1):
                size,way,day,weight,ind_1,ind_2=[],[],[],[],[],[]
                for indx in range(len(orders[key])):
                    size.append(orders[key][indx][2])
                    way.append(orders[key][indx][5])
                    day.append(orders[key][indx][6])
                    weight.append(orders[key][indx][4])
                count=0
                count_2=0
                max_way=max(way)
                index=way.index(max_way)
                if ((day[index]-1)*self.distance_max>max_way):
                    count_2=1
                if ((day[index]-2)*self.distance_max>max_way):
                    count_2=2
                if ((day[index]-3)*self.distance_max>max_way):
                    count_2=3
                for indx in range(len(size)): 
                    if (indx!=index):
                       count=size[index] +size[indx]
                    if (count<=(self._size_max-1)):
                       ind_1.append(indx)
                if(len(ind_1)>1):
                    count=0
                    for  indx in ind_1:
                        count=weight[indx]+weight[index]
                        if (count<=(self._weight_max-10)):
                            ind_2.append(indx)
                if(len(ind_2)<=count_2 and count_2!=0 and len(ind_2)!=0):
                    for ind in ind_2:
                        new = orders[key].pop(ind)
                        orders[key][index].append(0)
                        orders[key][index][orders[key][index].index(0)]=new
                else:
                    for ind in ind_2:
                       if(ind<=count_2):
                           new = orders[key].pop(ind)
                           orders[key][index].append(0)
                           orders[key][index][orders[key][index].index(0)]=new
        return orders
    

   
class Order_Car(Order):
    '''легкові автомобілі'''
    def __init__(self,count_car,speed=100,distance_max=600,weight_min=50,weight_max=400,size_min=1,size_max=10, cost=500,price=2):
        super().__init__(count_car,speed,distance_max,weight_min,weight_max,size_min,size_max, cost,price)

class Order_Semitrailers(Order):
    '''напівгрузові автомобілі'''
    def __init__(self,count_car,speed=90,distance_max=500,weight_min=400,weight_max=1000,size_min=10,size_max=59, cost=1000,price=5 ,profit=7):
        super().__init__(count_car,speed,distance_max,weight_min,weight_max,size_min,size_max, cost,price)

class Order_Truck(Order):
    '''грузові автомобілі'''
    def __init__(self,count_car,speed=80,distance_max=400,weight_min=1000,weight_max=9000,size_min=60,size_max=180, cost=4000,price=7 ,profit=9):
       super().__init__(count_car,speed,distance_max,weight_min,weight_max,size_min,size_max, cost,price)
        

class Graph:
    '''клас для графіка '''
    def histogram_two(self,name,profit,damage,text='Analyze profit and damage received in a day.',label_1='Profit',label_2='Damage'):
        '''Побудова графіка  двохвимірну гістограма'''

        width = 0.3
        x = np.arange(len(name))
        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, profit, width,label=label_1 )
        rects2 = ax.bar(x + width/2, damage, width,label=label_2 )
        ax.set_title(text)
        ax.set_xticks(x)
        ax.set_xticklabels(name)
        ax.legend()


    def graph_points(self,good_order_1,good_order_2,good_order_3,text='Profit for each order '):
        '''розсіюваюваний  графік у вигляді точок'''

        fig, ax = plt.subplots()
        x1 = [range( len(good_order_1))]
        y1 = good_order_1
        x2 = [range( len(good_order_2))]
        y2 = good_order_2
        x3 = [range( len(good_order_3))]
        y3 =good_order_3
        #  Дані в вигляді точок:
        ax.scatter(x1, y1,label='Car')
        ax.scatter(x2, y2,label='Semitrailers')
        ax.scatter(x3, y3,label='Truck')
        ax.set(title=text)

        

    def diagrama(self,data_names,data_values,text='Analysis of profit data for each mode of transport (%)'):
        '''Побудова графіка діаграма'''

        dpi = 80
        fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
        mpl.rcParams.update({'font.size': 9})
        plt.title(text)
        xs = range(len(data_names))
        plt.pie(
            data_values, autopct='%.1f', radius = 1.1,
            explode = [0.15] + [0 for _ in range(len(data_names) - 1)] )
        plt.legend(
            bbox_to_anchor = (-0.16, 0.45, 0.25, 0.25),
            loc = 'lower left', labels = data_names )
        fig.savefig('pie.png')
    

    def histogram(self,number,name=['Car', 'Semitrailers', 'Truck'],color=['r','b','g']):
        '''Проста гістограма'''

        fig, ax = plt.subplots()
        ax.bar(name, number,color=color,label=number )
        fig.set_figwidth(10)    #  ширина и
        fig.set_figheight(4)    #  высота "Figure"
        fig.set_facecolor('floralwhite')
        ax.set_facecolor('seashell')
        ax.set_xlabel('$Name$')
        ax.set_ylabel('$Number$')
        ax.set_title('Correlation of the number of transports')
    

def damage_car(profit,costs,number):
    '''збитки компанії через нехватку автомобілів'''

    damege,prof,money,cost=[],[],[],[]
    for indx in  range(len(profit)):
        if(indx<=number):
             prof.append(profit[indx]) 
             cost.append(costs[indx])
        else:
             damege.append(profit[indx])
    money.append(sum(prof))
    money.append(sum(damege))
    money.append(sum(cost))
    print(money)
    return money 

def  sort_order_profit(order,number):
    '''При нехватці  транспорту для замовлень , кількість замовлень що можуть опрацюватися'''
    good_order=[]
    for indx in  range(number):
        good_order.append(order[indx]) 
    return good_order 


count=1
with open('Data_order.csv', 'w', newline='') as csvfile:
    while count<=10000:
        count=count+1
        size= randint(1,200)
        price= randint(100,5000)
        weight= randint(1,10000)
        distance= randint(10,500)  
        days= randint(1,10)  
        order=[count,size,price,weight,distance,days]
        writer = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(order)
profit_1,profit_2,profit_3=[],[],[]
costs_1,costs_2,costs_3=[],[],[]
car_1=Order_Car(10)
car_2=Order_Semitrailers(100)
car_3=Order_Truck(600)
count_1,count_2,count_3,count_4=0,0,0,0
with open('Data_order.csv', 'r', newline='') as csvfile:
    with open('Car_order.csv', 'w', newline='') as file_1:
        with open('Semitrailers_order.csv', 'w', newline='') as file_2:
             with open('Truck_order.csv', 'w', newline='') as file_3:
                for order in csvfile:
                    order=order.split()
                    order_2=[]
                    for i in order:
                        order_2.append(int(i))
                    if (car_1.order_good(order_2)):
                            car = csv.writer(file_1, delimiter=' ',
                                                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            count_1=count_1+1
                            money_order=car_1.order_profit(order_2)
                            costs_1.append(money_order[1])
                            profit_1.append(money_order[0])                        
                            car.writerow(order_2)

                    elif (car_2.order_good(order_2)):
                            car = csv.writer(file_2, delimiter=' ',
                                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            count_2=count_2+1
                            money_order=car_2.order_profit(order_2)
                            costs_2.append(money_order[1])
                            profit_2.append(money_order[0])                               
                            car.writerow(order_2)
                    elif (car_3.order_good(order_2)):
                            car = csv.writer(file_3, delimiter=' ',
                                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            count_3=count_3+1
                            money_order=car_3.order_profit(order_2)
                            costs_3.append(money_order[1])
                            profit_3.append(money_order[0])                                    
                            car.writerow(order_2)
                    else:
                            count_4=count_4+1
damage,profit,number_order_ex,number_orde_full,numbers,costs=[],[],[],[],[],[]
if(car_1.enough_car(count_1)):
    number_order_ex.append(count_1)
    number_orde_full.append(0)
    damage.append(0)
    profit.append(sum(profit_1))
    costs.append(sum(costs_1))
    numbers.append(count_1)
    print("Success for car the %d are accepted. Profit is %d. "%(count_1,sum(profit_1)))
else:
    number=car_1.car_have()
    money=damage_car(profit_1,costs_1,number)
    damage.append(money[1])
    profit.append(money[0])
    costs.append(money[2])
    number_order_ex.append(number)
    number_orde_full.append(count_1-number)
    numbers.append(number)
    print("Success for car the %d are accepted. Profit is %d. "%(number,money[0]))
    print("Need more car! The %d can not accept.Damage is %d."%(count_1-number,money[1]))
if(car_2.enough_car(count_2)):
    number_order_ex.append(count_2)
    number_orde_full.append(0)
    damage.append(0)
    profit.append(sum(profit_2))
    costs.append(sum(costs_2))
    numbers.append(count_2)
    print("Success for Semitrailers the %d are accepted.Profit is %d."%(count_2,sum(profit_2)))
else:
    number=car_2.car_have()
    money=damage_car(profit_2,costs_2,number)
    damage.append(money[1])
    profit.append(money[0])
    costs.append(money[2])
    number_order_ex.append(number)
    number_orde_full.append(count_2-number)
    numbers.append(number)
    print("Success for Semitrailers. The %d are accepted.Profit is %d."%(number,money[0]))
    print("Need more Semitrailers. The %d can not accept.Damage is %d. "%(count_2-number,money[1]))

if(car_3.enough_car(count_3)):
    number_order_ex.append(count_1)
    number_orde_full.append(0)
    damage.append(0)
    profit.append(sum(profit_3))
    costs.append(sum(costs_3))
    numbers.append(count_3)
    print("Success for truck the %d are accepted. Profit is %d. "%(count_3,sum(profit_3)))
else:
    number=car_3.car_have()
    money=damage_car(profit_3,costs_3,number)
    damage.append(money[1])
    profit.append(money[0])
    costs.append(money[2])
    number_order_ex.append(number)
    number_orde_full.append(count_3-number)
    numbers.append(number)
    print("Success for truck. The  %d are accepted. Profit is %d. "%(number,money[0]))
    print("Need more truckthe.The %d can not accept.Damage is %d. "%(count_3-number,money[1]))
print("Order that the company cannot fulfill or erroneous requests %d"%(count_4))
print("The total profit is %d."%(sum(profit)))
print("The total damage is %d."%(sum(damage)))
name=['Car','Semitrailers','Truck']
colors=['Blue','Red']
a=Graph()
b=Graph()
print(damage,profit)
a.histogram_two(name, profit,damage)
#stackedbarplot(name,  number_ordr_ex,number_orde_full)
good_order_1=sort_order_profit(profit_1,number_order_ex[0])
good_order_2=sort_order_profit(profit_2,number_order_ex[1])
good_order_3=sort_order_profit(profit_3,number_order_ex[2])
b.diagrama(name,profit)
b.graph_points(good_order_1,good_order_2,good_order_3)
names=['Profit','Damage']
data=[sum(profit),sum(damage)]
text='Correlation of profit and damage due to lack of transport'
b.diagrama(names,data,text)
a.histogram(numbers)
text ='The ratio of profit to the order and the cost of its delivery'
a.histogram_two(name, profit,costs,text,'Profit','Costs')
plt.show()