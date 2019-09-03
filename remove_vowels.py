name = input("Enter the string:- ")
vowels = ['a','e','i','o','u']
for i in name:
  for i in vowels:
    if i in name:
      name = name.replace(i,'')
print(name)
