import numpy as np
temps = np.array([22.5, 30.1, 28.8, 33.2, 26.0, 31.7])
hot = temps[temps>30]
print("平均: ",temps.mean())
print("超標的:",hot)
print("超標數量:",len(hot))
