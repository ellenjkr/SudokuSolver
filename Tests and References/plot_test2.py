import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox


def submit_tamanho(tamanho):
    print(f'Tamanho do tabuleiro: {tamanho}x{tamanho}')


def submit_inicial(inicial):
    print(f'Vértice inicial: {inicial}')


T = 4  # Tamanho do tabuleiro

G = nx.Graph()  # Inicializa o grafo

node_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  # Vértices
colors = ["red", "blue", "green", "yellow"]  # Cores
cont = 0  # Contador para acessar o nome do vertice
for i in range(T, 0, -1):  # T -> 0, decrementa
    for j in range(1, T + 1, 1):  # 1 -> T + 1, incrementa
        G.add_node(node_list[cont], pos=(j, i), node_color=colors[j - 1])  # Adiciona o vértice ao grafo
        cont += 1


dic = {x: '1' for x in node_list}
nx.set_node_attributes(G, dic, 'label')
G.nodes(data=True)

# Adiciona ligações
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(2, 1)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(3, 1)
G.add_edge(3, 2)
G.add_edge(3, 4)
G.add_edge(4, 1)
G.add_edge(4, 2)
G.add_edge(4, 3)

fig, axes = plt.subplots(3, 1, gridspec_kw={'height_ratios': [10, 1, 1]})
ax = axes.flatten()

pos = nx.get_node_attributes(G, 'pos')  # Obtém as posições
node_colors = nx.get_node_attributes(G, 'node_color')  # Obtém as cores
nx.draw(G, pos, with_labels=True, arrows=False, node_color=list(node_colors.values()), ax=ax[0])  # Desenha o grafo

tamanho = TextBox(ax[1], 'Tamanho do tabuleiro', initial=4, hovercolor='0.975', label_pad=0.1)
tamanho.on_submit(submit_tamanho)
inicial = TextBox(ax[2], 'Vértice inicial', hovercolor='0.975')
inicial.on_submit(submit_inicial)

plt.show()  # Exibe o grafo
