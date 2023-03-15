import random
import heapq

#Suppose you have a list birth years and a list of death years for a certain
#population . Can you determine the year at which the population was greatest ?
#You do not know the maximimum or minimum years for birth or death . The domain could
#be 100 years or 1x10 ^ 9 years . It would take to long to go year by year . Use a heap
#instead ?

# priority queue using heap

b1 = [random.randint(1825,2023) for i in range(random.randint(200,210))]
b2 = [random.randint(1826,2023) for i in range(random.randint(190,200))]

event = [(year, 1) for year in b1] + [(year + 1, -1) for year in b2]
print(event)
heapq.heapify(event)
print(event)

current_pop = 0
max_pop = 0
mex_year = None

for i in range(len(event)):
    year,val = heapq.heappop(event)
    current_pop += val

    if current_pop > max_pop:
        max_pop = current_pop
        mex_year = year
    print(f'current_pop = {current_pop}, max_pop = {max_pop}')
print(max_pop,mex_year)
