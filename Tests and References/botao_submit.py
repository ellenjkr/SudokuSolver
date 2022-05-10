# import networkx as nx
# import matplotlib.pyplot as plt

# # for i in range(2):
# G = nx.DiGraph()
# G.add_edge("A", "B")
# nx.draw(G)
# plt.show()
# G.clear()


# G = nx.DiGraph()
# G.add_edge("A", "C")
# G.add_edge("A", "D")

# nx.draw(G)
# plt.draw()
# plt.close()
# G.clear()

# ============================================

# import matplotlib.pyplot as plt
# from matplotlib.widgets import TextBox
# import matplotlib.gridspec as gridspec

# fig, ax = plt.subplots()
# ax.plot([1,3,2])

# fig.subplots_adjust(bottom=0.4)
# gs = gridspec.GridSpec(2,2)
# gs.update(left=0.4, right=0.7, bottom=0.15, top=0.25, hspace=0.1)

# axes = [fig.add_subplot(gs[i,j]) for i,j in [[0,0],[0,1],[1,0],[1,1]]]
# # create the textboxes
# xlim = ax.get_xlim()
# ylim = ax.get_ylim()
# tb_xmin = TextBox(axes[0],'x', initial = str(xlim[0]), hovercolor='0.975', label_pad=0.1)
# tb_xmax = TextBox(axes[1],'',  initial = str(xlim[1]), hovercolor='0.975')
# tb_ymin = TextBox(axes[2],'y', initial = str(ylim[0]), hovercolor='0.975', label_pad=0.1)
# tb_ymax = TextBox(axes[3],'',  initial = str(ylim[1]), hovercolor='0.975')

# def submit(val):
#     lim = [float(tb.text) for tb in [tb_xmin,tb_xmax,tb_ymin,tb_ymax]]
#     ax.axis(lim)
#     fig.canvas.draw_idle()

# for tb in [tb_xmin,tb_xmax,tb_ymin,tb_ymax]:
#     tb.on_submit(submit)
# plt.show()

import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button
# Create figure
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
# I used pandas to read data from a csv file
# but in this case I will just use dummy values as example
X = [];Y1 = [];Y2 = [];Y3 = []
for i in range(10):
    X.append(i)
    Y1.append(i)
    Y2.append(i*2)
    Y3.append(i**2)
# Plot the data
ax.plot(X,Y1,X,Y2,X,Y3)
# Handles submit button
def submit(event):
    print("yes")
    print("x =", x_textbox.text)
    print("y =", y_textbox.text)
    x = int(x_textbox.text)
    y = y_textbox.text
    X = [];Y1 = [];Y2 = [];Y3 = []
    if x not in ["", None]:
        for i in range(x):
            X.append(i)
            Y1.append(i-1)
            Y2.append(i*3)
            Y3.append(i**3)
        #fig.pop(0)
        ax.lines.pop(0)
        ax.lines.pop(0)
        ax.lines.pop(0)
        ax.plot(X,Y1,X,Y2,X,Y3)
# Text box to input x value
axbox1 = fig.add_axes([0.1, 0.1, 0.5, 0.05])
x_textbox = TextBox(axbox1, "New X")
# Text box to input y value
axbox2 = fig.add_axes([0.1, 0.05, 0.5, 0.05])
y_textbox = TextBox(axbox2, "New Y")
# Submit button
axbox3 = fig.add_axes([0.81, 0.05, 0.1, 0.075])
submit_button = Button(axbox3, "Submit!")
submit_button.on_clicked(submit)
plt.show()