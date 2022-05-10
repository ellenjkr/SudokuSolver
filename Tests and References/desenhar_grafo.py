import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
import matplotlib.gridspec as gridspec
from ideia_implementacao2 import *

# Inicializa o plot
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2, top=0.9)

G = nx.Graph()  # Inicializa o grafo


def submit_tamanho(tamanho):
    ax.clear()
    G.clear()
    fig.canvas.draw_idle()
    monta_grafo(int(tamanho), vertices)

    print(f'Tamanho do tabuleiro: {tamanho}x{tamanho}')


def submit_inicial(inicial):
    print(f'Vértice inicial: {inicial}')


def monta_grafo(T,vertices):
    ax.set_title(label=f"Tabuleiro {T}x{T}", fontsize=20, pad=15)

    # node_list = [x for x in range(1, T * T + 1, 1)]  # Vértices
    colors = ["red", "green",  "blue", "yellow", "orange", "purple", "cyan", "gray", "chartreuse", "darkslateblue", "sienna", "aquamarine", "deeppink", "lightpink", "peru", "y"]  # Cores

    cont = 0  # Contador para acessar o nome do vertice
    for i in range(T, 0, -1):  # T -> 0, decrementa
        for j in range(1, T + 1, 1):  # 1 -> T + 1, incrementa
            G.add_node(vertices[cont].id, pos=(j, i), node_color=colors[vertices[cont].cor -1])  # Adiciona o vértice ao grafo
            cont += 1

    pos = nx.get_node_attributes(G, 'pos')  # Obtém as posições


    # # Adiciona ligações
    # for i in range(1, T * T, T):
    #     if i < T * T - T + 1:
    #         G.add_edge(i, i + T)
    #     for j in range(i + 1, i + T, 1):
    #         if j < T * T - T + 1:
    #             G.add_edge(j, j + T)
    #         G.add_edge(i, j)

    matriz = []

    for i in range(1, T + 1, 1):
        linha = [j + T * i - T for j in range(1, T + 1, 1)]
        matriz.append(linha)
    
    for i in range(T):
        for j in range(T):
            valor_casa = matriz[i][j]

            vertices_linha = matriz[i].copy()
            vertices_linha.remove(valor_casa)

            vertices_coluna = [matriz[x][j] for x in range(T)]
            vertices_coluna.remove(valor_casa)

            vertices_conexao = vertices_linha + vertices_coluna
            for vertice in vertices_conexao:
                G.add_edge(valor_casa, vertice)
                # ax.annotate("",
                #     xy=pos[valor_casa], xycoords='data',
                #     xytext=pos[vertice], textcoords='data',
                #     arrowprops=dict(arrowstyle="->", color="0.5",
                #                     shrinkA=5, shrinkB=5,
                #                     patchA=None, patchB=None,
                #                     connectionstyle="arc3,rad=0.3",
                #                     ),
                #             )

    node_colors = nx.get_node_attributes(G, 'node_color')  # Obtém as cores
    nx.draw(G, pos, with_labels=False, arrows=False, node_color=list(node_colors.values()), node_size=600, ax=ax)  # Desenha o grafo
    labels = {}
    for node in G.nodes():
        labels[node] = str(vertices[node-1].cor)
    #print(labels)
    nx.draw_networkx_labels(G, pos, labels, ax=ax)


    # pos_aux = list(pos.values())
    # ax.annotate("",
    #                 xy=pos_aux[0], xycoords='data',
    #                 xytext=pos_aux[1], textcoords='data',
    #                 arrowprops=dict(arrowstyle="->", color="0.5",
    #                                 shrinkA=5, shrinkB=5,
    #                                 patchA=None, patchB=None,
    #                                 connectionstyle="arc3,rad=0.3",
    #                                 ),
    #                 )
    # plt.axis('off')

gs = gridspec.GridSpec(2, 1)
gs.update(left=0.5, right=0.6, bottom=0.05, top=0.15, hspace=0.3)

axes = [fig.add_subplot(gs[i, j]) for i, j in [[0, 0], [1, 0]]]

# create the textboxes
tamanho = TextBox(axes[0], 'Tamanho do tabuleiro', hovercolor='0.975', initial='4', label_pad=0.05)
inicial = TextBox(axes[1], 'Vértice inicial', hovercolor='0.975', initial='1', label_pad=0.05)

tamanho.on_submit(submit_tamanho)
inicial.on_submit(submit_inicial)

mngr = plt.get_current_fig_manager()
mngr.window.setGeometry(200, 100, 880, 600)


T = 9
tabuleiro = monta_tabuleiro(T)
vertices = cria_vertices(tabuleiro, T)
matriz = gera_matriz(vertices, T)
vertices = resolve_sudoku(matriz, vertices)
monta_grafo(T, vertices)
plt.show()  # Exibe o grafo
