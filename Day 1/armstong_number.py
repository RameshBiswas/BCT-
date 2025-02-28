a=int(input("Enter a number "))
temp=a
sum=0
while a>0:
    r=a%10
    sum=sum+r**3
    a=int(a/10)
if temp==sum:
    print("its a armstrong number")
else:
    print("its not a armstrong number")