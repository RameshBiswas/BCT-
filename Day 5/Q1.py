num1=int(input("Enter number :"))
num2=int(input("Enter number:"))
try:
    z=num1/num2
    print(z)
except ZeroDivisionError:
    print("error")