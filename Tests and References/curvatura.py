# https://stackoverflow.com/questions/60464285/curved-edges-using-matplotlib-and-networkx-in-python-3-x

import networkx as nx

from matplotlib import pyplot as plt
G = nx.DiGraph()
G.add_node(0, pos=(0, 1))
G.add_node(1, pos=(0, 2))

pos = nx.get_node_attributes(G, 'pos')

# pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G, pos)

ax = plt.gca()
ax.annotate("",
                xy=pos[0], xycoords='data',
                xytext=pos[1], textcoords='data',
                arrowprops=dict(arrowstyle="->", color="0.5",
                                shrinkA=5, shrinkB=5,
                                patchA=None, patchB=None,
                                connectionstyle="arc3,rad=0.3",
                                ),
                )
plt.axis('off')
plt.show()