i = 1
while i<=10:
  print("Hello world")  #--->print Hello world 10 times
  print(f"Hello world {i}") #--->print Hello world with numbers
  i += 1
#################

i = 1
while i < 6:
    i = i + 1
    if i == 3:
        break #---> Break the loop whan i=3
    print(i)
################

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  #---> Skip the value of i
    print(i)
################

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
