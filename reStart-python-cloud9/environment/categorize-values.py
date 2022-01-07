'''
myMixedTypeList=[45,290578,1.02,True,"My dog is on the bed","45"]
for item in myMixedTypeList:
    print("{} is of the type {}.".format(item,type(item)))
    
for i in range(10):
    print(i)

print ()
fruits = ("apple","orange","mango")
for item in fruits:
    print(item)
    
for x in "banana":
    print(x)'''
    
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
      continue
  print(x)
    