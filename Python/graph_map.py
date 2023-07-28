import time
import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
graph = nx.Graph()


# Define positions (physical coordinates) for each node
# Define positions (physical coordinates) for each node
positions = {
    # -------colonne1--------
    1: {'pos': (30, 57), 'col': 1, 'line': 1},
    2: {'pos': (30, 627), 'col': 1, 'line': 2},
    3: {'pos': (30, 1219), 'col': 1, 'line': 3},
    4: {'pos': (30, 1781), 'col': 1, 'line': 4},
    5: {'pos': (30, 2370), 'col': 1, 'line': 5},
    6: {'pos': (30, 2927), 'col': 1, 'line': 6},
    # -------colonne2--------
    7: {'pos': (115, 57), 'col': 2, 'line': 1},
    8: {'pos': (115, 627), 'col': 2, 'line': 2},
    9: {'pos': (115, 1219), 'col': 2, 'line': 3},
    10: {'pos': (115, 1781), 'col': 2, 'line': 4},
    11: {'pos': (115, 2370), 'col': 2, 'line': 5},
    12: {'pos': (115, 2927), 'col': 2, 'line': 6},
    # ------colonne3--------
    13: {'pos': (207, 57), 'col': 3, 'line': 1},
    14: {'pos': (207, 627), 'col': 3, 'line': 2},
    15: {'pos': (207, 1219), 'col': 3, 'line': 3},
    16: {'pos': (207, 1781), 'col': 3, 'line': 4},
    17: {'pos': (207, 2370), 'col': 3, 'line': 5},
    18: {'pos': (207, 2927), 'col': 3, 'line': 6},
    # -------colonne4--------
    19: {'pos': (293, 57), 'col': 4, 'line': 1},
    20: {'pos': (293, 627), 'col': 4, 'line': 2},
    21: {'pos': (293, 1219), 'col': 4, 'line': 3},
    22: {'pos': (293, 1781), 'col': 4, 'line': 4},
    23: {'pos': (293, 2370), 'col': 4, 'line': 5},
    24: {'pos': (293, 2927), 'col': 4, 'line': 6},
    # -------colonne5--------
    25: {'pos': (373, 57), 'col': 5, 'line': 1},
    26: {'pos': (373, 627), 'col': 5, 'line': 2},
    27: {'pos': (373, 1219), 'col': 5, 'line': 3},
    28: {'pos': (373, 1781), 'col': 5, 'line': 4},
    29: {'pos': (373, 2370), 'col': 5, 'line': 5},
    30: {'pos': (373, 2927), 'col': 5, 'line': 6},
    # -------colonne6--------
    31: {'pos': (461, 57), 'col': 6, 'line': 1},
    32: {'pos': (461, 627), 'col': 6, 'line': 2},
    33: {'pos': (461, 1219), 'col': 6, 'line': 3},
    34: {'pos': (461, 1781), 'col': 6, 'line': 4},
    35: {'pos': (461, 2370), 'col': 6, 'line': 5},
    36: {'pos': (461, 2927), 'col': 6, 'line': 6},
    # -------colonne7--------
    37: {'pos': (555, 57), 'col':   7, 'line': 1},
    38: {'pos': (555, 627), 'col':  7, 'line': 2},
    39: {'pos': (555, 1219), 'col': 7, 'line': 3},
    40: {'pos': (555, 1781), 'col': 7, 'line': 4},
    41: {'pos': (555, 2370), 'col': 7, 'line': 5},
    42: {'pos': (555, 2927), 'col': 7, 'line': 6},
    # ************************************************************
    # -------colonne8--------
    43: {'pos': (1514, 52), 'col':   8, 'line': 1},
    44: {'pos': (1514, 617), 'col':  8, 'line': 2},
    45: {'pos': (1514, 1214), 'col': 8, 'line': 3},
    46: {'pos': (1514, 1775), 'col': 8, 'line': 4},
    47: {'pos': (1514, 2362), 'col': 8, 'line': 5},
    48: {'pos': (1514, 2925), 'col': 8, 'line': 6},
    # -------colonne9--------
    49: {'pos': (1609, 52), 'col':   9, 'line': 1},
    50: {'pos': (1609, 617), 'col':  9, 'line': 2},
    51: {'pos': (1609, 1214), 'col': 9, 'line': 3},
    52: {'pos': (1609, 1775), 'col': 9, 'line': 4},
    53: {'pos': (1609, 2362), 'col': 9, 'line': 5},
    54: {'pos': (1609, 2927), 'col': 9, 'line': 6},
    # -------colonne10--------
    55: {'pos': (1695, 52), 'col':   10, 'line': 1},
    56: {'pos': (1695, 617), 'col':  10, 'line': 2},
    57: {'pos': (1695, 1214), 'col': 10, 'line': 3},
    58: {'pos': (1695, 1775), 'col': 10, 'line': 4},
    59: {'pos': (1695, 2362), 'col': 10, 'line': 5},
    60: {'pos': (1695, 2927), 'col': 10, 'line': 6},
    # -------colonne11--------
    61: {'pos': (1783, 52), 'col':   11, 'line': 1},
    62: {'pos': (1783, 617), 'col':  11, 'line': 2},
    63: {'pos': (1783, 1214), 'col': 11, 'line': 3},
    64: {'pos': (1783, 1775), 'col': 11, 'line': 4},
    65: {'pos': (1783, 2362), 'col': 11, 'line': 5},
    66: {'pos': (1783, 2927), 'col': 11, 'line': 6},
    # -------colonne12--------
    67: {'pos': (1868, 52), 'col':   12, 'line': 1},
    68: {'pos': (1868, 617), 'col':  12, 'line': 2},
    69: {'pos': (1868, 1214), 'col': 12, 'line': 3},
    70: {'pos': (1868, 1775), 'col': 12, 'line': 4},
    71: {'pos': (1868, 2362), 'col': 12, 'line': 5},
    72: {'pos': (1868, 2927), 'col': 12, 'line': 6},
    # -------colonne13--------
    73: {'pos': (1955, 52), 'col':   13, 'line': 1},
    74: {'pos': (1955, 617), 'col':  13, 'line': 2},
    75: {'pos': (1955, 1214), 'col': 13, 'line': 3},
    76: {'pos': (1955, 1775), 'col': 13, 'line': 4},
    77: {'pos': (1955, 2362), 'col': 13, 'line': 5},
    78: {'pos': (1955, 2927), 'col': 13, 'line': 6},
    # -------colonne14--------
    79: {'pos': (2043, 52), 'col':   14, 'line': 1},
    80: {'pos': (2043, 617), 'col':  14, 'line': 2},
    81: {'pos': (2043, 1214), 'col': 14, 'line': 3},
    82: {'pos': (2043, 1775), 'col': 14, 'line': 4},
    83: {'pos': (2043, 2362), 'col': 14, 'line': 5},
    84: {'pos': (2043, 2927), 'col': 14, 'line': 6},
    # *******************************************
    # -------colonne15--------
    85: {'pos': (3011, 52), 'col':   15, 'line': 1},
    86: {'pos': (3011, 617), 'col':  15, 'line': 2},
    87: {'pos': (3011, 1214), 'col': 15, 'line': 3},
    88: {'pos': (3011, 1775), 'col': 15, 'line': 4},
    89: {'pos': (3011, 2362), 'col': 15, 'line': 5},
    90: {'pos': (3011, 2927), 'col': 15, 'line': 6},
    # -------colonne16--------
    91: {'pos': (3104, 52), 'col':   16, 'line': 1},
    92: {'pos': (3104, 617), 'col':  16, 'line': 2},
    93: {'pos': (3104, 1214), 'col': 16, 'line': 3},
    94: {'pos': (3104, 1775), 'col': 16, 'line': 4},
    95: {'pos': (3104, 2362), 'col': 16, 'line': 5},
    96: {'pos': (3104, 2927), 'col': 16, 'line': 6},
    # -------colonne17--------
    97: {'pos': (3190, 52), 'col':   17, 'line': 1},
    98: {'pos': (3190, 617), 'col':  17, 'line': 2},
    99: {'pos': (3190, 1214), 'col': 17, 'line': 3},
    100: {'pos': (3190, 1775), 'col': 17, 'line': 4},
    101: {'pos': (3190, 2362), 'col': 17, 'line': 5},
    102: {'pos': (3190, 2927), 'col': 17, 'line': 6},
    # -------colonne18--------
    103: {'pos': (3276, 52), 'col':   18, 'line': 1},
    104: {'pos': (3276, 617), 'col':  18, 'line': 2},
    105: {'pos': (3276, 1214), 'col': 18, 'line': 3},
    106: {'pos': (3276, 1775), 'col': 18, 'line': 4},
    107: {'pos': (3276, 2362), 'col': 18, 'line': 5},
    108: {'pos': (3276, 2927), 'col': 18, 'line': 6},
    # -------colonne19--------
    109: {'pos': (3362, 52), 'col':   19, 'line': 1},
    110: {'pos': (3362, 617), 'col':  19, 'line': 2},
    111: {'pos': (3362, 1214), 'col': 19, 'line': 3},
    112: {'pos': (3362, 1775), 'col': 19, 'line': 4},
    113: {'pos': (3362, 2362), 'col': 19, 'line': 5},
    114: {'pos': (3362, 2927), 'col': 19, 'line': 6},
    # -------colonne20--------
    115: {'pos': (3450, 52), 'col':   20, 'line': 1},
    116: {'pos': (3450, 617), 'col':  20, 'line': 2},
    117: {'pos': (3450, 1214), 'col': 20, 'line': 3},
    118: {'pos': (3450, 1775), 'col': 20, 'line': 4},
    119: {'pos': (3450, 2362), 'col': 20, 'line': 5},
    120: {'pos': (3450, 2927), 'col': 20, 'line': 6},
    # -------colonne21--------
    121: {'pos': (3537, 52), 'col':  21, 'line': 1},
    122: {'pos': (3537, 617), 'col': 21, 'line': 2},
    123: {'pos': (3537, 1214), 'col':21, 'line': 3},
    124: {'pos': (3537, 1775), 'col':21, 'line': 4},
    125: {'pos': (3537, 2362), 'col':21, 'line': 5},
    126: {'pos': (3537, 2927), 'col':21, 'line': 6},
    # *********************************************
    # ---------------REST POSITIONS----------------
    127: {'pos': (1040, 617), 'col':  "r1", 'line': 2},
    128: {'pos': (1040, 1775), 'col': "r1", 'line': 4},
    129: {'pos': (1040, 2927), 'col': "r1", 'line': 6},
    130: {'pos': (2516, 617), 'col': "r2", 'line': 2},
    131: {'pos': (2516, 1775), 'col':"r2", 'line': 4},
    132: {'pos': (2516, 2927), 'col':"r2", 'line': 6},
}


