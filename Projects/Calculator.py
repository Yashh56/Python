
first = input("Enter the Number")
operator = input("enter operator(+,-,/,%,*):")
second = input("Enter the Number")

first=int(first)
second=int(second)


if operator =="+":
    print(first+second)

elif operator =="-":
    print(first-second)

elif operator =="/":
    print(first/second)

elif operator =="%":
    print(first%second)

elif operator =="*":
    print(first*second)

else :
    print("Invalid Operations")


