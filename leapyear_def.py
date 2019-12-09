def get_integer(a, b):
    for i in range(a, b+1):
        if i < 1582 and i >9999:
            print("enter valid")
        yield (i)


letter = int(input("enter the year"))
if letter in get_integer(1582, 9999):
    print(letter)
# else:
#     print("enter valid year")
    if letter % 4 == 0:
        if letter % 100 == 0:
            if letter % 400 == 0:
                print("it is leap")
            else:
                print("it is not ")
        else:
            print("it is leap")
    else:
        print("it is not")
else:
    print("enter valid year")
