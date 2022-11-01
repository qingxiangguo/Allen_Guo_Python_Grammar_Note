# Qingxiang Guo
# {2022/8/26} {20:06}
#因为后面的随机梯度下降，需要用到dL/dw1，或者dL/dw2，或者dL/db1，来一个个的对权重进行优化
#其中dL/dw1代表L平方差均值对于w1的偏导，所以涉及到计算每一个权重或者误差的偏导
#那么这里用到了反向传播，即将dL/dw1拆分成，我们能计算的几个部分，然后再乘在一起
#举个例子，我们要计算dL/dw1，可以改写成，dL/dw1 = (dL/dYpred)*(dYpred/dw1)
#dYpred，是预测值的偏导
#所以，(dL/dYpred)=d[(Ytrue-Ypred)^2]/dYpred，由于是求偏导，这里把Ytrue看成常数，Ypred看成变量
#所以(dL/dYpred)=-2(Ytrue-Ypred)
#现在再来搞定(dYpred/dw1)，h1,h2,o1分别表示隐藏层神经元和输出神经元
#Ypred实际上=o1=f(w5h1+w6h2+b3)，其中f是激活函数
#(dYpred/dw1)可以改写成，(dYpred/dh1)*(dh1/dw1)，就是一步步拆分，各个击破
#其中，dYpred/dh1，是求对于h1的偏导，除了h1以外的，都看成常数，又因为Ypred=f(w5h1+w6h2+b3)
#所以dYpred/dh1=df(w5h1+w6h2+b3)/dh1，也就是f(w5h1+w6h2+b3)，对于h1求偏导
#这就是一个复合函数，先求外面的导，f'(w5h1+w6h2+b3)，再乘以里面的导，w5，所以=f'(w5h1+w6h2+b3)*w5
#同理，dh1/dw1 = df(w1x1+w2x2+b1)/dw1 = f'(w1x1+w2x2+b1)*x1，其中f'()是激活函数的导数
#总而言之，中心思想就是，把未知的，拆分为几个已知的，包括激活函数的导数，h1用f(w1x1+w2x2+b1)代替，L用(Ytrue-Ypred)^2代替
#Ypred实际上=o1=f(w5h1+w6h2+b3)，代替等等