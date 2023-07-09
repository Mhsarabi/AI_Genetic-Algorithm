
import random as rnd

p_s=200
n=8
m_r=0.8
epoch=200

def init_population(population_size,N):
     population_list=[]
     for i in range(population_size):
          new_member=[]
          for j in range(n):
               new_member.append(rnd.randint(1,n))
          new_member.append(0)
          population_list.append(new_member)
     return population_list

def cross_over(population_list):
    for i in range(0,len(population_list),2):
        chil1=population_list[i][:len(population_list[0])//2]+population_list[i+1][len(population_list[0])//2:len(population_list[0])-1]+[0]
        chil2=population_list[i+1][:len(population_list[0])//2]+population_list[i][len(population_list[0])//2:len(population_list[0])-1]+[0]
    
        population_list.append(chil1)
        population_list.append(chil2)
    return population_list

def mutation(population_list,mutation_rate,n):
    choosen_one=[i for i in range(len(population_list)//2,len(population_list))]
    for i in range(len(population_list)//2):
        new_random=rnd.randint(0,(len(population_list)//2)-1)
        choosen_one[new_random],choosen_one[i]=choosen_one[i],choosen_one[new_random]
    choosen_one=choosen_one[:int(len(choosen_one)*mutation_rate)]
     
    for i in choosen_one:
        new_ch=rnd.randint(0,n-1)
        new_value=rnd.randint(1,n)
        population_list[i][new_ch]=new_value
    return population_list

def fitness(population_list,n):
    i=0
    length=len(population_list)
    conflict=0
    while i<length:
       j=0
       conflict=0
       while j<n:
           k=j+1
           while k<n:
               if population_list[i][j]==population_list[i][k]:
                   conflict+=1
               if abs(j-k)==abs(population_list[i][j]-population_list[i][k]):
                   conflict+=1
               k+=1
           j+=1
       population_list[i][len(population_list[j])-1]=conflict
       i+=1
    for i in range(len(population_list)):
        _min=i
        for j in range(i,len(population_list)):
            if population_list[j][n]<population_list[_min][n]:
                _min=j
        population_list[i],population_list[_min]=population_list[_min],population_list[i]
    return population_list

population=init_population(p_s,n)
population=fitness(population,n)
if population[0][n]==0:
  print("solution found: ",population[0][0:n])
else:
 for i in range(epoch):
  population=cross_over(population)
  population=mutation(population,m_r,n)
  population=fitness(population,n)
  population=population[:len(population)//2]
  if population[0][n]==0:
    print("solution found: ",population[0][0:n])
    break
  else:
   print("*",i+1,"------>Best Solution so now:",population[0])