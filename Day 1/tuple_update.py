tuple1=('a','b','c','d')
print("initial tuple :")
for i in tuple1:
    print(i,end=" ")
a = list(tuple1)
a.append('e')
b=tuple(a)
print("\nafter update tuple")
for i in b:
    print(i,end=" ")


    
