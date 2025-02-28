def add(num1,num2):
    return num1+num2
def mul(num1,num2):
    return num1*num2
def sub(num1,num2):
    return num1-num2
def div(num1,num2):
    return num1/num2
num1=int(input("Enter a your first number "))
num2=int(input("Enter a your second number "))
operation=input("choose a operation \n1.'+' \n2.'-' \n3.'*' \n4.'/' \noperation = ")
if operation=='+':
    print("result =",add(num1,num2))
elif operation=='-':
    print("result =",sub(num1,num2))
elif operation=='*':
    print("result =",mul(num1,num2))
elif operation=='/':
    print("result =",div(num1,num2))