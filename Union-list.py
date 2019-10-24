l1 = [10,20,30,40,50,60]
l2 = [20,30,80,90,100]
l = []
for i in l1:
    if i in l2:
        l.append(i)
print(l)
