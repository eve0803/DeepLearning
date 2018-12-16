# 画出散点图
import matplotlib.pyplot as plt

dataset = [[1.2, 1.1], [2.4, 3.5], [4.1, 3.2], [3.4, 2.8], [5, 5.4]]

# 列表推导式
x = [row[0] for row in dataset]
y = [row[1] for row in dataset]

# 绘图的坐标范围 red dashes, blue squares and green triangles
plt.axis([0, 6, 0, 6])
plt.plot(x,y,'bx')
#plt.show()
plt.grid()
plt.savefig('scatter.jpg')