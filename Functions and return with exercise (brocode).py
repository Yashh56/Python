# function = A block of reusable code
#            place() after the function name to invoke it !!

# f is the format string


def happy_birthday(name):
    print(f"Happy Birthday to {name}!!")
    print(f"May your all wishes comes trues {name}!!")
    print("Once again happy birthday")
    print()


happy_birthday("Yash")


import datetime

today= datetime.date.today()
print(f"{today:%B %d, %Y}")




#EXERCISE-1 FUNCTIONS (BROCODE)



def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount} is due:{due_date}")

display_invoice("Yashh",50,"06/21")





# return = statement used to end a function
#       and send a result back to the caller


def add(x,y):
    z=x+y
    return z

def substract(x,y):
    z=x-y
    return z

def multiply(x,y):
    z=x*y
    return z

def divide(x,y):
    z=x/y
    return z

print(add(4,2))
print(substract(4,2))
print(multiply(4,2))
print(divide(4,2))




#EXERCISE-2 RETURN (BROCODE)


def create_name(first,last):
    first =first.capitalize()
    last=last.capitalize()
    return first+" "+last

full_name=create_name("Yash","Saini")

print(full_name)