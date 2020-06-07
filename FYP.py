import itertools as it
import math
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt


def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def convertion(a1,b1,Data):
    x_list = []
    y_list = []
    points = Origin.values
    for p in range (0, len(points)):
        a = (-a1)+ points[p-1][0]
        b = (-b1)+ points[p-1][1]
        x_list.append(a)
        y_list.append(b)

    c_list = {'X_coordinate':x_list,'Y_coordinate':y_list}

    df = pd.DataFrame(c_list, columns=['X_coordinate', 'Y_coordinate'])
    export_csv = df.to_csv(r'/Users/Nafees/Desktop/export_dataframe.csv', index=None, header=True)



def shortest_path(lbest, ibest, allpossibletours):
    for i in range(len(allpossibletours)):
        l = totaldistance(allpossibletours[i])
        if l < lbest:
            lbest = l
            ibest = i
    print('Total distance of shortest path {} meters'.format(np.around(lbest, decimals=3)))
    print("Shortest path direction is ->", allpossibletours[ibest])
    return
def longest_path(lbest,ibest,allpossibletours):
    for i in range(len(allpossibletours)):
        l = totaldistance(allpossibletours[i])
        if l > lbest:
            lbest = l
            ibest = i
    print('Total distance of longest path {} meters'.format(np.around(lbest, decimals=3)))
    print("longest path direction is ->", allpossibletours[ibest])

def random_path(tour):
    u = list(it.permutations(tour))
    ulen = len(u)
    random_num = random.randint(1,ulen)
    l = totaldistance(allpossibletours[random_num])
    print('Total distance of random path {} meters'.format(np.around(l, decimals=3)))
    print("longest path direction is ->", allpossibletours[random_num])
def totaldistance(tour):
    d=0
    for i in range(1,len(tour)):
        x1 = Cities[tour[i-1]][0]
        y1 = Cities[tour[i-1]][1]
        x2 = Cities[tour[i]][0]
        y2 = Cities[tour[i]][1]
        d = d+distance(x1,y1,x2,y2)
    x1 = Cities[tour[len(tour)-1]][0]
    y1 = Cities[tour[len(tour)-1]][1]
    x2 = Cities[tour[0]][0]
    y2 = Cities[tour[0]][1]
    d = d + distance(x1, y1, x2, y2)
    return d

Origin = pd.read_csv('/Users/Nafees/Desktop/Book1.csv')
convertion(5,6,Origin)
Data = pd.read_csv('/Users/Nafees/Desktop/export_dataframe.csv')
if Data.empty:
    raise Exception("""At least one of coords must be specified.""")
else:
    Cities = Data.values
    x = Cities.shape
    if x == (1,2):
        raise Exception("""Please enter another coords""")
    else:
        n = len(Data)
        tour = np.arange(n)
        np.random.shuffle(tour)
        allpossibletours = list(it.permutations(tour))
        lbest = int(input("Please enter the total area of affected land in Squre Kilometer: "))*1000
        ibest = 0
        long = 0
        shortest_path(lbest,ibest,allpossibletours)
        print(' ')
        print(' ')
        longest_path(long,ibest,allpossibletours)
        print(' ')
        print(' ')
        random_path(tour)





