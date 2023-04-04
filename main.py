import matplotlib.pyplot as plt
import networkx as nx
import networkx.algorithms.community.quality as nxq
import networkx.algorithms.community.label_propagation as lp
from cdlib import algorithms, viz
import Functions as fct


def main():

    #plt.figure(figsize=(40, 35))
    fp = open('data/bundesliga_complete.txt', 'r')
    bundesliga = {}
    positions = {}
    graph_bundesliga_complete = nx.Graph()

    data = fct.read_data(fp)
    fp.close()

    fct.create_dict_vereine(bundesliga, data)
    fct.create_nodes(graph_bundesliga_complete, bundesliga)
    fct.add_edges_to_nodes(graph_bundesliga_complete, bundesliga)

    # analysing communities
    com = algorithms.louvain(graph_bundesliga_complete)
    print('Erkannte Communities - Louvain-Methode: ', len(com.communities), ' Modularity-Score = ', nxq.modularity(graph_bundesliga_complete, com.communities))

    #plot a graph
    pos = nx.spring_layout(graph_bundesliga_complete)  # set positions for nodes
    viz.plot_network_clusters(graph_bundesliga_complete, com, pos, figsize=(25, 20))
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

