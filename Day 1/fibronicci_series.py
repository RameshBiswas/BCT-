a,b=0,1
for _ in range(10):
    print(a)
    temp=a
    a=b
    b=temp+b
    