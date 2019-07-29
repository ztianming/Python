import numpy as np

# 计算两个向量的叉乘
def calculationVectorCross(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]

# 计算多边形的面积，支持非凸情况
def calculationPolygonArea(polygon):
    """
    :param polygon: 多边形顶点，已经进行顺次逆时针排序
    :return: 该多边形的面积
    """
    n = len(polygon)
    if n < 3:
        return 0
    vectors = np.zeros((n, 2))
    for i in range(0, n):
        vectors[i, :] = polygon[i, :] - polygon[0, :]
    area = 0
    for i in range(1, n):
        area = area + calculationVectorCross(vectors[i - 1, :], vectors[i, :]) / 2
    return int(area)
# n coordinates
n = int(input())
l = []
for i in range(n):
    # 按顺时针（逆时针）方向输入坐标
    x, y = [int(j) for j in input().split()]
    temp = []
    temp.append(x)
    temp.append(y)
    l.append(temp)
# print(l)
print(calculationPolygonArea(np.array(l)))