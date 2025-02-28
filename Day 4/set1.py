s={}
print("datatype : ",type(s))
new_s=set(s)
print("datatype : ",type(new_s))
print("after adding value : ")
new_s.add(2)
new_s.add(5)
new_s.add(8)
new_s.add(3)
print("set is : ",new_s)
new_s.add(2) 
print("after second time adding value  set is  : ")
print(new_s)
new_s.discard(3)
print("discard an element : ",new_s)
new_s.discard(3)
print("after second time discarding set is : ",new_s)
new_s.remove(5)
print("after revoming 5 the set is ",new_s)
s1={1,2,3,4}
print("first set :",s1)
s2={6,8,0}
print("first set :",s2)
s1.update(s2)
print("after update ",s1)


