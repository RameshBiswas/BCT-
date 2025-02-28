text1=input("Enter your day DOB : ")
z=text1.replace("/",".")
print("after replacement",z)
day,month,year=z.split(".")
print("day =",day)
print("month =",month)
print("year =",year)

