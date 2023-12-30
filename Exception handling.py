# a=input("Enter the number")
# print(f"Multiplication table of {a} is:")
# try:
#   for i in range(1,11):
#     print(f"{int(a)}x{i}={int(a)*i}")
# except Exception as e:
#   print(e)


# print("some imp of lines")
# print("End of program")


# 
# a=input("Enter the number")
# print(f"Multiplication table of {a} is:")
# try:
#   for i in range(1,11):
#     print(f"{int(a)}x{i}={int(a)*i}")
# except :
#   print("invalid output")


# print("some imp of lines")
# print("End of program")


# try:
#   num= int(input("Enter the integer"))
# except ValueError:
#   print("Number entered is not an integer.")


try:
  num= int(input("Enter the integer"))
  a=[6,3]
  print(a[num])


except ValueError:
  print("Number entered is not an integer.")

except IndexError:
  print("Index Error")