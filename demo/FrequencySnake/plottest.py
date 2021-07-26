import matplotlib.pyplot as plt
import numpy as np

def tolerance(x, bounds=(0.0, 0.0), margin=0.0, sigmoid='gaussian',
              value_at_margin=0.1):
    lower, upper = bounds
    in_bounds = np.logical_and(lower <= x, x <= upper)
    d = np.where(x < lower, lower - x, x - upper) / margin
    value = np.where(in_bounds, 1.0, _sigmoids(d, value_at_margin, sigmoid))
    return float(value) if np.isscalar(x) else value

def _sigmoids(x, value_at_1, sigmoid):
    if sigmoid == 'gaussian':
        scale = np.sqrt(-2 * np.log(value_at_1))
        return np.exp(-0.5 * (x*scale)**2)

x = np.linspace(-1, 1, 100000) # 从0到1，等分50分
y1 = tolerance(x, bounds=(0.2, 0.2), margin=0.4, sigmoid='gaussian', value_at_margin=0.1) * 10
# y2 = tolerance(x, bounds=(0.3, 0.32), margin=0.15, sigmoid='gaussian', value_at_margin=0.1) *20
y = y1 - 9
# y = pow(1 - abs(x - 0.2)/0.2, 5)
# y = (1 - x) ** 2.10000
plt.figure() # 定义一个图像窗口
plt.plot(x, y) # 绘制曲线 y

plt.show()
