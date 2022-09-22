l2 = []
l1 = [12,34,7,3,12,67,7]

for i in l1:
    if i not in l2:
        l2.append(i)

print(l1)
print(l2)