def convertPixelsToCm(x):
    '''
        To BE CHECKED
    '''
    return x*4./659.

for node in positions:
    x, y = positions[node]['pos']
    positions[node]['pos'] = (convertPixelsToCm(x), convertPixelsToCm(y))

# Add nodes with positions to the graph
#graph.add_nodes_from(positions)
graph.add_nodes_from((node_id, attrs) for node_id, attrs in positions.items())

# Set the node positions as attributes in the graph
#nx.set_node_attributes(graph, positions)

# Calculate the Euclidean distance between two nodes in the real world


def distance(node1, node2):
    x1, y1 = positions[node1]['pos']
    x2, y2 = positions[node2]['pos']
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5


def addEdge(node1, node2, coeff=1):
    graph.add_edge(node1, node2, weight=distance(node1, node2)*coeff)


def linkCol(nodeStart, coeff=1):
    addEdge(nodeStart+1,nodeStart+2)
    addEdge(nodeStart+3,nodeStart+4)
    for i in range(0,5,2):
        addEdge(nodeStart+i, nodeStart+i+1, coeff)

def linkLine(nodeStart, coeff=1):
    for i in range(20):  # POUR LE MOMENT
        addEdge(nodeStart+i*6, nodeStart+(i+1)*6, coeff)

def linkBlockCols(start):
    # ------colonne1------
    linkCol(start, 1)

    # ------colonne2-->6------
    for i in range(1, 6):
        linkCol(start+6*i, 2)

    # ------colonne7------
    linkCol(start+6*6, 1)

