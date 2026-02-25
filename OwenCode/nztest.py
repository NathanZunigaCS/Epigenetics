import networkx as nx
import EoN

G = nx.erdos_renyi_graph(50, 0.1)
t, S, I = EoN.fast_SIS(G, tau=0.5, gamma=1.0)

print("Working.")