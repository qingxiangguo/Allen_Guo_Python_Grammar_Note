# Qingxiang Guo
# {2022/8/19} {14:07}
def get_province_population(filename):
    with open(filename) as f:
        for line in f:
            yield int(line)

gen = get_province_population('province_data.txt')  #gen现在是一个生成器
all_population = sum(gen)  #
print(all_population)  #输出7737179，这是总人口

for population in gen:  #gen生成器已经被遍历空了
    print (population/all_population)

'''
执行上面这段代码，除了总人口，将不会有任何输出，这是因为，生成器只能遍历一次。
生成器已经空了
在我们执行sum语句的时候，就遍历了我们的生成器，
当我们再次遍历我们的生成器的时候，将不会有任何记录。所以，上面的代码不会有任何输出。
因此，生成器的唯一注意事项就是：生成器只能遍历一次。
'''