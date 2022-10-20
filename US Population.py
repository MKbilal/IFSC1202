list_population = []
list_change = [0]
list_percent = [0]

population_list = []
with open("08.11 USPopulation.txt") as f:
    population_list = f.read().split('\n')
    for i in range(len(population_list)):
        population_list[i] = int(population_list[i]) * 1000

print(population_list)
print('Year    Population   Change     Percent Change')
for x in range(0,(1990-1950)+1):
    print(1950+x, end="    ")
    print(population_list[x], end="    ")
    print('N/A' if x==0 else population_list[x]-population_list[x-1], end="\t")
    if x == 0:
        print('N/A')
    else:
        change = population_list[x] - population_list[x-1]
        percent = (change/population_list[x-1]) * 100
        percent = str(percent)
        percent = percent[:1 + 3]
        percent = percent + '%'
        print(percent)
        
for i in range(len(population_list)):
        population_list[i] = int(population_list[i]) * 1000

average = sum(list_change) / 41
print("Average population change:",change)
maxi = list_change[1]
mini = list_change[1]
max_index = 0
min_index = 0
for i in range(2,len(list_change)):
    if(list_change[i]>maxi):
        maxi = list_change[i]
        max_index = i
    if(list_change[i]<mini):
        mini = list_change[i]
        min_index = i
print("Minimum change:",mini,[1950+min_index])
print("Maximum change:",maxi,[1950+max_index])