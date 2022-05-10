# import matplotlib.pylab as plt
# import networkx as nx

# # plt.rcParams["figure.figsize"] = [7.50, 3.50]
# # plt.rcParams["figure.autolayout"] = True

# G = nx.DiGraph()

# # pos = nx.spring_layout(G)
# G.add_nodes_from([1, 2, 3, 4])
# G.add_edges_from([(1, 2), (2, 4), (2, 3), (4, 1)])

# nx.draw(G, with_labels=True, connectionstyle="arc3,rad=0.4")

# plt.show()

# =========================================
# T = 4

# matriz = []

# for i in range(1, T + 1, 1):
# 	linha = [j + T * i - T for j in range(1, T + 1, 1)]
# 	matriz.append(linha)

# # casa_linha = 0
# # casa_coluna = 0
# # valor_casa = matriz[casa_linha][casa_coluna]

# # lista_casa = [valor_casa] * (T - 1)
# # vertices_linha = matriz[casa_linha].copy()

# # vertices_linha.remove(valor_casa)

# # for a in zip(lista_casa, vertices_linha):
# # 	print(a)

# for i in range(T):
# 	for j in range(T):
# 		valor_casa = matriz[i][j]
# 		conexoes = [valor_casa] * (T * 2 - 2)  # Para linha e coluna, removendo ele mesmo

# 		vertices_linha = matriz[i].copy()
# 		vertices_linha.remove(valor_casa)

# 		vertices_coluna = [matriz[x][j] for x in range(T)]
# 		vertices_coluna.remove(valor_casa)

# 		vertices = vertices_linha + vertices_coluna
# 		for a in zip(conexoes, vertices):
# 			print(a)


# ==============================================
import networkx as nx
from matplotlib import pyplot as plt

G = nx.Graph()
G.add_node(1, pos=(0, 1))
G.add_node(2, pos=(0, 2))
G.add_node(3, pos=(0, 3))
G.add_node(4, pos=(0, 4))
G.add_node(5, pos=(1, 1))
G.add_node(6, pos=(1, 2))
G.add_node(7, pos=(1, 3))
G.add_node(8, pos=(1, 4))


labels = {1: '1', 2: '2', 3: '3', 4: '3', 5: '3', 6: '3', 7: '3', 8: '3'}

pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, with_labels=False, pos=pos)
nx.draw_networkx_labels(G, pos, labels)

plt.show()