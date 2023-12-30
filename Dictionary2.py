# Dictionary



# dict= {
#   999:"Yash",
#   555:"Kunal",
#   444:"Rohan",
#   666:"SAM"
# }

# print(dict[666])



info={'name':'Yash','age':18,'eligible':True}
# print(info['name'])
# print(info['age'])
# print(info.get('eligible'))


# print(info.values())
# print(info.keys())


# for key in info.keys():
#   print(f"The value corresponding to the key {key} is  {info[key]}")

for key,value in info.items():
  print(f"The value corresponding to the key {key} is  {value}")