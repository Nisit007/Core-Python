# STRING latter replace

# name = input('enter a string:- ')
# for i in name:
#     org = name.replace('i' , '$')
# print(org)


# def remove(string, n):
#     first = string[:n]
#     last = string[n + 1:]
#     return first + last
#
#
# name = input('enter the name:- ')
# a = int(input('enter the index if you want to remove:- '))
# print(remove(name, a))

# VOWEL founder

name = input('enter a string:- ')
vowels = 0
for i in name:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vowels = vowels+1

print(vowels)


# STRING reversing

#
# def rev(x):
#     return x[::-1]
#
#
# name = rev(input("enter the string"))
# print(name)
