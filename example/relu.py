from matplotlib import pyplot as plt
import numpy as np


def ShowReLU():
    x = np.linspace(-6, 6, 1000)
    y = np.where(x < 0, 0, x)
    plt.figure(figsize=(10, 10))
    plt.plot(x, y)
    plt.title('ReLU activation function')
    # plt.xlabel('Input')
    # plt.ylabel('Output')
    plt.legend(labels=[r'${ReLU}(x) = \max(0, x)$'])
    ax = plt.gca()
    ax.spines['right'].set_color('none') 
    ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
    # ax.xaxis.set_ticks_position('bottom')   
    # ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
    ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
    ax.spines['left'].set_position(('data', 0))
    plt.savefig('./img/relu.jpg', dpi=100, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    ShowReLU()
