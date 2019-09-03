# l1 = [10,20,30,40]
# l = []
# for i in range(len(l1)):
#     if i == 0:
#         l1[i] = l1[i]
#     else:
#         l1[i] = l1[i] + l1[i-1]
# print(l1)


l1 = [10,20,30,40,50,60]
l2 = [20,30,80,90,100]
l = []
for i in l1:
    if i in l2:
        l.append(i)
# for i in range(len[l2]):
#     l4=i[l2] + 1
#     l.append(l4)
print(l)


# number = [1,1,2,3,4]
# temp = []
# i = 0
# while i < len(number):
#     if number[i] not in temp:
#         temp.append(number[i])
#         # print(number[i])
#     i += 1
# print(temp)
# print('length = ',len(temp))