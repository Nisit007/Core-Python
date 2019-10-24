a = int(input('Enter the date:- '))
b = int(input('Enter the Month:-'))
c = int(input('Enter he Year:-'))
if 0 < a <= 31 and 0 < b <= 12 and 0 <= len(str(c)) <= 4:
    print("Valid date")
    print('The  Today Date is:-', a, "/", b, "/", c)
    if a == 28 and b == 2:
        a = 1
        b = b + 1
        print('The next day Date is :- ', a, "/", b, '/', c)
    elif 0 < a <= 29:
        a = a + 1
        print('The next day Date is :- ', a, "/", b, '/', c)
    elif a == 31 and b == 12:
        a = 1
        b = 1
        c = c + 1
        print('The next day Date is :- ', a, "/", b, '/', c)
        print('HAPPY NEW YEAR.....!')
    elif a == 30 and b == 4 or b == 6 or b == 9 or b == 11:
        a = 1
        b = b + 1
        print('The next day Date is :- ', a, "/", b, '/', c)
    elif a == 31 and b == 1 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12:
        a = 1
        b = b + 1
        print('The next day Date is :- ', a, "/", b, '/', c)
else:
    print('Enter valid date format ..!')
