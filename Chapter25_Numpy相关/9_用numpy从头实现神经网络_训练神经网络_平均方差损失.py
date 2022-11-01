# Qingxiang Guo
# {2022/8/25} {21:57}
'''
假设有这样一组身高，体重，还有性别的数据
姓名	体重(磅)	身高 (英寸)	性别
Alice	133	65	F
Bob	160	72	M
Charlie	152	70	M
Diana	120	60	F

接下来我们用这个数据来训练神经网络的权重和误差，从而可以根据身高体重预测性别：
两个输入x1,x2分别是身高体重。我们用0和1分别表示男性（M）和女性（F），并对数值做了转化：

姓名	体重 (减 135)	身高 (减 66)	性别
Alice	-2	-1	1
Bob	25	6	0
Charlie	17	4	0
Diana	-15	-6	1

这里是随意选取了135和66来标准化数据，通常会使用平均值。
在训练网络之前，我们需要量化当前的网络是『好』还是『坏』，从而可以寻找更好的网络。这就是定义损失的目的。
使用《平均方差损失》来定义，即（真实值-预测值）*平方后，再取均值

比如：

假设我们的网络总是输出0，换言之就是认为所有人都是男性。损失如何？

Name	y_true  y_pred  (y_true - y_pred)^2
Alice	1	0	1
Bob     0	0   0
Charlie	0	0	0
Diana	1	0	1

MSE=（1+0+0+1）/4=0.5，这个值越小越好。我们训练的目的
就是最小化这个值
'''

#下面是计算MSE的代码

import numpy as np

def mse_loss(y_true, y_pred):
  # y_true and y_pred are numpy arrays of the same length.
  return ((y_true - y_pred) ** 2).mean()  #相减，平方，然后取均值

y_true = np.array([1, 0, 0, 1])
y_pred = np.array([0, 0, 0, 0])

print(mse_loss(y_true, y_pred)) # 0.5