def linkRest(rest, start):
    addEdge(rest, start)
    addEdge(rest, start+6)

# Add edges to the graph with physical distances as edge weights

# ------Link Cols------
linkBlockCols(1)
linkBlockCols(43)
linkBlockCols(85)

# ------Line1---------
linkLine(1, 1.6)
# ------Line2---------
linkLine(2, 1.5)
# ------Line3---------
linkLine(3, 1.55)
# ------Line4---------
linkLine(4, 1.4)
# ------Line5---------
linkLine(5, 1.4)
# ------Line6---------
linkLine(6)

# -------LinkRest------
linkRest(127, 38)
linkRest(128, 40)
linkRest(129, 42)
linkRest(130, 80)
linkRest(131, 82)
linkRest(132, 84)
addEdge(127, 128)
addEdge(128, 129)
addEdge(130, 131)
addEdge(131, 132)

def node_exists_at_position(x, y):
    for node, data in graph.nodes(data=True):
        if 'pos' in data and abs(data['pos'][0]-x)<0.05 and abs(data['pos'][1])-y<0.05:
            return node
    return 0

# --------------CHECK---------------------------
def addDynamicNodeGoal(id, x, y, id_source):
    node = node_exists_at_position(x,y)
    if(node):  #SHOULD NEVER BE THE CASE
        return node
    else :
        distances_to_new_node = {node: ((x - data['pos'][0])**2 + (
            y - data['pos'][1])**2)**0.5 for node, data in graph.nodes(data=True)}
        
        #IL FAUDRAIT VERIFIER SI LE NOEUD QU'ON AJOUTE N'EST PAS DÉJÀ UN NOEUD
        
        closest_node = min(distances_to_new_node, key=distances_to_new_node.get)
        graph.add_node(id, pos=(x, y))
        graph.add_edge(id, closest_node,
                    weight=distances_to_new_node[closest_node])
        if(closest_node!=id_source):
            graph.add_edge(id, closest_node+1,
                        weight=distances_to_new_node[closest_node+1])
            graph.add_edge(id, closest_node+6,
                        weight=distances_to_new_node[closest_node+6]*3)
            graph.add_edge(id, closest_node+7,
                        weight=distances_to_new_node[closest_node+7]*3)
        return id

