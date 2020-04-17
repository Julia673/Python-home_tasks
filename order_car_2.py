import csv
from random import randint
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


class Order:
    '''зразок замовлення'''
    def __init__(self,name,speed,distance_max,weight_min,weight_max,size_min,size_max, cost,price):
        self.name = name
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
                if(order[2]-self.price*order[4]>=self.cost):
                    return 1
                else: 
                    return 0
            else: 
                    return 0
        else: 
            return 0


    def order_profit(self,orders):
        '''визначаю чистий прибуток з кожного перевезення ''' 

        profit,damage,money=[],[],[0,0]
        for key in orders:
            for lis in orders[key]:
                print(lis)
                damage_lis=0
                if(len(lis)!=1 and len(lis)<9):
                    damage_lis=lis[5]*self.price
                    damage.append(damage_lis)
                    profit.append(lis[3]-damage_lis)
                elif(len(lis)>=9):
                    lis_2=lis[8]
                    damage_lis=lis[5]*self.price + lis_2[5]*self.price
                    damage.append(damage_lis)
                    profit.append(lis[3]+lis_2[3]-damage_lis)
        money[0]=list(set(profit))
        money[1]=list(set(damage))
        return money
               

    def get_same_direction(self,order):
        '''Визначення одного напрямку руху'''

        orders={'dir_1':[],'dir_2':[],'dir_3':[],'dir_4':[],'dir_5':[],'dir_6':[],'dir_7':[],'dir_8':[]}
        for indx in range(len(order)):
            if order[indx][7] ==1:
                orders['dir_1'].append(order[indx])
            if order[indx][7] ==2:
                orders['dir_2'].append(order[indx])
            if order[indx][7] ==3:
                orders['dir_3'].append(order[indx])
            if order[indx][7] ==4:
                orders['dir_4'].append(order[indx])
            if order[indx][7] ==5:
                orders['dir_5'].append(order[indx])
            if order[indx][7] ==6:
                orders['dir_6'].append(order[indx])
            if order[indx][7] ==7:
                orders['dir_7'].append(order[indx])
            if order[indx][7] ==8:
                orders['dir_8'].append(order[indx])
        return orders


    def sort_order_add(self,orders):
        '''Визначення одного напрямку руху'''

        for key in orders:
            if (len(orders[key])>1):
              size,way,day,weight,ind=[],[],[],[],[]
              for indx in range(len(orders[key])):
                  size.append(orders[key][indx][2])
                  way.append(orders[key][indx][5])
                  day.append(orders[key][indx][6])
                  weight.append(orders[key][indx][4])
              max_way=0
              min_way=min(way)
              while (min_way!=max_way):
                ind_1,ind_2=[],[]
                max_way=max(way)
                index=way.index(max_way)
                way.pop(index)
                if ((day[index]-1)*self.distance_max>max_way):
                    for indx in range(len(size)): 
                        if (ind.count(indx)== 0):
                            count=size[index] +size[indx]
                            if (count<=(self._size_max-1)):
                               ind_1.append(indx)
                            else:
                                count=0
                    if(len(ind_1)>=1):
                       for  indx in ind_1:
                            count=weight[indx]+weight[index]
                            if (count<=(self._weight_max-10)):
                                 ind_2.append(indx)
                            else:
                                  count=0
                    
                    if(len(ind_2)>=1 ):
                            lis= orders[key]
                            lis[index].append(0) 
                            lis[index][8]=lis[ind_2[0]]
                            orders[key]=lis
                            ind.append(ind_2[0])  
                else:
                    continue
              if(len(ind)>=1):
                  for i in ind:
                    orders[key][i]=[0] 
        return orders
                
class Order_Car(Order):
    '''легкові автомобілі'''
    def __init__(self,name,speed=100,distance_max=600,weight_min=50,weight_max=400,size_min=1,size_max=10, cost=500,price=2):
        super().__init__(name,speed,distance_max,weight_min,weight_max,size_min,size_max, cost,price)

