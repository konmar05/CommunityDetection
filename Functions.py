from Vereine import *
import Colors as c
import numpy as np
import networkx as nx


def read_data(filepointer):
    """
    @description: reads txt-file and returns a nested list in following form: file = [line1=[], line2=[], ...]
    @parameter: filepointer
    @return: liste = [zeile1=[], zeile2=[], ...]
    """

    zeilen = filepointer.readlines()
    list_zeilen = []

    for zeile in zeilen:
        tmp = zeile.rstrip()
        list_zeile = tmp.split('#')

        for i in range(len(list_zeile)):
            if list_zeile[i].isdigit():
                list_zeile[i] = int(list_zeile[i])

        list_zeilen.append(list_zeile)

    return list_zeilen


def read_data_verein(filepointer, verein):
    zeilen = filepointer.readlines()
    list_zeilen = []

    for zeile in zeilen:
        tmp = zeile.rstrip()
        list_zeile = tmp.split('#')

        for i in range(len(list_zeile)):
            if list_zeile[i].isdigit():
                list_zeile[i] = int(list_zeile[i])

        if verein == list_zeile[1]:
            list_zeilen.append(list_zeile)

    return list_zeilen


def create_dict_vereine(dict_to_write, list_to_read):
    """
    @description: creates and adds a new dictionary = {year:'club'} for each player in given league-dictionary
    @:parameter: dictionary, list
    """

    for line in list_to_read:
        dict_to_write[line[0]] = Vereine(line)


def create_nodes(graph, dictionary):
    """
    @description: iterates trough dictionary and adds every key:value pair to the graph
    @parameter: dictionary, graph
    """

    id_for_node = 1
    for player, clubs in dictionary.items():
        graph.add_node(id_for_node, name=player)
        id_for_node = id_for_node+1


def add_edges_till2023(graph, dictionary):
    knoten = graph.number_of_nodes()
    for i in range(1, knoten + 1):
        for j in range(1, knoten + 1):

            if (graph._node[i] == graph._node[j]):
                break
            spieler1 = graph._node[i].get('name')
            spieler2 = graph._node[j].get('name')
            vereine1 = dictionary[spieler1]
            vereine2 = dictionary[spieler2]
            for jahr1, club1 in vereine1.vereine.items():
                for jahr2, club2 in vereine2.vereine.items():


                    '''
                    if club2 == club1 and club1 != 'FC Bayern München' and club2 != 'FC Bayern München':
                        graph.add_edge(i, j)
                    '''
                    if (club1 != 'FC Bayern München' or club2 != 'FC Bayern München'):
                        if (jahr1 == jahr2):
                            if (club1 == club2):
                                if (graph.has_edge(i, j)):
                                    break
                                else:
                                    graph.add_edge(i, j)



def add_edges_to_nodes(graph, dictionary):
    """
    @description: add edges to the nodes from players how played in the same year in the same club
    @parameter: graph, dictionary from which the graph was created
    """

    knoten = graph.number_of_nodes()
    for i in range(1, knoten+1):
        for j in range(1, knoten+1):

            if (graph._node[i] == graph._node[j]):
                break
            spieler1 = graph._node[i].get('name')
            spieler2 = graph._node[j].get('name')
            vereine1 = dictionary[spieler1]
            vereine2 = dictionary[spieler2]
            for jahr1, club1 in vereine1.vereine.items():
                for jahr2, club2 in vereine2.vereine.items():
                    if (jahr1 == jahr2):
                        if (club1 == club2):
                            if (graph.has_edge(i, j)):
                                break
                            else:
                                graph.add_edge(i, j)


