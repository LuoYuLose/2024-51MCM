import networkx as nx
import matplotlib.pyplot as plt
import math

# 定义函数：计算矩形中心坐标
def calculate_positions(rows, cols, rect_width, rect_height, spacing):
    positions = {}
    x_offset = rect_width / 2
    y_offset = rect_height / 2
    for row in range(rows):
        for col in range(cols):
            x = col * (rect_width + spacing) + x_offset
            y = row * (rect_height + spacing) + y_offset
            positions[f"R{row * cols + col + 1}"] = (x, y)
    return positions

# 定义函数：创建图并添加边和权重
def create_graph(positions):
    G = nx.Graph()
    nodes = list(positions.keys())
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            p1, p2 = positions[nodes[i]], positions[nodes[j]]
            distance = math.hypot(p2[0] - p1[0], p2[1] - p1[1])
            G.add_edge(nodes[i], nodes[j], weight=distance)
    return G

# 定义函数：可视化图和路径
def plot_graph(G, path, positions):
    plt.figure(figsize=(12, 10))
    nx.draw(G, pos=positions, with_labels=True, node_color='orange', node_size=500)
    path_edges = list(zip(path[:-1], path[1:]))
    nx.draw_networkx_edges(G, positions, edgelist=path_edges, edge_color='red', width=2)
    plt.title("Hamiltonian Path for Rectangles")
    plt.show()

# 矩形和布局参数
rect_width = 4
rect_height = 3
spacing = 2
rows = 3
cols = 4

# 计算位置
positions = calculate_positions(rows, cols, rect_width, rect_height, spacing)

# 创建图
G = create_graph(positions)

try:
    path = list(nx.approximation.traveling_salesman_problem(G, weight='weight'))
except AttributeError:
    print("Traveling Salesman Problem solver is not available in this version of NetworkX.")
    path = list(positions.keys()) + [list(positions.keys())[0]]

# 输出路径
print("Path:", path)

# 可视化图和路径
plot_graph(G, path, positions)
