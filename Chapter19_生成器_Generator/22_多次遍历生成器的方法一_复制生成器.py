# Qingxiang Guo
# {2022/8/19} {14:19}
'''
生成器只能被遍历一次，如果想多次，可以采用复制的方法
'''
import itertools

def get_province_population(filename):
    with open(filename) as f:
        for line in f:
            yield int(line)

gen = get_province_population('province_data.txt')  #gen现在是一个生成器
#下面开始复制生成器
(gen1,gen_copy) = itertools.tee(gen,2)  #从gen中复制2个，一个gen1，一个gen_copy
#注意，这里的复制，更像是分裂，原来的gen就不能用了

all_population = sum(gen1)  #gen1被消耗完了
print(all_population)  #输出7737179，这是总人口
for population in gen_copy:  #gen1被消耗完了，这里遍历复制出来的gen_copy
    print (population/all_population)

'''
7737179
0.013208948636188978
0.0015797747473594705
0.011061266645117038
0.0717327335970901
0.5083030908293579
0.3941141855448866
'''

''''
但是，itertools.tee有两个缺陷：
其一是如果原始生成器能循环非常多次，产生的数据量非常大，并且你在消费的时候，
是先迭代第一个分裂后的生成器，完整迭代完以后再迭代第二个分裂后的生成器，那么这将会浪费大量内存。
所以，应该让两个生成器能间隔着迭代，或者“同时”迭代。
其二，多个生成器同时迭代也有问题，分裂出来的多个生成器不是线程安全的，在多线程里面同时运行会导致报错。
'''
