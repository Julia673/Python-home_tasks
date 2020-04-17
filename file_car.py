import csv
from random import randint
import matplotlib as mpl
import matplotlib.pyplot as plt
i=0
with open('Data.csv', 'w', newline='') as csvfile:
    while i<1000:
        i+=1
        number=[randint(60, 131) for i in range(2)]
        num=[i]
        nums =[randint(1,8)]
        number=num+nums+number
        writer = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(number)
coutn_1=0
coutn_2=0
coutn_3=0
coutn_4=0
Car=[]
Bike=[]
Bus=[]
Truck=[]
with open('Data.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    with open('Car.csv', 'w', newline='') as file:
        with open('Bike.csv', 'w', newline='') as file_2:
            with open('Bus.csv', 'w', newline='') as file_3:
                 with open('Truck.csv', 'w', newline='') as file_4:
                    for row in reader:
                            row=row[0].split()
                            lis=[]
                            for i in row:
                                i=int(i)
                                lis.append(i)
                                
                            if lis[1]==4 and 60<=lis[2]<=130 and 80<=lis[3]<=130:
                                    car = csv.writer(file, delimiter=' ',
                                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                                    car.writerow(row)
                                    coutn_1+=1
                            elif 2<=lis[1]<4 and 80<=lis[2]<=130 and 90<=lis[3]<=130:
                                    bike = csv.writer(file_2, delimiter=' ',
                                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                                    bike.writerow(row)
                                    coutn_2+=1
                            elif lis[1]==4 and 70<=lis[2]<=110 and 70<=lis[3]<=110:
                                    bus = csv.writer(file_3, delimiter=' ',
                                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                                    bus.writerow(row)
                                    coutn_3+=1
                            elif 4<=lis[1]<9 and 90<=lis[2]<=130 and 100<=lis[3]<=130:
                                    truck = csv.writer(file_4, delimiter=' ',
                                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                                    truck.writerow(row)
                                    coutn_4+=1
result={'Car':coutn_1,'Bike':coutn_2,'Bus':coutn_3,'Truck':coutn_4}
Car.append(coutn_1)
Bike.append(coutn_2)
Bus.append(coutn_3)
Truck.append(coutn_4)
coutn_1=0
coutn_2=0
coutn_3=0
with open('Car.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    with open('Pick_ups.csv', 'w', newline='') as file:
        with open('Sport_cars.csv', 'w', newline='') as file_2:
            with open('Estate_cars', 'w', newline='') as file_3:
                    for row in reader:
                            row=row[0].split()
                            lis=[]
                            for i in row:
                                i=int(i)
                                lis.append(i)
                                
                            if lis[1]==4 and 80<=lis[2]<=100 and 80<=lis[3]<=100:
                                    pick = csv.writer(file, delimiter=' ',
                                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                                    pick.writerow(row)
                                    coutn_1+=1
                            elif lis[1]==4 and 100<=lis[2]<=130 and 90<=lis[3]<=130:
                                    sport = csv.writer(file_2, delimiter=' ',
                                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                                    sport.writerow(row)
                                    coutn_2+=1
                            elif lis[1]==4 and 60<=lis[2]<=100 and 70<=lis[3]<=90:
                                    car = csv.writer(file_3, delimiter=' ',
                                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                                    car.writerow(row)
                                    coutn_3+=1
result['Pick_ups']=coutn_1 
result['Sport_cars']=coutn_2
result['Estate_cars']=coutn_3
Car.append(coutn_1)
Car.append(coutn_2)
Car.append(coutn_3)
Car_name=['Other cars','Pick_ups','Sport_cars','Estate_cars']
Car[0]=Car[0]-Car[1]-Car[2]-Car[3]
coutn_1=0
coutn_2=0
with open('Bike.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    with open('Pedal_bikes.csv', 'w', newline='') as file:
        with open('Motor_bikes.csv', 'w', newline='') as file_2:
            for row in reader:
                row=row[0].split()
                lis=[]
                for i in row:
                   i=int(i)
                   lis.append(i)
                                
                if lis[1]==3 and 60<=lis[2]<=130 and 70<=lis[3]<=110:
                        pick = csv.writer(file, delimiter=' ',
                                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
                        pick.writerow(row)
                        coutn_1+=1
                elif lis[1]==2 and 80<=lis[2]<=130 and 80<=lis[3]<=130:
                        sport = csv.writer(file_2, delimiter=' ',
                                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
                        sport.writerow(row)
                        coutn_2+=1
result['Pedal_bikes']=coutn_1
result['Motor_bikes']=coutn_2
Bike.append(coutn_1)
Bike.append(coutn_2)
Bike_name=['Other Bike','Pedal_bikes','Motor_bikes']
Bike[0]=Bike[0]-Bike[1]-Bike[2]
coutn_1=0
coutn_2=0
with open('Truck.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    with open('Medium_tracs.csv', 'w', newline='') as file:
        with open('Heavy_tracs.csv', 'w', newline='') as file_2:
            for row in reader:
                row=row[0].split()
                lis=[]
                for i in row:
                    i=int(i)
                    lis.append(i)
                                
                if lis[1]==6 and 60<=lis[2]<=120 and 70<=lis[3]<=110:
                        pick = csv.writer(file, delimiter=' ',
                                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
                        pick.writerow(row)
                        coutn_1+=1
                elif lis[1]==8 and 80<=lis[2]<=120 and 80<=lis[3]<=120:
                        sport = csv.writer(file_2, delimiter=' ',
                                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
                        sport.writerow(row)
                        coutn_2+=1
result['Medium_tracs']=coutn_1
result['Heavy_tracs']=coutn_2
Truck.append(coutn_1)
Truck.append(coutn_2)
Truck_name=['Other Truck','Medium_tracs','Heavy_tracs']
Truck[0]=Truck[0]-Truck[1]-Truck[2]
for key in result:
        print(key,'-',result[key])

data_names = []
data_values = []
for key in result:
        data_names.append(key)
        data_values.append(result[key])
print(data_names)
print(data_values)
s=data_values[0]+data_values[1]+data_values[2]+data_values[3]
data_names.append('Wrong data')
data_values.append(s)
dpi = 80
fig = plt.figure(dpi = dpi, figsize = (412 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 9})

plt.title('Transport data (%)')

xs = range(len(data_names))

plt.pie(
    data_values, autopct='%.1f', radius = 1.1,
    explode = [0.15] + [0 for _ in range(len(data_names) - 1)] )
plt.legend(
    bbox_to_anchor = (-0.16, 0.45, 0.25, 0.25),
    loc = 'lower left', labels = data_names )
fig.savefig('pie.png')      
#plt.show()               
# chart Car

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (412 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 9})

plt.title('Car data (%)')

xs = range(len(Car_name))

plt.pie(
    Car, autopct='%.1f', radius = 1.1,
    explode = [0.15] + [0 for _ in range(len(Car_name)-1)] )
plt.legend(
    bbox_to_anchor = (-0.16, 0.45, 0.25, 0.25),
    loc = 'lower left', labels = Car_name)
fig.savefig('pie.png')      
#plt.show()   
# chart CBike

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (412 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 9})

plt.title('Bike data (%)')

xs = range(len(Bike_name))

plt.pie(
    Bike, autopct='%.1f', radius = 1.1,
    explode = [0.15] + [0 for _ in range(len(Bike_name)-1)] )
plt.legend(
    bbox_to_anchor = (-0.16, 0.45, 0.25, 0.25),
    loc = 'lower left', labels = Bike_name)
fig.savefig('pie.png')      
#plt.show()  
# char Truck                      
dpi = 80
fig = plt.figure(dpi = dpi, figsize = (412 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 9})

plt.title('Truck  data (%)')

xs = range(len(Truck_name))

plt.pie(
    Truck, autopct='%.1f', radius = 1.1,
    explode = [0.15] + [0 for _ in range(len(Truck_name)-1)] )
plt.legend(
    bbox_to_anchor = (-0.16, 0.45, 0.25, 0.25),
    loc = 'lower left', labels = Truck_name)
fig.savefig('pie.png')      
plt.show()                        