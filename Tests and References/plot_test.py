import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()

G.add_edges_from(
    [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])

# val_map = {1: 1.0,
#            2: 0.5714285714285714,
#            3: 0.0}

# values = [val_map.get(node, 0.25) for node in G.nodes()]

# black_edges = [edge for edge in G.edges()]


print(G)

indices = [(0, 0), (0, 1), (1, 0), (1, 1)]
valores = [1, 2, 3, 4]
pos = dict(zip(valores, indices))
nx.draw_networkx(G, pos=pos, with_labels=True, node_size=200)

# pos = nx.spring_layout(G)
# nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
#                        node_color = values, node_size = 500)

# nx.draw_networkx_labels(G, pos)
# nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
plt.show()


# ============================================================================
# # import networkx as nx
# # import matplotlib.pyplot as plt


# N = 3
# G = nx.grid_2d_graph(N, N)
# pos = dict((n, n) for n in G.nodes())
# labels = dict( ((i,j), i + (N - 1 - j) * N ) for i, j in G.nodes())
# nx.relabel_nodes(G, labels, False)
# inds = list(labels.keys())
# vals = list(labels.values())
# print(inds)
# print(vals)
# inds.sort()
# vals.sort()
# pos2 = dict(zip(vals,inds))
# print(pos2)
# plt.figure()
# nx.draw_networkx(G, pos=pos2, with_labels=True, node_size = 200)

# # plt.show()

# ============================================================================
# import networkx as nx
# import matplotlib.pylab as pl

# G = nx.Graph()

# G.add_node("s", level=0)
# G.add_node("t_1", level=1)
# G.add_node("t_2", level=1)
# G.add_node("v_1", level=2)
# G.add_node("v_2", level=2)
# G.add_node("v_3", level=2)
# G.add_node("t", level=3)

# pos = nx.multipartite_layout(G, subset_key="level")

# nx.draw(G, pos, with_labels=True)
# pl.show()