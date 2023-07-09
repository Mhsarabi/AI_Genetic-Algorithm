
from random import randint as rnd
from random import shuffle
import numpy as np
import matplotlib.pyplot as plt
import cv2


N_cities=200
Width=1000
Height=1000

population_size=100
Epoch=200

def random_city_generator(n_c,a_w,a_h):
    offset=20
    cities=[]
    i=0
    while i<n_c:
        city_location=[rnd(offset,a_w-offset),rnd(offset,a_h-offset)]
        if city_location not in cities:
            cities.append(city_location)
            i+=1
    return cities

def init_population(n,ps):
    population_list=[]
    for i in range(ps):
        path=[i for i in range(n)]
        shuffle(path)
        path+=[None]
        population_list.append(path)
    return population_list

def cross_over(population_list,n,p):
    for i in range(p):
        path=population_list[i][:n]+[None]
        population_list.append(path)
    return population_list

def mutation(population_list,n,p):
    lenght=p*2
    i=p
    while i<lenght:
      cell1=rnd(0,n-1)
      cell2=rnd(0,n-1)
      if cell1!=cell2:
        population_list[i][cell1],population_list[i][cell2]=population_list[i][cell2],population_list[i][cell1]
        i+=1
          
    return population_list

def path_cordinates(Cities_location,path):
    cordinates=[]
    for i in path:
        cordinates.append(Cities_location[i])
    return cordinates


def euclidean_distance(path):
    distance=0
    for i in range(len(path)-1):
       distance+=np.sqrt((path[i][0]-path[i+1][0])**2 +(path[i][1]-path[i+1][1])**2)
    return distance


def fitness(population_list,n,location_list):
    for i in range(len(population_list)):
        if population_list[i][-1]==None:
            current_path=path_cordinates(location_list,population_list[i][:n]+[population_list[i][0]])
            d=euclidean_distance(current_path)
            population_list[i][n]=d
    return population_list

def sorted(population_list,C):
    population_list.sort(key=lambda x:x[C])
    return population_list

def draw_cities(img,cities_location,color):
    for x,y in cities_location:
        img=cv2.circle(img,(x,y),6,color,-1)
    return img

def draw_path(img,path,color):
    for i in range(len(path)-1):
        img=cv2.line(img,path[i],path[i+1],color,2)
    return img

Cities_location=random_city_generator(N_cities,Width,Height)
current_population=init_population(N_cities,population_size)
for i in range(1,Epoch+1):
 current_population=cross_over(current_population,N_cities,population_size)
 current_population=mutation(current_population,N_cities,population_size)
 current_population=fitness(current_population,N_cities,Cities_location)
 current_population=sorted(current_population,N_cities)
 current_population=current_population[:population_size]
#  print("Best Path and Distance so now:",current_population[0])

else:
 print("Best found solution :",current_population[0])
 area=np.full((Width,Height,3),255,np.int16)
 area=draw_cities(area,Cities_location,(255,0,0))
 current_path=path_cordinates(Cities_location,current_population[0][:N_cities])
 current_path+=[current_path[0]]
 area=draw_path(area,current_path,(0,0,255))
 plt.imshow(area)
 plt.grid()
 plt.show()