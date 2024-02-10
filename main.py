import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

data = pd.read_csv('airports.csv')
G = nx.from_pandas_edgelist(data, source='Origin', target='Dest', edge_attr=True)

def attribute_for_nodes(G, attribute, default_value):
    for g in G.nodes.keys():
        G.nodes[g][attribute] = default_value
print(G.edges['IAD', 'TPA'])
print(data.head())
print(data.columns)  
plt.figure()
nx.draw_networkx(G, with_labels=True)
plt.show()