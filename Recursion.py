#Recursion in Python

# Factorial 


def factorial(i):
  if(i==0) or (i==1):
    return 1
  else:
    return i * factorial(i-1)


print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))


# fibonacci (quick quiz done by me ;)
# Fn=Fn-1+Fn-2


def fibonacci(i):
  if (i==1) or (i==2):
    return 1
  else:
    return fibonacci(i-1) + fibonacci(i-2)

print(fibonacci(6))