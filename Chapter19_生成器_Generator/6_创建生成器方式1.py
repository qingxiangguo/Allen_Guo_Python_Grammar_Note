# Qingxiang Guo
# {2022/7/4} {20:41}
#第一种：列表生成式的中括号变成小括号
nums=[x for x in range(5)]  #列表生成式
print(type(nums))  #<class 'list'>
print(nums)  #[0, 1, 2, 3, 4]

nums2=(x for x in range(5))  #生成器，用的时候现生成
print(type(nums2))  #<class 'generator'>
print(nums2)  #<generator object <genexpr> at 0x0000023D429E9A10>

for item in nums2:
    print(item)

'''
0
1
2
3
4
'''