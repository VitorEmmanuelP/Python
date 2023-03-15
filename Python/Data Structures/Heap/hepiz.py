import random
import heapq

# Heap.heapify turns an unsorted arary into a minHeap
x = [1,3,5,2,4,6]
heapq.heapify(x)
print(x)
# if you want a maxHeap you have to multipy the array by -1
z = [1,3,5,2,4,6]
z = [ -1 * i for i in z]
heapq.heapify(z)
print(z)

# heapq.heappush insert values ( list , value )
heapq.heappush(x,65)
print(x)

# heapq.heappop removes the min heap or the max if it is a max heap ( list )
heapq.heappop(x)
print(x)

# heappushpop insert then removes the min or max value ( lista , value )
heapq.heappushpop(x,20)
print(x)
# heappushpop removes the min or max value  then insert the value ( lista , value )
heapq.heapreplace(x,100)
print(x)

# heapq.nsmallest return the given numbers or smarllest values ( how many you want, the iterable )
heapq.nsmallest(2,x)
# heapq.nsmallest return the given numbers or largest values ( how many you want, the iterable )
heapq.nlargest(2,x)

# using as a priority queue with tuples

fila_de_espera = [(10,'Vitor'),(20,'Kevem'),(30,'Vanessinha'),(15,'Fred'),(25,'Emmanuel'),(1,'abc'),(1.1,'Mesqui')]
heapq.heapify(fila_de_espera)

for i in range(len(fila_de_espera)):
    print(f'Removido: {heapq.heappop(fila_de_espera)}')