def color_nodes(graph, list_communities):
    """
    @description: coloring nodes according to communities
    @:parameter:graph, list_communities liste[set{}, set{}, ...]
    @return: color_map[] for use in nx.draw()
    """

    color_map = []

    for player in graph:
        if player in list_communities[0]:
            color_map.append(c.Blue)
        elif player in list_communities[1]:
            color_map.append(c.Brown)
        elif player in list_communities[2]:
            color_map.append(c.Green)
        elif player in list_communities[3]:
            color_map.append(c.DarkOrange)
        elif player in list_communities[4]:
            color_map.append(c.Red)
        elif player in list_communities[5]:
            color_map.append(c.Purple)
        elif player in list_communities[6]:
            color_map.append(c.Yellow)
        elif player in list_communities[7]:
            color_map.append(c.CornflowerBlue)
        elif player in list_communities[8]:
            color_map.append(c.RosyBrown)
        elif player in list_communities[9]:
            color_map.append(c.Khaki)
        elif player in list_communities[10]:
            color_map.append(c.Coral)
        elif player in list_communities[11]:
            color_map.append(c.OrangeRed)
        elif player in list_communities[12]:
            color_map.append(c.Magenta)
        elif player in list_communities[12]:
            color_map.append(c.Gold)
        elif player in list_communities[13]:
            color_map.append(c.DarkCyan)
        elif player in list_communities[14]:
            color_map.append(c.Peru)
        elif player in list_communities[15]:
            color_map.append(c.ForestGreen)
        elif player in list_communities[16]:
            color_map.append(c.Sienna1)
        elif player in list_communities[17]:
            color_map.append(c.MediumVioletRed)
        elif player in list_communities[18]:
            color_map.append(c.Orchid)
        elif player in list_communities[19]:
            color_map.append(c.LightGoldenrod1)
        elif player in list_communities[20]:
            color_map.append(c.Aquamarine)
        elif player in list_communities[21]:
            color_map.append(c.LimeGreen)
        elif player in list_communities[22]:
            color_map.append(c.LightCoral)
        elif player in list_communities[23]:
            color_map.append(c.Violet)
        elif player in list_communities[24]:
            color_map.append(c.DeepPink)
        elif player in list_communities[25]:
            color_map.append(c.GreenYellow)
        elif player in list_communities[26]:
            color_map.append(c.NavyBlue)
        elif player in list_communities[27]:
            color_map.append(c.tan1)
        elif player in list_communities[28]:
            color_map.append(c.LightSlateGray)
        elif player in list_communities[29]:
            color_map.append(c.Cyan2)
        elif player in list_communities[30]:
            color_map.append(c.MediumSeaGreen)
        elif player in list_communities[31]:
            color_map.append(c.Firebrick3)
        elif player in list_communities[32]:
            color_map.append(c.MediumPurple)

    return color_map


def random_walk(graph, start_node, number_of_steps):
    """
    @description: implementing the Random Walk Detection Algorithm
    @parameter: graph, start_node, steps
    @return: list = [{nodeset}, {nodeset}, ...]
    """

    visit_counts = {}
    current_node = start_node
    for i in range(number_of_steps):
        neighbors = list(graph.neighbors(current_node))
        if len(neighbors) == 0:
            current_node = start_node
        else:
            current_node = np.random.choice(neighbors)
        if current_node not in visit_counts:
            visit_counts[current_node] = 1
        else:
            visit_counts[current_node] += 1

    # result for return
    communities = {}
    for node, count in visit_counts.items():
        if count not in communities:
            communities[count] = [node]
        else:
            communities[count].append(node)

    ret = []
    for key, value in communities.items():
        ret.append(set(value))
    return ret  # communities  # visit_counts


