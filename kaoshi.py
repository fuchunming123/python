import numpy as np

def init():
    # 构建地图
    mapping_list = [[np.inf for i in range(0, 10)] for i in range(0, 10)]  # 构建全是无穷大的二维列表
    for i in range(0, 10):
        mapping_list[i][i] = 0  # 对角线处的值为0

    mapping_list[0][1] = 24
    mapping_list[0][2] = 8
    mapping_list[0][3] = 15
    mapping_list[1][4] = 6
    mapping_list[2][4] = 7
    mapping_list[2][5] = 3
    mapping_list[3][5] = 5
    mapping_list[3][6] = 4,
    mapping_list[4][5] = 2
    mapping_list[4][6] = 9
    mapping_list[5][6] = 10
    mapping_list[1][0] = 24
    mapping_list[2][0] = 8
    mapping_list[3][0] = 15
    mapping_list[4][1] = 6
    mapping_list[4][2] = 7
    mapping_list[5][2] = 3
    mapping_list[5][3] = 5
    mapping_list[6][3] = 4,
    mapping_list[5][4] = 2
    mapping_list[6][4] = 9
    mapping_list[6][5] = 10
    mapping_list[0][9] = 15
    mapping_list[1][7] = 23
    mapping_list[1][9] = 13
    mapping_list[6][8] = 19
    mapping_list[7][8] = 12
    mapping_list[9][0] = 15
    mapping_list[7][1] = 23
    mapping_list[9][1] = 13
    mapping_list[8][6] = 19
    mapping_list[8][7] = 12
    return mapping_list;

def greedy_optimal_path(matrix):
    m, n = matrix.shape
    path = [(0,0)]
    total_cost = matrix[0, 0]

    # 选择每次能够获得最大收益的路径进行扩展
    while path[-1] != (m-1, n-1):
        x, y = path[-1]
        if x == m-1:
            path.append((x, y+1))
        elif y == n-1:
            path.append((x+1, y))
        elif matrix[x+1, y] <= matrix[x, y+1]:
            path.append((x+1, y))
        else:
            path.append((x, y+1))

        total_cost += matrix[path[-1]]

    # 返回最终的最优路径长度
    return total_cost

if __name__ == "__main__":
    data = init()
    greedy_optimal_path(data)