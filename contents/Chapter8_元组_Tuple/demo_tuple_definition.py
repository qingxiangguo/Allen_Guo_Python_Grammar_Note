# Qingxiang Guo
# {2022/5/11} {16:56}
'''不可变序列，可变序列'''
'''可变序列包括，列表，字典，就是可以在不修改id的情况下，为可变序列'''
lst=[10,20,45]
print(id(lst))
lst.append(300)
print(id(lst))
'''不可变序列，字符串，元组'''
s='hello'   #字符串一变，id就变了
print(id(s))
s=s+'world'
print(id(s))
print(s)