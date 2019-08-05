number = int(input("Enter the winnig number"))
Winnig_number = 47
if number == winning_number:
  print("You win")
else:
  if number > winning_number:
    print("Too High")
  else:
    print("Too Low")
