psum = 0
nsum = 0
for i in range(1,6):
 num = int(input("Enter a number"))
if num>0:
    psum += num
else:
    nsum += num
print("positive number  =",psum)
print("negative number =",nsum)