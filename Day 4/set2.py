s1={1,2,3,4,5}
s2={1,2,3}
s3={9,0,3}
print("s1 = ",s1,"\ns2 = ",s2,"\ns2 is subset of s1",s2.issubset(s1))
print("s1 = ",s1,"\ns2 = ",s2,"\nsuperset of s2 is s1 : ",s3.issuperset(s1))
print("s1 = ",s1,"\ns3 = ",s3,"\nintersection of s1 and s3 : ",s1.intersection(s3))
print("s1 = ",s1,"\ns3 = ",s3,"\nunion of s1 and s3 : ",s3.union(s1))

