#!/usr/bin/env python
"""
Draw a graph with matplotlib.
You must have matplotlib for this to work.
"""

__author__ = """Alejandro Alcalde (algui91@gmail.com)"""

try:
        import matplotlib.pyplot as plt
except:
        raise

import networkx as nx

G = nx.Graph()

G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,3), (3,4), (3,5), (4,2), (5,2)])

#nx.spring_layout(G)
#nx.draw_networkx(G)
# explicitly set positions
pos={1:(.4,3),
     2:(1.4,3),
     3:(.6,3),
     4:(1,3.1),
     5:(1,2.9)}
labels={1:"1",
		2:"2",
		3:"3",
		4:"4",
		5:"5"}


#nx.draw_networkx(G,pos)   
nx.draw_networkx_nodes(G,pos,node_size=2000)
nx.draw_networkx_nodes(G,pos,node_size=3000,node_color='r')
nx.draw_networkx_edges(G,pos,alpha=0.5,width=6)
nx.draw_networkx_labels(G,pos,labels=labels)
plt.axis('off')
plt.savefig("house_with_colors.png") # save as png
plt.show() # display
