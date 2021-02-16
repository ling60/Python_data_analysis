# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 19:29:56 2016

@author: liuling
"""

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

#G_fb = nx.read_edgelist("data/comp_edges.txt",
#                        create_using = nx.Graph(), nodetype = int)

edge_all = pd.read_csv('data/edges_0201_0430_316.csv', header=None)

dig = nx.DiGraph()
dig.add_weighted_edges_from(edge_all.values)

print(nx.info(dig))

#Create network layout for visualizations
#spring_pos = nx.spring_layout(dig)

#plt.axis("off")
nx.draw_networkx(dig, with_labels = False, node_size = 35)
plt.show()