age = int(input("enter your age:- "))
if 0<age<3:
  print("Ticket price is:Free")
elif 3<age<=10:
  print("Ticket price is:150")
elif 11<age<=60:
  print("Ticket price is:250")
else:
  print("Ticket price is:500")
