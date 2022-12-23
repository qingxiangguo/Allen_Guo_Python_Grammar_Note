# Qingxiang Guo
# {2022/8/25} {21:32}
'''
所谓的神经网络就是一堆神经元，包括输入层和输出层，隐藏层
隐藏层就是输入层和输出层之间的层，隐藏层可以是多层的。以一个简单的神经网络为例子
这个网络有两个输入x1，x2，一个有两个神经元（ 和 ）的隐藏层，
以及一个有一个神经元（ ) ）的输出层。要注意， 的输入就是 和  的输出，这样就组成了一个网络。
假设每个节点神经元的权重都是w=[0,1]，误差也都是b=0,激活函数都是S
当输入x=[2,3]时，会得到什么结果？h1=h2=f(0*2+1*3+0)=f(3)=0.9526
那么将h1，h2再套用一遍，就是o1。o1=f(0*0.9526+1*0.9526+0)=f(0.9526)=0.7216
下面用代码实现
'''
import numpy as np

def sigmoid(x):  #定义激活函数
    return 1 / (1 + np.exp(-x))

class Neuron(object):  #定义每一个神经元
    def __init__(self, weights, bias):  #初始化函数用来输入权重和偏差
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):  #前馈函数用来输入x
        total = np.dot(self.weights, inputs) + self.bias  #np.dot是用点积，即把输入的向量分别和权重相乘，再加上误差
        return sigmoid(total)  #得到输出

class OurNeuralNetwork(object):  #定义神经网络，会调用上面的神经元
    '''
  A neural network with:
    - 2 inputs
    - a hidden layer with 2 neurons (h1, h2)
    - an output layer with 1 neuron (o1)
  Each neuron has the same weights and bias:
    - w = [0, 1]
    - b = 0
    '''
    def __init__(self):
        weights = np.array([0, 1])
        bias = 0
        #下面调用上面的Neuron类，实例化出三个对象，分别是两个隐藏层对象和一个输出层对象
        self.h1 = Neuron(weights, bias)  #这个实例对象装到神经网络对象的属性里面
        self.h2 = Neuron(weights, bias)
        self.o1 = Neuron(weights, bias)

    def feedforward(self, x):  #神经网络的前馈函数
        out_h1 = self.h1.feedforward(x)  #由于self.h1是神经元对象，他自己就有feedforward方法
        out_h2 = self.h2.feedforward(x) #因为输入x和weights都是数组形式，所以可以用点积分析

        # o1的输入是h1和h2的输出
        out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))  #再将上面两个结果变为新数组输入
        return out_o1

network = OurNeuralNetwork()
x = np.array([2, 3])
print(network.feedforward(x))  #输出0.7216325609518421
#结果正确，看上去没问题
