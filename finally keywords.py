# try:
#   l=[4,5,7,2,9]
#   i=int(input("enter the index:"))
#   print(l[i])
# except:
#   print("some error occurred")
   

# finally:
#   print("I am always executed")




def func1():
  try:
    l=[4,5,7,2,9]
    i=int(input("enter the index:"))
    print(l[i])
    return 1
  
  except:
   print("some error occurred")
   return 0
  
  finally:
    print("I am always executed")

x=func1()
print(x)