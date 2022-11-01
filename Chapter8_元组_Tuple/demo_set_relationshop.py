# Qingxiang Guo
# {2022/5/12} {14:55}
#集合间的关系

'''两个集合是否相当（元素相同就相等）'''
s={10,20,30,40}
s2={30,40,20,10}   #因为集合无序，所以两者相等
print(s==s2)   #True
print(s!=s2)  #False

'''一个集合是否是另一个集合的子集'''
s1={10,20,30,40,50,60}
s2={10,20,30,40}
s3={10,20,90}
print(s2.issubset(s1))  #True
print(s3.issubset(s1))   #False

'''一个集合是否是另一个集合的超集(父集)'''
print(s1.issuperset(s2))   #True
print(s1.issuperset(s3))   #False

'''两个集合是否《无交集》'''
print(s2.isdisjoint(s3))  #s2与s3有交集，所以False
s4={100,200,300}

print(s2.isdisjoint(s4))  #True