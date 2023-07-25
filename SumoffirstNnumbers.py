Find the Sum of the First N Natural Numbers in Python
Method 1: Loop
num = int(input("Enter Value:"))
sum = 0
for i in range(num+1):
  sum+=i
print(sum)


Method 2: Formula
Num= int(input("Enter number"))
print(int( Num * ( Num + 1 ) ) / 2)
