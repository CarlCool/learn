'''
neural networtk
'''
import numpy as np
import matplotlib.pylab as plt

# a = np.array([1,2,3])  
# print(a)
# input should be np.array
def step_function(x):
    # if(x>0):
    #     return 1
    # else:
    #     return 0
    #适用numPy 实现 一上代码
    y = x > 0
    return y.astype(np.int)
# print(step_function(np.array(3.0)))
# x = np.arange(-0.5,0.5,0.1)
# y = step_function(x)
# plt.plot(x, y)
# # plt.ylim(-0.1,1.1)
# plt.show()


# sigmoid 函数
def sigmoid(x):
    return 1/(1+np.exp(-x))
    # return 1/(1+2.718**(-x))

# x = np.array([0.1,1.0,3.0])
# print(sigmoid(x))
# x = np.arange(-5,5,0.1)
# y = sigmoid(x)
# plt.plot(x,y)
# plt.ylim(-0.1,1.1)
# plt.show()


# relu 函数
def relu(x):
    return np.maximum(0,x)
# x = np.arange(-5.0,5.0,0.1)
# y = relu(x)
# plt.plot(x,y)
# plt.ylim(-0.1,5)
# plt.show()

# softmax 函数 和=1
def softmax(a):
    max_a = np.max(a)    #防止溢出
    exp_a = np.exp(a - max_a)
    exp_sum = np.sum(exp_a)
    y = exp_a/exp_sum
    return y

# print(softmax(np.array([3001,3002,3003])))

x = np.array([[[0.1,0.8,0.1],[0.3,0.1,0.6]],[[0.2,0.5,0.3],[0.8,0.1,0.1]]])
# y = np.argmax(x,axis = 1)
print(x.ndim)