def bundesliga_small():
    """
    @description: creates a small graph with 35 players
    @paramoter: none
    @return: new instance from class Graph in networkx, fully implemented with nodes an edges
    """

    bundesliga = nx.Graph()

    bundesliga.add_node(1, name='Reece Oxford', club='FC Augsburg', y2013='West Ham United FC', y2014='West Ham United FC', y2015='West Ham United FC', y2016='West Ham United FC', y2017='Borussia Mönchengladbach', y2018='West Ham United FC', y2019='FC Augsburg', y2020='FC Augsburg', y2021='FC Augsburg', y2022='FC Augsburg')
    bundesliga.add_node(2, name='Thomas Meunier', club='Borussia Dortmund', y2013='Club Brügge', y2014='Club Brügge', y2015='Club Brügge', y2016='Paris Saint-Germain FC', y2017='Paris Saint-Germain FC', y2018='Paris Saint-Germain FC', y2019='Paris Saint-Germain FC', y2020='Borussia Dortmund', y2021='Borussia Dortmund', y2022='Borussia Dortmund')
    bundesliga.add_node(3, name='Yann Sommer', club='FC Bayern München',y2013='FC Basel', y2014='Borussia Mönchengladbach', y2015='Borussia Mönchengladbach', y2016='Borussia Mönchengladbach', y2017='Borussia Mönchengladbach', y2018='Borussia Mönchengladbach', y2019='Borussia Mönchengladbach', y2020='Borussia Mönchengladbach', y2021='Borussia Mönchengladbach', y2022='Borussia Mönchengladbach')
    bundesliga.add_node(4, name='Johannes Schenk', club='FC Bayern München')
    bundesliga.add_node(5, name='Kelvin Yeboah', club='FC Augsburg', y2017='AC Gozzano',y2018='WSG Wattens', y2019='WSG Swarovski Tirol', y2020='WSG Swarovski Tirol', y2021='SK Puntigamer Sturm Graz', y2022='Genua CFC 1893')
    bundesliga.add_node(6, name='Lars Stindl', club='Borussia Mönchengladbach', y2013='Hannover 96', y2014='Hannover 96', y2015='Borussia Mönchengladbach', y2016='Borussia Mönchengladbach', y2017='Borussia Mönchengladbach',y2018='Borussia Mönchengladbach',y2019='Borussia Mönchengladbach',y2020='Borussia Mönchengladbach',y2021='Borussia Mönchengladbach',y2022='Borussia Mönchengladbach')
    bundesliga.add_node(7, name='Sadio Mané', club='FC Bayern München', y2013='FC Red Bull Salzburg', y2014='Southampton FC', y2015='Southampton FC', y2016='Liverpool FC', y2017='Liverpool FC', y2018='Liverpool FC', y2019='Liverpool FC', y2020='Liverpool FC', y2021='Liverpool FC', y2022='FC Bayern München')
    bundesliga.add_node(8, name='Josip Stanišić', club='FC Bayern München')
    bundesliga.add_node(9, name='Irvin Cardona', club='FC Augsburg', y2013='AS Monaco', y2014='AS Monaco', y2015='AS Monaco', y2016='AS Monaco', y2017='Cercle Brügge KSV', y2018='Cercle Brügge KSV', y2019='Stade Brestois', y2020='Stade Brestois', y2021='Stade Brestois', y2022='Stade Brestois')
    bundesliga.add_node(10, name='Marcus Thuram', club='Borussia Mönchengladbach', y2013='FC Sochaux', y2014='FC Sochaux', y2015='FC Sochaux', y2016='FC Sochaux', y2017='En Avant de Guingamp', y2018='En Avant de Guingamp', y2019='Borussia Mönchengladbach', y2020='Borussia Mönchengladbach', y2021='Borussia Mönchengladbach', y2022='Borussia Mönchengladbach')
    bundesliga.add_node(11, name='Florian Müller', club='VfB Stuttgart', y2013='1. FSV Mainz 05', y2014='1. FSV Mainz 05', y2015='1. FSV Mainz 05', y2016='1. FSV Mainz 05', y2017='1. FSV Mainz 05', y2018='1. FSV Mainz 05', y2019='1. FSV Mainz 05', y2020='1. FSV Mainz 05', y2021='VfB Stuttgart', y2022='VfB Stuttgart')
    bundesliga.add_node(12, name='Iago', club='FC Augsburg', y2013='SC Internacional', y2014='SC Internacional', y2015='SC Internacional', y2016='SC Internacional', y2017='SC Internacional', y2018='SC Internacional', y2019='FC Augsburg', y2020='FC Augsburg', y2021='FC Augsburg', y2022='FC Augsburg')
    bundesliga.add_node(13, name='Nico Elvedi', club='Borussia Mönchengladbach', y2013='FC Zürich', y2014='FC Zürich', y2015='Borussia Mönchengladbach', y2016='Borussia Mönchengladbach', y2017='Borussia Mönchengladbach', y2018='Borussia Mönchengladbach', y2019='Borussia Mönchengladbach', y2020='Borussia Mönchengladbach', y2021='Borussia Mönchengladbach', y2022='Borussia Mönchengladbach')
    bundesliga.add_node(14, name='Lucas Hernández', club='FC Bayern München', y2013='Atletico Madrid', y2014='Atletico Madrid', y2015='Atletico Madrid', y2016='Atletico Madrid', y2017='Atletico Madrid', y2018='Atletico Madrid', y2019='FC Bayern München', y2020='FC Bayern München', y2021='FC Bayern München', y2022='FC Bayern München')
    bundesliga.add_node(15, name='Marius Wolf', club='Borussia Dortmund', y2013='TSV 1860 München', y2014='TSV 1860 München', y2015='TSV 1860 München', y2016='Hannover 96', y2017='Eintracht Frankfurt', y2018='Borussia Dortmund', y2019='Hertha BSC Berlin', y2020='Borussia Dortmund', y2021='1. FC Köln', y2022='Borussia Dortmund')
    bundesliga.add_node(16, name='Konstantinos Mavropanos', club='VfB Stuttgart', y2013='Apollon Smyrnis', y2014='Apollon Smyrnis', y2015='Apollon Smyrnis', y2016='PAS Giannina FC', y2017='PAS Giannina FC', y2018='Arsenal FC', y2019='Arsenal FC', y2020='1. FC Nürnberg', y2021='VfB Stuttgart', y2022='VfB Stuttgart')
    bundesliga.add_node(17, name='Joshua Kimmich', club='FC Bayern München', y2013='RB Leipzig', y2014='RB Leipzig', y2015='FC Bayern München', y2016='FC Bayern München', y2017='FC Bayern München', y2018='FC Bayern München', y2019='FC Bayern München', y2020='FC Bayern München', y2021='FC Bayern München', y2022='FC Bayern München')
    bundesliga.add_node(18, name='Benjamin Leneis', club='FC Augsburg', y2014='1. FC Nürnberg', y2015='FC Augsburg', y2016='FC Augsburg', y2017='FC Augsburg', y2018='FC Augsburg', y2019='FC Augsburg', y2020='FC Augsburg', y2021='1. FC Magdeburg', y2022='FC Augsburg')
    bundesliga.add_node(19, name='Conor Noß', club='Borussia Mönchengladbach', y2013='Borussia Mönchengladbach', y2014='Borussia Mönchengladbach', y2015='Borussia Mönchengladbach', y2016='Borussia Mönchengladbach', y2017='Borussia Mönchengladbach', y2018='Borussia Mönchengladbach', y2019='Borussia Mönchengladbach', y2020='Borussia Mönchengladbach', y2021='Borussia Mönchengladbach', y2022='Borussia Mönchengladbach')
    bundesliga.add_node(20, name='Mërgim Berisha ', club='FC Augsburg',y2016='FC Liefering', y2017='FC Red Bull Salzburg', y2018='1. FC Magdeburg', y2019='FC Red Bull Salzburg', y2020='FC Red Bull Salzburg', y2021='Fenerbahce SK Istanbul', y2022='FC Augsburg')
    bundesliga.add_node(21, name='Jonas Hofmann', club='Borussia Mönchengladbach', y2013='Borussia Dortmund', y2014='1. FSV Mainz 05', y2015='Borussia Dortmund', y2016='Borussia Mönchengladbach', y2017='Borussia Mönchengladbach', y2018='Borussia Mönchengladbach', y2019='Borussia Mönchengladbach', y2020='Borussia Mönchengladbach', y2021='Borussia Mönchengladbach', y2022='Borussia Mönchengladbach')
    bundesliga.add_node(22, name='Ko Itakura', club='Borussia Mönchengladbach', y2013='Kawasaki Frontale', y2014='Kawasaki Frontale', y2015='Kawasaki Frontale', y2016='Kawasaki Frontale', y2017='Kawasaki Frontale', y2018='Vegalta Sendai', y2019='Kawasaki Frontale', y2020='Manchester City FC', y2021='Manchester City FC', y2022='Borussia Mönchengladbach')
    bundesliga.add_node(23, name='Daniel Klein', club='FC Augsburg', y2013='FC Astoria Walldorf', y2014='TSG 1899 Hoffenheim', y2015='TSG 1899 Hoffenheim', y2016='TSG 1899 Hoffenheim', y2017='TSG 1899 Hoffenheim', y2018='TSG 1899 Hoffenheim', y2019='TSG 1899 Hoffenheim', y2020='TSG 1899 Hoffenheim', y2021='FC Augsburg', y2022='FC Augsburg')
    bundesliga.add_node(24, name='Alassane Pléa', club='Borussia Mönchengladbach', y2013='Olympique Lyonnais', y2014='AJ Auxerre' , y2015='OGC Nice', y2016='OGC Nice', y2017='OGC Nice', y2018='Borussia Mönchengladbach', y2019='Borussia Mönchengladbach', y2020='Borussia Mönchengladbach', y2021='Borussia Mönchengladbach', y2022='Borussia Mönchengladbach')
    bundesliga.add_node(25, name='Waldemar Anton', club='VfB Stuttgart', y2013='Hannover 96', y2014='Hannover 96', y2015='Hannover 96', y2016='Hannover 96', y2017='Hannover 96', y2018='Hannover 96', y2019='Hannover 96', y2020='VfB Stuttgart', y2021='VfB Stuttgart', y2022='VfB Stuttgart')
    bundesliga.add_node(26, name='Antonis Aidonis', club='VfB Stuttgart', y2013='TSG 1899 Hoffenheim', y2014='TSG 1899 Hoffenheim', y2015='TSG 1899 Hoffenheim', y2016='TSG 1899 Hoffenheim', y2017='TSG 1899 Hoffenheim', y2018='VfB Stuttgart', y2019='VfB Stuttgart', y2020='VfB Stuttgart', y2021='SG Dynamo Dresden', y2022='VfB Stuttgart')
    bundesliga.add_node(27, name='Sven Ulreich', club='FC Bayern München', y2013='VfB Stuttgart', y2014='VfB Stuttgart', y2015='FC Bayern München', y2016='FC Bayern München', y2017='FC Bayern München', y2018='FC Bayern München', y2019='FC Bayern München', y2020='Hamburger SV', y2021='FC Bayern München', y2022='FC Bayern München')
    bundesliga.add_node(28, name='Semir Telalovic', club='Borussia Mönchengladbach', y2017='SSV Ehingen-Süd', y2018='SSV Ehingen-Süd', y2019='SSV Ehingen-Süd', y2020='SSV Ehingen-Süd', y2021='FV Illertissen', y2022='Borussia Mönchengladbach')
    bundesliga.add_node(29, name='Alexander Meyer', club='Borussia Dortmund', y2013='TSV Havelse', y2014='TSV Havelse', y2015='TSV Havelse', y2016='FC Energie Cottbus', y2017='VfB Stuttgart', y2018='VfB Stuttgart', y2019='SSV Jahn Regensburg', y2020='SSV Jahn Regensburg', y2021='SSV Jahn Regensburg', y2022='Borussia Dortmund')
    bundesliga.add_node(30, name='Atakan Karazor', club='VfB Stuttgart', y2013='VfL Bochum', y2014='VfL Bochum', y2015='Borussia Dortmund', y2016='Borussia Dortmund', y2017='Holstein Kiel', y2018='Holstein Kiel', y2019='VfB Stuttgart', y2020='VfB Stuttgart', y2021='VfB Stuttgart', y2022='VfB Stuttgart')
    bundesliga.add_node(31, name='Felix Uduokhai', club='FC Augsburg', y2013='TSV 1860 München', y2014='TSV 1860 München', y2015='TSV 1860 München', y2016='TSV 1860 München', y2017='TSV 1860 München', y2018='TSV 1860 München', y2019='FC Augsburg', y2020='FC Augsburg', y2021='FC Augsburg', y2022='FC Augsburg')
    bundesliga.add_node(32, name='Gabriel Marušić', club='FC Bayern München')
    bundesliga.add_node(33, name='André Hahn', club='FC Augsburg', y2013='FC Augsburg', y2014='Borussia Mönchengladbach', y2015='Borussia Mönchengladbach', y2016='Borussia Mönchengladbach', y2017='Hamburger SV', y2018='Hamburger SV', y2019='FC Augsburg', y2020='FC Augsburg', y2021='FC Augsburg', y2022='FC Augsburg')
    bundesliga.add_node(34, name='Matthijs de Ligt', club='FC Bayern München', y2013='Ajax Amsterdam', y2014='Ajax Amsterdam', y2015='Ajax Amsterdam', y2016='Ajax Amsterdam', y2017='Ajax Amsterdam', y2018='Ajax Amsterdam', y2019='Juventus FC Turin', y2020='Juventus FC Turin', y2021='Juventus FC Turin', y2022='FC Bayern München')
    bundesliga.add_node(35, name='Hiroki Ito', club='VfB Stuttgart', y2015='Jubilo Iwata', y2016='Jubilo Iwata', y2017='Jubilo Iwata', y2018='Jubilo Iwata', y2019='Nagoya Grampus Eight', y2020='Jubilo Iwata', y2021='VfB Stuttgart', y2022='VfB Stuttgart')

    numbernodes = bundesliga.number_of_nodes()
    #print('Knoten im Graph: ', numbernodes)

    for i in range(1, numbernodes+1):
        for j in range(1, numbernodes+1):

            if (bundesliga._node[i] == bundesliga._node[j]):
                break

            if (bundesliga._node[i].get('club') == bundesliga._node[j].get('club')):
                bundesliga.add_edge(i, j)
            if (bundesliga._node[i].get('y2013') == bundesliga._node[j].get('y2013')):
                bundesliga.add_edge(i, j)
            if (bundesliga._node[i].get('y2014') == bundesliga._node[j].get('y2014')):
                bundesliga.add_edge(i, j)
            if (bundesliga._node[i].get('y2015') == bundesliga._node[j].get('y2015')):
                bundesliga.add_edge(i, j)
            if (bundesliga._node[i].get('y2016') == bundesliga._node[j].get('y2016')):
                bundesliga.add_edge(i, j)
            if (bundesliga._node[i].get('y2017') == bundesliga._node[j].get('y2017')):
                bundesliga.add_edge(i, j)
            if (bundesliga._node[i].get('y2018') == bundesliga._node[j].get('y2018')):
                bundesliga.add_edge(i, j)
            if (bundesliga._node[i].get('y2019') == bundesliga._node[j].get('y2019')):
                bundesliga.add_edge(i, j)
            if (bundesliga._node[i].get('y2020') == bundesliga._node[j].get('y2020')):
                bundesliga.add_edge(i, j)
            if (bundesliga._node[i].get('y2021') == bundesliga._node[j].get('y2021')):
                bundesliga.add_edge(i, j)
            if (bundesliga._node[i].get('y2022') == bundesliga._node[j].get('y2022')):
                bundesliga.add_edge(i, j)

    return bundesliga


