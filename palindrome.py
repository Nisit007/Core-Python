# string = input("enter the string:- ")
# if string == string[::-1]:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")
#

###### Second method #####
# string = input("Please enter your own String:- ")
# str1 = ""
# for i in string:
#     str1 = i + str1
# print("String in reverse Order:- ", str1)
#
# if (string == str1):
#     print("This is a Palindrome String")
# else:
#     print("This is Not a Palindrome String")

####### Third method #####
# num = int(input("enter a number: "))
#
# temp = num
# rev = 0
#
# while temp != 0:
#     rev = (rev * 10) + (temp % 10)
#     temp = temp // 10
#
# if num == rev:
#     print("number is palindrome")
# else:
#     print("number is not palindrome")