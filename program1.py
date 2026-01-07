#program to print sum of 1 to n
n = int(input("enter n value:"))
print ("entered value:", n)
sum = 0
for i in range(1,n+1):
    # print(i)
    sum = sum + i
    
print("total sum from 1 to {} is {}".format(n,sum))