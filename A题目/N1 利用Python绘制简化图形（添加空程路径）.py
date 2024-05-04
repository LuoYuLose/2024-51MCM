import matplotlib.pyplot as plt
import networkx as nx

# 创建图对象
G = nx.DiGraph()

# 添加节点
nodes = ['B1', 'B2', 'B3', 'B4', 'A1', 'A2', 'A3', 'A4']
positions = {
    'B1': (1, 0), 'B2': (1, 1), 'B3': (0, 1),
    'B4': (0, 0), 'A4': (0.3, 0.3), 'A1': (0.7, 0.3),
    'A2': (0.7, 0.7), 'A3': (0.3, 0.7)
}
G.add_nodes_from(nodes)

# 添加边
edges = [
    ('B1', 'B2'), ('B2', 'B3'), ('B4', 'B1'),  # 切割路径
    ('A4', 'A1'), ('A1', 'A2'), ('A2', 'A3'), ('A3', 'A4'),  # 切割路径
    ('B3', 'A3'), ('A3', 'B4')  # 空程路径
]
G.add_edges_from(edges)

# 绘制图
plt.figure(figsize=(8, 8))
nx.draw(G, pos=positions, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15, font_weight='bold')
nx.draw_networkx_edges(G, pos=positions, edgelist=[('B3', 'A3'), ('A3', 'B4')], edge_color='red', style='dashed')
plt.title("Illustration of the Optimal Path with Minimal Air Travel")
plt.savefig('./After.png')
