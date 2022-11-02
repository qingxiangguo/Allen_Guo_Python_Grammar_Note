# 转义字符
print('hello\nworld')   # \ + 转移功能首字母，n=newline的首字母表示换行
print('hello\tworld')
print('helloooo\tworld')   # \t是四个一组的，不到四个，就不重开，补齐到四
print('hello\rworld')    # \r 回车，是回到本行首位重新开始输入，所以world会覆盖前面的hello
print('hello\bworld')  # \b是退一个格，将o退没了
print('老师说：\'大家好\'')

# 原字符，不希望字符中的所有转义字符起作用，就使用原字符，就是在字符串之前加上r，或R，原汁原味输出
print(r'hello\nworld')
# 注意事项，原字符，最后一个字符不能是单个反斜杠，会把最后一个引号给转义了
# print(r'hello\nworld\')
# 但是最后是两个反斜线是ok的
print(r'hello\nworld\\')