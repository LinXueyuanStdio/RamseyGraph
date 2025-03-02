import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def plot_G_and_its_complement(G: nx.classes.graph.Graph, save_path="ramsey_graph.png"):
    """
    绘制图 G 和其补图
    :param G: 图 G
    :param save_path: 保存路径
    :return: None
    """
    # 生成图 G 的补图
    Gc = nx.complement(G)

    # 使用相同的布局，使两幅图的节点位置一致
    pos = nx.spring_layout(G, seed=482)

    # 为节点分配颜色，使用 Set2 调色板保证色彩丰富
    node_colors = plt.cm.Set2(np.linspace(0, 1, len(G.nodes)))

    # 定义边的颜色（年轻化的红和蓝）
    edge_color_G = "#FF6B6B"   # 充满活力的红色
    edge_color_Gc = "#4D79FF"  # 鲜明的蓝色

    # 创建画布，左右分别显示两个子图
    plt.figure(figsize=(14, 7))

    # 设置支持中文的字体
    plt.rcParams['font.sans-serif'] = ['Heiti SC']  # 或者使用 'Heiti SC'
    plt.rcParams['axes.unicode_minus'] = False  # 确保负号正常显示
    # 绘制图 G
    plt.subplot(1, 2, 1)
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500)
    nx.draw_networkx_edges(G, pos, edge_color=edge_color_G, width=2)
    nx.draw_networkx_labels(G, pos, font_size=16, font_color='black')
    plt.title("图 G", fontdict={'family': 'Heiti SC', 'size': 32})
    plt.axis('off')

    # 绘制图 G 的补图
    plt.subplot(1, 2, 2)
    nx.draw_networkx_nodes(Gc, pos, node_color=node_colors, node_size=500)
    nx.draw_networkx_edges(Gc, pos, edge_color=edge_color_Gc, width=2)
    nx.draw_networkx_labels(Gc, pos, font_size=16, font_color='black')
    plt.title("图 G 的补图", fontdict={'family': 'Heiti SC', 'size': 32})
    plt.axis('off')

    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()


# 创建图 G，添加节点和边
# G = nx.Graph()
# nodes = [1, 2, 3, 4, 5, 6, 7]
# G.add_nodes_from(nodes)
# # 添加一些边（边的选择确保补图中的边互补）
# G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 5), (5, 6), (6, 7), (2, 3)])

Gs = nx.read_graph6('raw_data/r44_6.g6')
G: nx.classes.graph.Graph = Gs[10]
plot_G_and_its_complement(G, save_path="ramsey_graph.png")
