# MAP

def cube(x):
  return x*x*x

print(cube(3))



l=[2,4,6,8,10,12]
# newl=[]
# for item in l:
#   newl.append(cube(item))

# print(newl)


newl=list(map(cube,l))
print(newl)


# FILTER    

def filter_function(a):
  return a>2

newnewl=list(filter(filter_function,l))
print(newnewl)



# REDUCE

from functools import reduce

numbers=[1,2,3,4,5]

sum=reduce(lambda x,y: x+y,numbers)

print(sum)

# Both are same examples but one are in function and another one is not in function.

def mysum(x,y):
  return x+y

sum=reduce(mysum,numbers)
print(sum)

