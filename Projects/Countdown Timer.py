import time

def countdown(t):
    while t:
        mins, secs=divmod(t,60)
        timer='{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        t-=1
    print("Roronoa Zoro")

t=int(input("Enter the time in seconds:"))
countdown(t)
    

# y=divmod(4,2)
# print(y)




# The divmod() function returns a tuple containing the quotient  and the remainder when argument1 (dividend) is divided by argument2 (divisor).

