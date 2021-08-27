from functools import reduce
#First reduce function with lambda
num=[1,2,3,4]
print(reduce(lambda x,y:x+y,num))
#Second filter function with lambda
print(list(filter(lambda x : x%2==0 , range(1,11))))
#Third map function with lambda
print(list(map(lambda x:x*x,num)))