string = input("Enter the string:- ")
count1 = 0
count2 = 0
for i in string:
    if i.isdigit():
        count1 = count1 + 1
    count2 = count2 + 1
print("The number of digit is = ", count1)
print("Total character is = ", count2)