import calculatator
num1=int(input("Enter a your first number "))
num2=int(input("Enter a your second number "))
operation=input("choose a operation \n1.'+' \n2.'-' \n3.'*' \n4.'/' \noperation = ")
if operation=='+':
    print("result =",calculatator.add(num1,num2))
elif operation=='-':
    print("result =",calculatator.sub(num1,num2))
elif operation=='*':
    print("result =",calculatator.mul(num1,num2))
elif operation=='/':
    print("result =",calculatator.div(num1,num2))
