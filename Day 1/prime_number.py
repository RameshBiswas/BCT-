a=int(input("Enter a number "))
prime=True
for i in range(2,int(a**(1/2)+1)):
        if a%i==0:
            prime=False
            break
if prime:
     print(a,"prime number")
else:
     print(a," not prime number")