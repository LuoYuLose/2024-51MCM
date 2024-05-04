import networkx as nx
import matplotlib.pyplot as plt

# 创建有向图
G = nx.DiGraph()

# 添加节点
nodes = {
    'A': (20, 75),  # 顶部第一个圆的中心
    'B': (45, 75),
    'C': (70, 75),
    'D': (95, 75),
    'E': (70, 40),  # 椭圆中心
    'Start': (0, 80),  # 起始点，外部边缘的左上角
    'End': (100, 80)   # 结束点，外部边缘的右上角
}

# 将节点添加到图中
for node, pos in nodes.items():
    G.add_node(node, pos=pos)

edges = [
    ('Start', 'A'), ('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'End'),  # 上部边缘的切割
    ('A', 'E'), ('B', 'E'), ('C', 'E'), ('D', 'E')  # 从每个圆到椭圆的连接
]

# 标记特殊的空程边
air_travels = [('Start', 'A'), ('D', 'End')]

# 添加边到图中
for edge in edges:
    G.add_edge(*edge, weight=1)  # 简化示例，权重设为1

# 绘制图
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=9, font_weight='bold')
nx.draw_networkx_edges(G, pos, edgelist=air_travels, edge_color='red', style='dashed')
plt.savefig('./N2Simple.png')
