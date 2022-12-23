# Qingxiang Guo
# {2022/8/25} {12:54}
'''
神经网络的基本单位，神经元。神经元接受输入，对其做一些数据操作，然后产生输出。
比如对于一个有两个输入的神经元，x1,x2是两个输入，w1，w2是两个权重，b是误差
那么每个输入都和权重相乘，然后再相加，再加一个误差，即：(x1*w1+x2*w2)+b
再把这个结果传递给激活函数f,y=f(x1*w1+x2*w2+b)，激活函数的用途是将一个无边界的输入，
转变成一个可预测的形式。常用的激活函数就就是S型函数：S型函数的值域是(0, 1)。简单来说，就是把
(−∞, +∞)压缩到(0, 1) ，很大的负数约等于0，很大的正数约等于1。y=1/(1+e^(-x))
一个简单的例子，假如我们有一个神经元，w=[0,1], b=4，两个权重的0,1，误差等于4
输入一个[2，3]，那么根据上面公式，输出=0+3+4=7
y=f(7)=0.999,这种给定输入，得到输出的过程被称为前馈（feedforward）
下面就来编码一个简单神经元
'''

import numpy as np

def sigmoid(x):  #定义激活函数
    return 1 / (1 + np.exp(-x))

class Neuron(object):  #定义神经元
    def __init__(self, weights, bias):  #初始化函数用来输入权重和偏差
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):  #前馈函数用来输入x
        total = np.dot(self.weights, inputs) + self.bias  #np.dot是用点积，即把输入的向量分别和权重相乘，再加上误差
        return sigmoid(total)  #得到输出

weights = np.array([0, 1]) # w1 = 0, w2 = 1
bias = 4                   # b = 4
n = Neuron(weights, bias)  #实例化一个神经元对象，其中初始化参数为权重与误差
print(n.feedforward(np.array([2,3])))  #numpy建立一个数组，输入给n的feedforward函数，得到sigmoid(total)
#输出0.9990889488055994