def addDynamicNodePos(id, x, y):
    node = node_exists_at_position(x,y)
    if(node):
        return node
    distances_to_new_node = {node: ((x - data['pos'][0])**2 + (
        y - data['pos'][1])**2)**0.5 for node, data in graph.nodes(data=True)}

    #IL FAUDRAIT VERIFIER SI LE NOEUD QU'ON AJOUTE N'EST PAS DÉJÀ UN NOEUD

    closest_node = min(distances_to_new_node, key=distances_to_new_node.get)
    # distances_to_new_node.remove(closest_node)
    closest_node1 = min(distances_to_new_node, key=distances_to_new_node.get)
    graph.add_node(id, pos=(x, y))
    graph.add_edge(id, closest_node,
                   weight=distances_to_new_node[closest_node])
    graph.add_edge(id, closest_node1,
                   weight=distances_to_new_node[closest_node1])
    return id

t0 = time.time()
# Create a subgraph with only visible edges
'''
subgraph = graph.copy()
for u, v, data in graph.edges(data=True):
    if 'hidden' in data and data['hidden']:
        subgraph.remove_edge(u, v)
'''
# addDynamicNodePos(300, 160,2902)
# addDynamicNodeGoal(301, 251,2515)


def shortest_path(source,target):
    id_source = addDynamicNodePos(135,source[0],source[1])
    id_goal = addDynamicNodeGoal(136,target[0],target[1],id_source)

    # Find the shortest path based on physical distances
    shortest_path = nx.shortest_path(graph, id_source, id_goal, weight='weight')

    i=1
    cols = False
    lines=False
    time.sleep(0.1)  #CHECK IF NEEDED
    
    if(shortest_path!=[]):
        while i < len(shortest_path):
            if not lines and 'col' in graph.nodes[shortest_path[i]] and 'col' in graph.nodes[shortest_path[i-1]]:
                if graph.nodes[shortest_path[i]]['col'] == graph.nodes[shortest_path[i-1]]['col']:
                    shortest_path.pop(i-1)
                    cols = True
                    i=i-1
                else:
                    if cols:
                        if(len(shortest_path)-i>0):
                            i = i+1
                            cols = False
                        
                    
            if not cols and 'line' in graph.nodes[shortest_path[i]] and 'line' in graph.nodes[shortest_path[i-1]]:
                if graph.nodes[shortest_path[i]]['line']==graph.nodes[shortest_path[i-1]]['line']:

                        shortest_path.pop(i-1)    
                        i=i-1
                        lines = True
                else:
                    if lines:        
                        if(len(shortest_path)-i>0):
                            i = i + 1   
                            lines = False

            i=i+1

    #remove first element since its node will be removed
    shortest_path.pop(0)

    #remove last element since its position is known in the main function and its node will be removed
    #shortest_path.pop(-1)   
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    if(id_source == 135):
        graph.remove_node(135)
    if(id_goal == 136):
        graph.remove_node(136)

    # graph.remove_node(300)
    #print(time.time()-t0)
    print("Shortest path based on physical distances:", shortest_path)

    return shortest_path