class Order_Semitrailers(Order):
    '''напівгрузові автомобілі'''
    def __init__(self,name,speed=90,distance_max=500,weight_min=400,weight_max=1000,size_min=10,size_max=59, cost=1000,price=5 ,profit=7):
        super().__init__(name,speed,distance_max,weight_min,weight_max,size_min,size_max, cost,price)

class Order_Truck(Order):
    '''грузові автомобілі'''
    def __init__(self,name,speed=80,distance_max=400,weight_min=1000,weight_max=9000,size_min=60,size_max=180, cost=4000,price=7 ,profit=9):
       super().__init__(name,speed,distance_max,weight_min,weight_max,size_min,size_max, cost,price)


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
    
def order_money(file,car):
    '''прибуток і затрати '''
    
    order_all=[]
    for order in file:
        order=order.split()
        order_2=[]
        for ind in order:
            order_2.append(int(ind))
        order_all.insert(len(order_all),order_2)
    orders=car.get_same_direction(order_all)
    orders_change=car.sort_order_add(orders)
    money_order=car.order_profit(orders_change)
    money_order.append(0)
    money_order[2]=orders_change
    return money_order

count=0
with open('Data_order.csv', 'w', newline='') as csvfile:
    while count<=10000:
        count=count+1
        size= randint(1,200)

        price= randint(100,6000)
        weight= randint(1,10000)
        distance= randint(10,500)  
        days= randint(1,10)  
        direction= randint(1,9)  
        order=[count,size,price,weight,distance,days,direction]
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
    with open('Car_Order.csv', 'w', newline='') as file_1:
        with open('Semitrailers_Order.csv', 'w', newline='') as file_2:
             with open('Truck_Order.csv', 'w', newline='') as file_3:
                for order in csvfile:
                    order=order.split()
                    order_2=[]
                    for i in order:
                        order_2.append(int(i))
                    if (car_1.order_good(order_2)):
                            car = csv.writer(file_1, delimiter=' ',
                                                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            count_1=count_1+1
                            order_2.insert(0, count_1)                     
                            car.writerow(order_2)

                    elif (car_2.order_good(order_2)):
                            car = csv.writer(file_2, delimiter=' ',
                                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            count_2=count_2+1
                            order_2.insert(0, count_2)                             
                            car.writerow(order_2)
                    elif (car_3.order_good(order_2)):
                            car = csv.writer(file_3, delimiter=' ',
                                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            count_3=count_3+1
                            order_2.insert(0, count_3)                                   
                            car.writerow(order_2)
                    else:
                            count_4=count_4+1

csvfile.close()
file_1.close()
file_2.close()
file_3.close()

with open('Car_Order.csv', 'r', newline='') as file_1:
           car_1=Order_Car('Day_1')
           money_1=order_money(file_1,car_1)
with open('Semitrailers_Order.csv', 'r', newline='') as file_2:
            car_2=Order_Semitrailers('Day_1')
            money_2=order_money(file_2,car_2)
with open('Truck_Order.csv', 'r', newline='') as file_3:
            car_3=Order_Truck('Day_1')
            money_3=order_money(file_3,car_3)
print(money_1)
csvfile.close()
file_1.close()
file_2.close()
file_3.close()
profit,damage=[0,0,0],[0,0,0]
name=['Car','Semitrailers','Truck']
colors=['Blue','Red']
a=Graph()
b=Graph()
profit[0]=sum(money_1[0])
profit[1]=sum(money_2[0])
profit[2]=sum(money_3[0])
damage[0]=sum(money_1[1])
damage[1]=sum(money_2[1])
damage[2]=sum(money_3[1])
a.histogram_two(name, profit,damage)
b.diagrama(name,profit)
names=['Profit','Damage']
data=[sum(profit),sum(damage)]
text ='The ratio of profit to the order and the cost of its delivery'
b.diagrama(names,data,text)

b.graph_points(money_1[0],money_2[0],money_3[0])
plt.show()

