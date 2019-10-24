name = 'ravi'
new = []
for i in range(len(name)):
    for j in range(i, len(name)):
        new.append(name[i:j+1])
print(new)


