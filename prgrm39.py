n=int(input("Enter a no: "))
temp=n
digits=len(str(n))
sum=0
while temp>0:
 digit=temp%10
 sum=sum+digit**digits
 temp=temp//10
if sum==n:
 print("Armstrong no")
else:
 print("Not an Armstrong no")
