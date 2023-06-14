import matplotlib.pyplot as plt
import networkx as nx
import networkx.algorithms.community.quality as nxq
import networkx.algorithms.community.label_propagation as lp
from cdlib import algorithms, viz, evaluation, benchmark
import Functions as fct
import test as tst


def main():

    #plt.figure(figsize=(40, 35))
    fp = open('data/bundesliga_complete.txt', 'r')
    bundesliga = {}
    positions = {}
    graph_bundesliga_complete = nx.Graph()
    worldmap = fct.worldmap()

    data = fct.read_data(fp)
    fp.close()

    fct.create_dict_vereine(bundesliga, data)
    fct.create_nodes(graph_bundesliga_complete, bundesliga)
    fct.add_edges_to_nodes(graph_bundesliga_complete, bundesliga)

    # analysing communities
    com = algorithms.girvan_newman(worldmap, 8)
    print('Erkannte Communities - Louvain-Methode: ', len(com.communities), ' Modularity-Score = ', nxq.modularity(worldmap, com.communities))

    # benchmark.GRP()
    # fitness score
    scd = evaluation.avg_distance(worldmap, com)
    scd2 = evaluation.size(worldmap, com)
    scd3 = evaluation.internal_edge_density(worldmap, com)
    scd4 = evaluation.link_modularity(worldmap, com)
    #print(scd)
    #print(scd2)
    #print(scd3)
    print(scd4)

    # plot a graph
    pos = nx.spring_layout(worldmap)  # set positions for nodes
    viz.plot_network_clusters(worldmap, com, pos, figsize=(25, 20))
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tst.main()