# Visualize the graph with node positions
def plotGraph():
    pos = nx.get_node_attributes(graph, 'pos')
    nx.draw(graph, pos, with_labels=True, node_size=500, font_size=12)
    #edge_labels = nx.get_edge_attributes(graph, 'weight')
    #nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    plt.show()

def getNodePosition(node):
    return graph.nodes[node]['pos']
    #return nx.get_node_attributes(graph, 'pos')[node]
# You can also draw edges with attributes (e.g., weights)
#edge_labels = nx.get_edge_attributes(graph, 'weight')
#nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

#print(shortest_path([1,123],[8,650]))
#print(getNodePosition(46))
#plotGraph()



'''
---------------In this dico, there are the exact positions in pixels 
positions = {
    # -------colonne1--------
    1: {'pos': (27, 57), 'col': 1, 'line': 1},
    2: {'pos': (27, 627), 'col': 1, 'line': 2},
    3: {'pos': (27, 1219), 'col': 1, 'line': 3},
    4: {'pos': (27, 1781), 'col': 1, 'line': 4},
    5: {'pos': (27, 2370), 'col': 1, 'line': 5},
    6: {'pos': (27, 2925), 'col': 1, 'line': 6},
    # -------colonne2--------
    7: {'pos': (109, 57), 'col': 2, 'line': 1},
    8: {'pos': (109, 627), 'col': 2, 'line': 2},
    9: {'pos': (117, 1219), 'col': 2, 'line': 3},
    10: {'pos': (117, 1781), 'col': 2, 'line': 4},
    11: {'pos': (121, 2370), 'col': 2, 'line': 5},
    12: {'pos': (121, 2925), 'col': 2, 'line': 6},
    # ------colonne3--------
    13: {'pos': (200, 57), 'col': 3, 'line': 1},
    14: {'pos': (200, 627), 'col': 3, 'line': 2},
    15: {'pos': (207, 1219), 'col': 3, 'line': 3},
    16: {'pos': (207, 1781), 'col': 3, 'line': 4},
    17: {'pos': (213, 2370), 'col': 3, 'line': 5},
    18: {'pos': (213, 2925), 'col': 3, 'line': 6},
    # -------colonne4--------
    19: {'pos': (287, 57), 'col': 4, 'line': 1},
    20: {'pos': (287, 627), 'col': 4, 'line': 2},
    21: {'pos': (293, 1219), 'col': 4, 'line': 3},
    22: {'pos': (293, 1781), 'col': 4, 'line': 4},
    23: {'pos': (300, 2370), 'col': 4, 'line': 5},
    24: {'pos': (300, 2925), 'col': 4, 'line': 6},
    # -------colonne5--------
    25: {'pos': (369, 57), 'col': 5, 'line': 1},
    26: {'pos': (369, 627), 'col': 5, 'line': 2},
    27: {'pos': (373, 1219), 'col': 5, 'line': 3},
    28: {'pos': (373, 1781), 'col': 5, 'line': 4},
    29: {'pos': (377, 2370), 'col': 5, 'line': 5},
    30: {'pos': (377, 2925), 'col': 5, 'line': 6},
    # -------colonne6--------
    31: {'pos': (457, 57), 'col': 6, 'line': 1},
    32: {'pos': (457, 627), 'col': 6, 'line': 2},
    33: {'pos': (461, 1219), 'col': 6, 'line': 3},
    34: {'pos': (461, 1781), 'col': 6, 'line': 4},
    35: {'pos': (465, 2370), 'col': 6, 'line': 5},
    36: {'pos': (465, 2925), 'col': 6, 'line': 6},
    # -------colonne7--------
    37: {'pos': (555, 57), 'col':   7, 'line': 1},
    38: {'pos': (555, 627), 'col':  7, 'line': 2},
    39: {'pos': (555, 1219), 'col': 7, 'line': 3},
    40: {'pos': (555, 1781), 'col': 7, 'line': 4},
    41: {'pos': (555, 2370), 'col': 7, 'line': 5},
    42: {'pos': (555, 2925), 'col': 7, 'line': 6},
    # ************************************************************
    # -------colonne8--------
    43: {'pos': (1500, 52), 'col':   8, 'line': 1},
    44: {'pos': (1500, 617), 'col':  8, 'line': 2},
    45: {'pos': (1500, 1214), 'col': 8, 'line': 3},
    46: {'pos': (1500, 1775), 'col': 8, 'line': 4},
    47: {'pos': (1500, 2362), 'col': 8, 'line': 5},
    48: {'pos': (1500, 2925), 'col': 8, 'line': 6},
    # -------colonne9--------
    49: {'pos': (1607, 52), 'col':   9, 'line': 1},
    50: {'pos': (1607, 617), 'col':  9, 'line': 2},
    51: {'pos': (1609, 1214), 'col': 9, 'line': 3},
    52: {'pos': (1609, 1775), 'col': 9, 'line': 4},
    53: {'pos': (1609, 2362), 'col': 9, 'line': 5},
    54: {'pos': (1609, 2927), 'col': 9, 'line': 6},
    # -------colonne10--------
    55: {'pos': (1691, 52), 'col':   10, 'line': 1},
    56: {'pos': (1691, 617), 'col':  10, 'line': 2},
    57: {'pos': (1691, 1214), 'col': 10, 'line': 3},
    58: {'pos': (1696, 1775), 'col': 10, 'line': 4},
    59: {'pos': (1699, 2362), 'col': 10, 'line': 5},
    60: {'pos': (1699, 2927), 'col': 10, 'line': 6},
    # -------colonne11--------
    61: {'pos': (1779, 52), 'col':   11, 'line': 1},
    62: {'pos': (1779, 617), 'col':  11, 'line': 2},
    63: {'pos': (1783, 1214), 'col': 11, 'line': 3},
    64: {'pos': (1783, 1775), 'col': 11, 'line': 4},
    65: {'pos': (1787, 2362), 'col': 11, 'line': 5},
    66: {'pos': (1787, 2927), 'col': 11, 'line': 6},
    # -------colonne12--------
    67: {'pos': (1866, 52), 'col':   12, 'line': 1},
    68: {'pos': (1866, 617), 'col':  12, 'line': 2},
    69: {'pos': (1868, 1214), 'col': 12, 'line': 3},
    70: {'pos': (1868, 1775), 'col': 12, 'line': 4},
    71: {'pos': (1870, 2362), 'col': 12, 'line': 5},
    72: {'pos': (1870, 2927), 'col': 12, 'line': 6},
    # -------colonne13--------
    73: {'pos': (1952, 52), 'col':   13, 'line': 1},
    74: {'pos': (1952, 617), 'col':  13, 'line': 2},
    75: {'pos': (1955, 1214), 'col': 13, 'line': 3},
    76: {'pos': (1955, 1775), 'col': 13, 'line': 4},
    77: {'pos': (1959, 2362), 'col': 13, 'line': 5},
    78: {'pos': (1959, 2927), 'col': 13, 'line': 6},
    # -------colonne14--------
    79: {'pos': (2043, 52), 'col':   14, 'line': 1},
    80: {'pos': (2043, 617), 'col':  14, 'line': 2},
    81: {'pos': (2043, 1214), 'col': 14, 'line': 3},
    82: {'pos': (2043, 1775), 'col': 14, 'line': 4},
    83: {'pos': (2043, 2362), 'col': 14, 'line': 5},
    84: {'pos': (2043, 2927), 'col': 14, 'line': 6},
    # *******************************************
    # -------colonne15--------
    85: {'pos': (3011, 52), 'col':   15, 'line': 1},
    86: {'pos': (3011, 617), 'col':  15, 'line': 2},
    87: {'pos': (3011, 1214), 'col': 15, 'line': 3},
    88: {'pos': (3011, 1775), 'col': 15, 'line': 4},
    89: {'pos': (3011, 2362), 'col': 15, 'line': 5},
    90: {'pos': (3011, 2927), 'col': 15, 'line': 6},
    # -------colonne16--------
    91: {'pos': (3101, 52), 'col':   16, 'line': 1},
    92: {'pos': (3101, 617), 'col':  16, 'line': 2},
    93: {'pos': (3104, 1214), 'col': 16, 'line': 3},
    94: {'pos': (3104, 1775), 'col': 16, 'line': 4},
    95: {'pos': (3106, 2362), 'col': 16, 'line': 5},
    96: {'pos': (3106, 2927), 'col': 16, 'line': 6},
    # -------colonne17--------
    97: {'pos': (3187, 52), 'col':   17, 'line': 1},
    98: {'pos': (3187, 617), 'col':  17, 'line': 2},
    99: {'pos': (3190, 1214), 'col': 17, 'line': 3},
    100: {'pos': (3190, 1775), 'col': 17, 'line': 4},
    101: {'pos': (3194, 2362), 'col': 17, 'line': 5},
    102: {'pos': (3194, 2927), 'col': 17, 'line': 6},
    # -------colonne18--------
    103: {'pos': (3273, 52), 'col':   18, 'line': 1},
    104: {'pos': (3273, 617), 'col':  18, 'line': 2},
    105: {'pos': (3277, 1214), 'col': 18, 'line': 3},
    106: {'pos': (3277, 1775), 'col': 18, 'line': 4},
    107: {'pos': (3278, 2362), 'col': 18, 'line': 5},
    108: {'pos': (3278, 2927), 'col': 18, 'line': 6},
    # -------colonne19--------
    109: {'pos': (3359, 52), 'col':   19, 'line': 1},
    110: {'pos': (3359, 617), 'col':  19, 'line': 2},
    111: {'pos': (3362, 1214), 'col': 19, 'line': 3},
    112: {'pos': (3362, 1775), 'col': 19, 'line': 4},
    113: {'pos': (3366, 2362), 'col': 19, 'line': 5},
    114: {'pos': (3366, 2927), 'col': 19, 'line': 6},
    # -------colonne20--------
    115: {'pos': (3347, 52), 'col':   20, 'line': 1},
    116: {'pos': (3347, 617), 'col':  20, 'line': 2},
    117: {'pos': (3450, 1214), 'col': 20, 'line': 3},
    118: {'pos': (3450, 1775), 'col': 20, 'line': 4},
    119: {'pos': (3454, 2362), 'col': 20, 'line': 5},
    120: {'pos': (3454, 2927), 'col': 20, 'line': 6},
    # -------colonne21--------
    121: {'pos': (3537, 52), 'col':  21, 'line': 1},
    122: {'pos': (3537, 617), 'col': 21, 'line': 2},
    123: {'pos': (3537, 1214), 'col':21, 'line': 3},
    124: {'pos': (3537, 1775), 'col':21, 'line': 4},
    125: {'pos': (3537, 2362), 'col':21, 'line': 5},
    126: {'pos': (3537, 2927), 'col':21, 'line': 6},
    # *********************************************
    # ---------------REST POSITIONS----------------
    127: {'pos': (1040, 617), 'col':  "r1", 'line': 2},
    128: {'pos': (1040, 1775), 'col': "r1", 'line': 4},
    129: {'pos': (1040, 2927), 'col': "r1", 'line': 6},
    130: {'pos': (2516, 617), 'col': "r2", 'line': 2},
    131: {'pos': (2516, 1775), 'col':"r2", 'line': 4},
    132: {'pos': (2516, 2972), 'col':"r2", 'line': 6},
}
'''

