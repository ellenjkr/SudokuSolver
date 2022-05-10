import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import TextBox
import matplotlib.gridspec as gridspec
import networkx as nx

fig, ax = plt.subplots()
ax.plot([1,3,2])

fig.subplots_adjust(bottom=0.4)
gs = gridspec.GridSpec(2,2)
gs.update(left=0.4, right=0.7, bottom=0.15, top=0.25, hspace=0.1)

axes = [fig.add_subplot(gs[i,j]) for i,j in [[0,0],[0,1],[1,0],[1,1]]]
# create the textboxes
tb_xmin = TextBox(axes[0],'x', hovercolor='0.975', label_pad=0.1)
tb_xmax = TextBox(axes[1],'',  hovercolor='0.975')
tb_ymin = TextBox(axes[2],'y', hovercolor='0.975', label_pad=0.1)
tb_ymax = TextBox(axes[3],'',  hovercolor='0.975')

def submit(val):
    data = eval(val)
    # how to know which limit to set here?
    ax.set_xlim(data)
    plt.draw()

for tb in [tb_xmin,tb_xmax,tb_ymin,tb_ymax]:
    tb.on_submit(submit)
plt.show()


# graphs = [nx.gnp_random_graph(20,0.3) for _ in range(2)]

# fig, axes = plt.subplots(nrows=2)
# ax = axes.flatten()

# for i in range(2):
#     nx.draw_networkx(graphs[i], ax=ax[i])
#     ax[i].set_axis_off()

# plt.show()