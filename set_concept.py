# most IMP
# set which is represent by{}
#set which is unorder , unindex , immutable
#which does not contain duplicate elements
# remove duplicate elements from list using set

l1 = {12,34,67,89,4,4,6,6}
s = set(l1)
l1 = list(s)
print(l1)

l2 = []
l1 = [12,34,7,3,12,67,7]

for i in l1:
    if i not in l2:
        l2.append(i)

print(l1)
print(l2)