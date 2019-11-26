import pandas as pd
cars = pd.read_csv('cars.csv')
a = cars.loc[[0,1,2,3,4], ::2]
b = cars[cars['Model']=='Mazda RX4']
c = cars.loc[cars['Model']=='Camaro Z28', 'cyl']
d = cars.loc[(cars['Model']=='Mazda RX4 Wag'), ('Model', 'cyl', 'gear')]
e = cars.loc[(cars['Model']=='Honda Civic'), ('Model', 'cyl', 'gear')]
f = cars.loc[(cars['Model']=='Ford Pantera L'), ('Model', 'cyl', 'gear')]
print(a)
print(b)
print('Cylinders of Camaro Z28: ', c)
print('Cylinders and Gears: ')
print(pd.concat([d,e,f]))