def read_hauptstaedte(filepointer):
    zeilen = filepointer.readlines()
    list_zeilen = []

    for zeile in zeilen:
        tmp = zeile.rstrip()
        list_zeile = tmp.split('#')
        list_zeile[0] = list(list_zeile[0].split(','))
        list_zeile[3] = list(list_zeile[3].split(','))
        tmp = []
        for val in list_zeile[0]:
            tmp.append(float(val))
        list_zeile[0] = tmp
        list_zeilen.append(list_zeile)

    return list_zeilen


def worldmap():

    fp = open('data/hauptstaedte.txt', 'r')
    list_data = read_hauptstaedte(fp)

    g = nx.Graph()
    list_country = []
    dict_pos = {}
    for city in list_data:
        dict_pos[city[2]] = (city[0][1], city[0][0])
        list_country.append(city[2])
        for n in city[3]:
            g.add_edge(city[2], n)

    g_nodes = g.nodes()
    for n in g_nodes:
        if n in list_country:
            a = 2 + 1
        else:
            print("Data to ", n, ' does not exist')

    return g


def read_streets(fp):
    zeilen = fp.readlines()
    l_zeilen = []
    for zeile in zeilen:
        tmp = zeile.rstrip()
        l_cross = tmp.split(',')
        l_zeilen.append(l_cross)
    return l_zeilen


def graben_streets():
    fp = open('data/graben.txt', 'r')
    l_crosses = read_streets(fp)
    graben = nx.Graph()

    for cross in l_crosses:
        graben.add_edge(cross[0], cross[1])

    return graben
