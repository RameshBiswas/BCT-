from prettytable import PrettyTable
class myclass:
 def __init__(self):
        self.l=[]
        self.table = PrettyTable()
 def signup(self):
  email=input("Enter a email : ")
  password=input("password : ")  
  if email.endswith("@gmail.com"):
    a={
        "e":email,
        "p":password,
        }
    self.l.append(a)
  else:
        print("Enter a valid gmail") 

 def login(self):
    email1=input("plz Enter your email : ")
    password1=input("password : ")
    b={
        "e":email1,
        "p":password1,
        }
    for i in self.l:
      if i["e"] == email1 and i["p"] == password1:
        print("You successfully login in") 
        p=int(input("Select an option\n1.logout\n2.exit\n"))
        if p=='1':
          print("logout successfully")
          
        else:
          break
      else:
        print("Incorrect email or password. Please try again.")
 def show(self):
  n=1
  for data in self.l:
    self.table.field_names=(["no","email","password"])
    self.table.add_row([n,data["e"],data["p"]])
    n=n+1
    # print(l)
  print(self.table)
  
  
def main():
  t=myclass()
  print("create an account -->>")
  while 1:
   z=input("Select an option\n1.login\n2.signup\n3.show\n4.exit\n")
   if z=='1':    
    t.login()
    continue
   elif z=='2':
    t.signup()
   elif z=='3':
    t.show()
   elif z=='4':
    print("Exit")
    break
if __name__ == "__main__":
    main()