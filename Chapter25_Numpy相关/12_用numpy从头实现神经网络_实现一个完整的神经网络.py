# Qingxiang Guo
# {2022/8/26} {20:45}
import numpy as np

def sigmoid(x):   #激活函数
  # Sigmoid activation function: f(x) = 1 / (1 + e^(-x))
  return 1 / (1 + np.exp(-x))

def deriv_sigmoid(x):  #激活函数的导数，后面要用
  # Derivative of sigmoid: f'(x) = f(x) * (1 - f(x))
  fx = sigmoid(x)
  return fx * (1 - fx)

def mse_loss(y_true, y_pred):  #平均方差损失
  # y_true和y_pred是相同长度的numpy数组。
  return ((y_true - y_pred) ** 2).mean()

class OurNeuralNetwork:
  '''
  A neural network with:
    - 2 inputs
    - a hidden layer with 2 neurons (h1, h2)
    - an output layer with 1 neuron (o1)
  '''
  def __init__(self):
    # 权重，Weights
    self.w1 = np.random.normal()  #该函数用于生成高斯随机分布是随机数,self.w1是神经网络的权重属性
    self.w2 = np.random.normal()
    self.w3 = np.random.normal()
    self.w4 = np.random.normal()
    self.w5 = np.random.normal()
    self.w6 = np.random.normal()

    # 截距项，Biases
    self.b1 = np.random.normal()
    self.b2 = np.random.normal()
    self.b3 = np.random.normal()

  def feedforward(self, x):  #前馈函数，输入为x，x是numpy数组
    # X是一个有2个元素的数字数组。
    h1 = sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.b1)   #x[0]就是x1，这里讲h1隐藏层给表达出来
    h2 = sigmoid(self.w3 * x[0] + self.w4 * x[1] + self.b2)
    o1 = sigmoid(self.w5 * h1 + self.w6 * h2 + self.b3)
    return o1  #o1是最终的输出，也叫Ypred

  def train(self, data, all_y_trues):   #训练函数，其中date是所有的权重和截距数值，all_y_trues是真实的性别值
    '''
    - data is a (n x 2) numpy array, n = # of samples in the dataset.
    - all_y_trues is a numpy array with n elements.
      Elements in all_y_trues correspond to those in data.
    '''
    learn_rate = 0.1  #随机梯度下降的学习率
    epochs = 1000 # 遍历整个数据集的次数，就是你训练的次数

    for epoch in range(epochs):  #从训练的0到999次，训练1000次
      for x, y_true in zip(data, all_y_trues):   #每一次当中，都将一行行的数据拿出来训练，zip是将x与y缝合
        # --- 做一个前馈(稍后我们将需要这些值)
        sum_h1 = self.w1 * x[0] + self.w2 * x[1] + self.b1
        h1 = sigmoid(sum_h1)   #这是当前h1的值

        sum_h2 = self.w3 * x[0] + self.w4 * x[1] + self.b2
        h2 = sigmoid(sum_h2)   #这是当前h2的值

        sum_o1 = self.w5 * h1 + self.w6 * h2 + self.b3
        o1 = sigmoid(sum_o1)
        y_pred = o1   #这是当前输出的值

        # --- 计算偏导数。
        # --- Naming: d_L_d_w1 代表，求L对w1的偏导，L是整个系统的平均均方差
        d_L_d_ypred = -2 * (y_true - y_pred)  #将L换算成(y_true - y_pred)^2可以求得

        # Neuron o1
        d_ypred_d_w5 = h1 * deriv_sigmoid(sum_o1)
        d_ypred_d_w6 = h2 * deriv_sigmoid(sum_o1)
        d_ypred_d_b3 = deriv_sigmoid(sum_o1)

        d_ypred_d_h1 = self.w5 * deriv_sigmoid(sum_o1)  #偏导数，这个值是为了反向传播，计算后面的dL/dw1而提前计算好的
        d_ypred_d_h2 = self.w6 * deriv_sigmoid(sum_o1)

        # Neuron h1
        d_h1_d_w1 = x[0] * deriv_sigmoid(sum_h1)
        d_h1_d_w2 = x[1] * deriv_sigmoid(sum_h1)
        d_h1_d_b1 = deriv_sigmoid(sum_h1)

        # Neuron h2
        d_h2_d_w3 = x[0] * deriv_sigmoid(sum_h2)
        d_h2_d_w4 = x[1] * deriv_sigmoid(sum_h2)
        d_h2_d_b2 = deriv_sigmoid(sum_h2)

        # --- 更新权重和偏差
        # Neuron h1
        self.w1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w1  #本质就是dL/dw1，因为后面随机梯度下降，要用这个值来优化
        self.w2 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w2  #这就是正式开始优化的过程
        self.b1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_b1

        # Neuron h2
        self.w3 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w3
        self.w4 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w4
        self.b2 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_b2

        # Neuron o1
        self.w5 -= learn_rate * d_L_d_ypred * d_ypred_d_w5
        self.w6 -= learn_rate * d_L_d_ypred * d_ypred_d_w6
        self.b3 -= learn_rate * d_L_d_ypred * d_ypred_d_b3

      # --- 在每次epoch结束时计算总损失
      if epoch % 10 == 0:  #这里已经将所有样本遍历完了，但是第一次遍历还没结束，这里是每隔10次输出一次
        y_preds = np.apply_along_axis(self.feedforward, 1, data)
        #apply_along_axis是numpy从，沿着横轴（1）或纵轴（0）取值，生成新数组的函数
        #上面的意思是，沿着横向，将data也就是权重和截距，赋给前馈函数，然后返回一个新数组，y_preds=[预测值1，预测值2。。。]
        loss = mse_loss(all_y_trues, y_preds)   #注意，all_y_trues, y_preds都是数组，返回一个均值，就是平均方差均值
        print("Epoch %d loss: %.3f" % (epoch, loss))

# 定义数据集
data = np.array([
  [-2, -1],  # Alice  #体重和截距
  [25, 6],   # Bob
  [17, 4],   # Charlie
  [-15, -6], # Diana
])
all_y_trues = np.array([  #真实性别所有的
  1, # Alice
  0, # Bob
  0, # Charlie
  1, # Diana
])

# 训练我们的神经网络!
network = OurNeuralNetwork()
network.train(data, all_y_trues)

'''
Epoch 0 loss: 0.229
Epoch 10 loss: 0.148
Epoch 20 loss: 0.103
Epoch 30 loss: 0.076
Epoch 40 loss: 0.058
Epoch 50 loss: 0.046
Epoch 60 loss: 0.038
'''