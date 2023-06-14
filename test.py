import networkx as nx
import matplotlib.pyplot as plt
from cdlib import viz

def main():
    fp = open('data/algorithms_overview.txt', 'r')
    zeilen = fp.readlines()
    list_zeilen = []
    
    for zeile in zeilen:
        tmp = zeile.strip()
        list_zeile = tmp.split()  # maxsplit=1
        
        list_zeilen.append(list_zeile)

    print(list_zeilen)

    a = nx.Graph()

    for zeile1 in list_zeilen:
        for zeile2 in list_zeilen:
            for word in zeile1:
                for word2 in zeile2:
                    if (word == word2):
                        a.add_edge(zeile1[0], zeile2[0])

    pos = nx.spring_layout(a)
    nx.draw(a, pos)
    plt.show()
