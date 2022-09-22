#find even and odd number in for loop
esum = 0
osum = 0
for i in range(1,6):
 num=int(input("enter a number : "))
if num%2 ==0:
  esum += num
else:
  osum += num 

print("total even sum = ",esum)
print("totaal odd sum = ",osum)
  
  
  