import time
import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
graph = nx.Graph()


# Define positions (in pixels) for each node
positions = {
    # -------colonne1--------
    1: {'pos': (27, 18.6), 'col': 1, 'line': 1},
    2: {'pos': (27, 15), 'col': 1, 'line': 2},
    3: {'pos': (27, 11.6), 'col': 1, 'line': 3},
    4: {'pos': (27, 8), 'col': 1, 'line': 4},
    5: {'pos': (27, 5), 'col': 1, 'line': 5},
    6: {'pos': (27, 0), 'col': 1, 'line': 6},
    # -------colonne2--------
    7: {'pos': (26.45, 18.6), 'col': 2, 'line': 1},
    8: {'pos': (26.45, 15), 'col': 2, 'line': 2},
    9: {'pos': (26.45, 11.6), 'col': 2, 'line': 3},
    10: {'pos': (26.45,8), 'col': 2, 'line': 4},
    11: {'pos': (26.45,5), 'col': 2, 'line': 5},
    12: {'pos': (26.45,0), 'col': 2, 'line': 6},
    # ------colonne3--------
    13: {'pos': (25.9, 18.6),  'col': 3, 'line': 1},
    14: {'pos': (25.9, 15), 'col': 3, 'line': 2},
    15: {'pos': (25.9, 11.6), 'col': 3, 'line': 3},
    16: {'pos': (25.9, 8), 'col': 3, 'line': 4},
    17: {'pos': (25.9, 5), 'col': 3, 'line': 5},
    18: {'pos': (25.9, 0), 'col': 3, 'line': 6},
    # -------colonne4--------
    19: {'pos': (25.4, 18.6),  'col': 4, 'line': 1},
    20: {'pos': (25.4, 15), 'col': 4, 'line': 2},
    21: {'pos': (25.4, 11.6), 'col': 4, 'line': 3},
    22: {'pos': (25.4, 8), 'col': 4, 'line': 4},
    23: {'pos': (25.4, 5), 'col': 4, 'line': 5},
    24: {'pos': (25.4, 0), 'col': 4, 'line': 6},
    # -------colonne5--------
    25: {'pos': (24.9, 18.6),  'col': 5, 'line': 1},
    26: {'pos': (24.9, 15), 'col': 5, 'line': 2},
    27: {'pos': (24.9, 11.6), 'col': 5, 'line': 3},
    28: {'pos': (24.9, 8), 'col': 5, 'line': 4},
    29: {'pos': (24.9, 5), 'col': 5, 'line': 5},
    30: {'pos': (24.9, 0), 'col': 5, 'line': 6},
    # -------colonne6--------
    31: {'pos': (24.4, 18.6),  'col': 6, 'line': 1},
    32: {'pos': (24.4, 15), 'col': 6, 'line': 2},
    33: {'pos': (24.4, 11.6), 'col': 6, 'line': 3},
    34: {'pos': (24.4, 8), 'col': 6, 'line': 4},
    35: {'pos': (24.4, 5), 'col': 6, 'line': 5},
    36: {'pos': (24.4, 0), 'col': 6, 'line': 6},
    # -------colonne7--------
    37: {'pos': (23.9, 18.6),  'col':   7, 'line': 1},
    38: {'pos': (23.9, 15), 'col':  7, 'line': 2},
    39: {'pos': (23.9, 11.6), 'col': 7, 'line': 3},
    40: {'pos': (23.9, 8), 'col': 7, 'line': 4},
    41: {'pos': (23.9, 5), 'col': 7, 'line': 5},
    42: {'pos': (23.9, 0), 'col': 7, 'line': 6},
    # -------colonne8--------
    43: {'pos': (23.3, 18.6),  'col':   8, 'line': 1},
    44: {'pos': (23.3, 15), 'col':  8, 'line': 2},
    45: {'pos': (23.3, 11.6), 'col': 8, 'line': 3},
    46: {'pos': (23.3, 8), 'col': 8, 'line': 4},
    47: {'pos': (23.3, 5), 'col': 8, 'line': 5},
    48: {'pos': (23.3, 0), 'col': 8, 'line': 6},
    # ************************************************************

    # -------colonne9--------
    49: {'pos': (18, 18.6),  'col':   9, 'line': 1},
    50: {'pos': (18, 15), 'col':  9, 'line': 2},
    51: {'pos': (18, 11.6), 'col': 9, 'line': 3},
    52: {'pos': (18, 8), 'col': 9, 'line': 4},
    53: {'pos': (18, 5), 'col': 9, 'line': 5},
    54: {'pos': (18, 0), 'col': 9, 'line': 6},
    # -------colonne10--------
    55: {'pos': (17.5, 18.6),  'col':   10, 'line': 1},
    56: {'pos': (17.5, 15), 'col':  10, 'line': 2},
    57: {'pos': (17.5, 11.6), 'col': 10, 'line': 3},
    58: {'pos': (17.5, 8), 'col': 10, 'line': 4},
    59: {'pos': (17.5, 5), 'col': 10, 'line': 5},
    60: {'pos': (17.5, 0), 'col': 10, 'line': 6},
    # -------colonne11--------
    61: {'pos': (17, 18.6),  'col':   11, 'line': 1},
    62: {'pos': (17, 15), 'col':  11, 'line': 2},
    63: {'pos': (17, 11.6), 'col': 11, 'line': 3},
    64: {'pos': (17, 8), 'col': 11, 'line': 4},
    65: {'pos': (17, 5), 'col': 11, 'line': 5},
    66: {'pos': (17, 0), 'col': 11, 'line': 6},
    # -------colonne12--------
    67: {'pos': (16.5, 18.6),  'col':   12, 'line': 1},
    68: {'pos': (16.5, 15), 'col':  12, 'line': 2},
    69: {'pos': (16.5, 11.6), 'col': 12, 'line': 3},
    70: {'pos': (16.5, 8), 'col': 12, 'line': 4},
    71: {'pos': (16.5, 5), 'col': 12, 'line': 5},
    72: {'pos': (16.5, 0), 'col': 12, 'line': 6},
    # -------colonne13--------
    73: {'pos': (16, 18.6),  'col':   13, 'line': 1},
    74: {'pos': (16, 15), 'col':  13, 'line': 2},
    75: {'pos': (16, 11.6), 'col': 13, 'line': 3},
    76: {'pos': (16, 8), 'col': 13, 'line': 4},
    77: {'pos': (16, 5), 'col': 13, 'line': 5},
    78: {'pos': (16, 0), 'col': 13, 'line': 6},
    # -------colonne14--------
    79: {'pos': (15.5, 18.6),  'col':   14, 'line': 1},
    80: {'pos': (15.5, 15), 'col':  14, 'line': 2},
    81: {'pos': (15.5, 11.6), 'col': 14, 'line': 3},
    82: {'pos': (15.5, 8), 'col': 14, 'line': 4},
    83: {'pos': (15.5, 5), 'col': 14, 'line': 5},
    84: {'pos': (15.5, 0), 'col': 14, 'line': 6},
    # -------colonne15--------
    85: {'pos': (15, 18.6),  'col':   15, 'line': 1},
    86: {'pos': (15, 15), 'col':  15, 'line': 2},
    87: {'pos': (15, 11.6), 'col': 15, 'line': 3},
    88: {'pos': (15, 8), 'col': 15, 'line': 4},
    89: {'pos': (15, 5), 'col': 15, 'line': 5},
    90: {'pos': (15, 0), 'col': 15, 'line': 6},
    # -------colonne16--------
    91: {'pos': (14.5, 18.6),  'col':   16, 'line': 1},
    92: {'pos': (14.5, 15), 'col':  16, 'line': 2},
    93: {'pos': (14.5, 11.6), 'col': 16, 'line': 3},
    94: {'pos': (14.5, 8), 'col': 16, 'line': 4},
    95: {'pos': (14.5, 5), 'col': 16, 'line': 5},
    96: {'pos': (14.5, 0),   'col': 16, 'line': 6},
    # *******************************************

    # -------colonne17--------
    97: {'pos': (9.5, 18.6),  'col':   17, 'line': 1},
    98: {'pos': (9.5, 15), 'col':  17, 'line': 2},
    99: {'pos': (9.5, 11.6), 'col': 17, 'line': 3},
    100: {'pos': (9.5,8), 'col': 17, 'line': 4},
    101: {'pos': (9.5,5), 'col': 17, 'line': 5},
    102: {'pos': (9.5,0),  'col': 17, 'line': 6},
    # -------colonne18--------
    103: {'pos': (8.7, 18.6),   'col':   18, 'line': 1},
    104: {'pos': (8.7, 15), 'col':  18, 'line': 2},
    105: {'pos': (8.7, 11.6),  'col': 18, 'line': 3},
    106: {'pos': (8.7, 8),  'col': 18, 'line': 4},
    107: {'pos': (8.7, 5),  'col': 18, 'line': 5},
    108: {'pos': (8.7, 0),    'col': 18, 'line': 6},
    # -------colonne19--------
    109: {'pos': (8.2, 18.6),   'col':   19, 'line': 1},
    110: {'pos': (8.2, 15), 'col':  19, 'line': 2},
    111: {'pos': (8.2, 11.6),  'col': 19, 'line': 3},
    112: {'pos': (8.2, 8),  'col': 19, 'line': 4},
    113: {'pos': (8.2, 5),  'col': 19, 'line': 5},
    114: {'pos': (8.2, 0),    'col': 19, 'line': 6},
    # -------colonne20--------
    115: {'pos': (7.7, 18.6),   'col':   20, 'line': 1},
    116: {'pos': (7.7, 15), 'col':  20, 'line': 2},
    117: {'pos': (7.7, 11.6),  'col': 20, 'line': 3},
    118: {'pos': (7.7, 8),  'col': 20, 'line': 4},
    119: {'pos': (7.7, 5),  'col': 20, 'line': 5},
    120: {'pos': (7.7, 0),    'col': 20, 'line': 6},
    # -------colonne21--------
    121: {'pos': (7.1, 18.6),   'col':   21, 'line': 1},
    122: {'pos': (7.1, 15), 'col':  21, 'line': 2},
    123: {'pos': (7.1, 11.6),  'col': 21, 'line': 3},
    124: {'pos': (7.1, 8),  'col': 21, 'line': 4},
    125: {'pos': (7.1, 5),  'col': 21, 'line': 5},
    126: {'pos': (7.1, 0),    'col': 21, 'line': 6},
    # -------colonne22--------
    127: {'pos': (6.6, 18.6),   'col':   22, 'line': 1},
    128: {'pos': (6.6, 15), 'col':  22, 'line': 2},
    129: {'pos': (6.6, 11.6),  'col': 22, 'line': 3},
    130: {'pos': (6.6, 8),  'col': 22, 'line': 4},
    131: {'pos': (6.6, 5),  'col': 22, 'line': 5},
    132: {'pos': (6.6, 0),    'col': 22, 'line': 6},
    # -------colonne23--------
    133: {'pos': (6.1, 18.6),   'col':  23, 'line': 1},
    134: {'pos': (6.1, 15), 'col': 23, 'line': 2},
    135: {'pos': (6.1, 11.6),  'col':23, 'line': 3},
    136: {'pos': (6.1, 8),  'col':23, 'line': 4},
    137: {'pos': (6.1, 5),  'col':23, 'line': 5},
    138: {'pos': (6.1, 0),    'col':23, 'line': 6},
    # -------colonne24--------
    139: {'pos': (5, 18.6),   'col':  24, 'line': 1},
    140: {'pos': (5, 15), 'col': 24, 'line': 2},
    141: {'pos': (5, 11.6),  'col':24, 'line': 3},
    142: {'pos': (5, 8),  'col':24, 'line': 4},
    143: {'pos': (5, 5),  'col':24, 'line': 5},
    144: {'pos': (5, 0),    'col':24, 'line': 6},
    # *********************************************

}


'''
EN CHANGEANT REST_X NE PAS OUBLIER DE CHANGER LA VALEUR DES COL
'''
# ---------------REST POSITIONS----------------
rest_positions = {
    # -------colonne r28--------
    145: {'pos': (28, 18.6),   'col':  "r28", 'line': 1},
    146: {'pos': (28, 15), 'col': "r28", 'line': 2}, 
    147: {'pos': (28, 11.6),  'col':"r28", 'line': 3},
    148: {'pos': (28, 8),  'col':"r28", 'line': 4},
    149: {'pos': (28, 5),  'col':"r28", 'line': 5},
    150: {'pos': (28, 0),    'col':"r28", 'line': 6},
    # -------colonne r10--------
    151: {'pos': (22, 18.6),   'col':  "r22", 'line': 1},
    152: {'pos': (22, 15), 'col': "r22", 'line': 2},
    153: {'pos': (22, 11.6),  'col':"r22", 'line': 3},
    154: {'pos': (22, 8),  'col':"r22", 'line': 4},
    155: {'pos': (22, 5),  'col':"r22", 'line': 5},
    156: {'pos': (22, 0),    'col':"r22", 'line': 6},
    # -------colonne r19--------
    157: {'pos': (19, 18.6),   'col':  "r19", 'line': 1},
    158: {'pos': (19, 15), 'col': "r19", 'line': 2},
    159: {'pos': (19, 11.6),  'col':"r19", 'line': 3},
    160: {'pos': (19, 8),  'col':"r19", 'line': 4},
    161: {'pos': (19, 5),  'col':"r19", 'line': 5},
    162: {'pos': (19, 0),    'col':"r19", 'line': 6},
    # -------colonne r13--------
    163: {'pos': (13, 18.6),   'col':  "r13", 'line': 1},
    164: {'pos': (13, 15), 'col': "r13", 'line': 2},
    165: {'pos': (13, 11.6),  'col':"r13", 'line': 3},
    166: {'pos': (13, 8),  'col':"r13", 'line': 4},
    167: {'pos': (13, 5),  'col':"r13", 'line': 5},
    168: {'pos': (13, 0),    'col':"r13", 'line': 6},
    # -------colonne r11--------
    169: {'pos': (11, 18.6),   'col':  "r11", 'line': 1},
    170: {'pos': (11, 15), 'col': "r11", 'line': 2},
    171: {'pos': (11, 11.6),  'col':"r11", 'line': 3},
    172: {'pos': (11, 8),  'col':"r11", 'line': 4},
    173: {'pos': (11, 5),  'col':"r11", 'line': 5},
    174: {'pos': (11, 0),    'col':"r11", 'line': 6},
    # -------colonne r4--------
    175: {'pos': (4, 18.6),   'col':  "r4", 'line': 1},
    176: {'pos': (4, 15), 'col': "r4", 'line': 2},
    177: {'pos': (4, 11.6),  'col':"r4", 'line': 3},
    178: {'pos': (4, 8),  'col':"r4", 'line': 4},
    179: {'pos': (4, 5),  'col':"r4", 'line': 5},
    180: {'pos': (4, 0),    'col':"r4", 'line': 6},
}

'''
def convertPixelsToCm(x):
    
    #To BE CHECKED 
    
    return x*4./659.
'''

'''
#convert the positions from pixels to cm
for node in positions:
    x, y = positions[node]['pos']
    positions[node]['pos'] = (convertPixelsToCm(x), convertPixelsToCm(y))

for node in rest_positions:
    x, y = rest_positions[node]['pos']
    rest_positions[node]['pos'] = (x, convertPixelsToCm(y))
'''
positions.update(rest_positions)
# Add nodes with positions to the graph
graph.add_nodes_from((node_id, attrs) for node_id, attrs in positions.items())

# Set the node positions as attributes in the graph
#nx.set_node_attributes(graph, positions)

# Calculate the Euclidean distance between two nodes in the real world (cm)
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
    for i in range(7):  # POUR LE MOMENT
        addEdge(nodeStart+i*6, nodeStart+(i+1)*6, coeff)

def linkBlockCols(start):
    # ------colonne1------
    linkCol(start, 1)

    # ------colonne2-->7------
    for i in range(1, 7):
        linkCol(start+6*i, 2)

    # ------colonne8------
    linkCol(start+7*6, 1)


def linkLineRest(rest, start):
    addEdge(rest, start,0.9)
    addEdge(rest,rest+6)
    addEdge(rest+6, start+6,0.9)


# Add edges to the graph with physical distances as edge weights

# ------Link Cols------
linkBlockCols(1)
linkBlockCols(49)
linkBlockCols(97)


# ------Line1---------
linkLine(1, 1.6)
# ------Line2---------
linkLine(2, 1.5)
# ------Line3---------
linkLine(3, 1.4)
# ------Line4---------
linkLine(4, 1.4)
# ------Line5---------
linkLine(5, 1.4)
# ------Line6---------
linkLine(6,0.75)
# ------Line1---------
linkLine(49, 1.6)
# ------Line2---------
linkLine(50, 1.5)
# ------Line3---------
linkLine(51, 1.4)
# ------Line4---------
linkLine(52, 1.4)
# ------Line5---------
linkLine(53, 1.4)
# ------Line6---------
linkLine(54,0.75)
# ------Line1---------
linkLine(97, 1.6)
# ------Line2---------
linkLine(98, 1.5)
# ------Line3---------
linkLine(99, 1.4)
# ------Line4---------
linkLine(100, 1.4)
# ------Line5---------
linkLine(101, 1.4)
# ------Line6---------
linkLine(102,0.75)


# -------------------LinkRest--------------------

#Add edges from the rest positions at the far left to the first column
addEdge(145,1,0.8) # When I am at the edge, I prefer to go laterally when I am just above the final destination
addEdge(146,2)
addEdge(147,3,0.8) # When I am at the edge, I prefer to go laterally when I am just above the final destination
addEdge(148,4)
addEdge(149,5,0.8) # When I am at the edge, I prefer to go laterally when I am just above the final destination
addEdge(150,6)

#Link the edges of the rest positions that are between the arenas to the corresponding column
linkLineRest(151, 43)
linkLineRest(152, 44)
linkLineRest(153, 45)
linkLineRest(154, 46)
linkLineRest(155, 47)
linkLineRest(156, 48)
linkLineRest(163, 91)
linkLineRest(164, 92)
linkLineRest(165, 93)
linkLineRest(166, 94)
linkLineRest(167, 95)
linkLineRest(168, 96)

#Add edges from the rest positions at the far right to the last column
addEdge(175,139,0.8) # When I am at the edge, I prefer to go laterally when I am just above the final destination
addEdge(176,140)
addEdge(177,141,0.8) # When I am at the edge, I prefer to go laterally when I am just above the final destination
addEdge(178,142)
addEdge(179,143,0.8) # When I am at the edge, I prefer to go laterally when I am just above the final destination
addEdge(180,144)

linkCol(145,0.9) # I prefer to move on the far left --> BUT CHECK !!!!!!!!
linkCol(151)
linkCol(157)
linkCol(163)
linkCol(169)
linkCol(175,0.9) # I prefer to move on the far right --> BUT CHECK !!!!!!!!


THRESHOLD_EXISTS_AT_POSITION = 0.01
def node_exists_at_position(x, y):
    for node, data in graph.nodes(data=True):
        if 'pos' in data and abs(data['pos'][0]-x)<THRESHOLD_EXISTS_AT_POSITION and abs(data['pos'][1])-y<THRESHOLD_EXISTS_AT_POSITION:
            return node
    return 0

# --------------NOT USED ANYMORE---------------------------
'''
def addDynamicNodeGoal(id, x, y, id_source):
    node = node_exists_at_position(x,y)
    if(node): 
        return node
    
    distances_to_new_node = {node: ((x - data['pos'][0])**2 + (
        y - data['pos'][1])**2)**0.5 for node, data in graph.nodes(data=True)}        
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
'''

#Add a node to the graph and connect it to the closest nodes
def addDynamicNode(id, x, y, id_source = 0, at_rest = False):
    '''
        If the node already exists, create a node right on it but specify that they have the same col and line
        If the node does not exist, create it and connect it to the closest nodes
            *If we are at_rest, connect to the two closest nodes that are not rest positions + the two closest rest position
            *If we are not at_rest, connect to the two closest nodes
    '''
    node = node_exists_at_position(x,y)
    if(node):
        s = graph.nodes[node]['col']
        l = graph.nodes[node]['line']
    elif id == 0:
        s = l = "s" # source
    else:
        s = l = "g" # goal

    ch = "r" + str(round(x))
    
    if at_rest:
        ch = "r" + str(round(x))

        distances_to_new_node = {node: ((x - data['pos'][0])**2 + (
            y - data['pos'][1])**2)**0.5 for node, data in graph.nodes(data=True)
                                        if 'col' in data and data['col'] != ch
        }
        closest_node = min(distances_to_new_node, key=distances_to_new_node.get)
        d = distances_to_new_node[closest_node]
        distances_to_new_node.pop(closest_node)

        closest_node1 = min(distances_to_new_node, key=distances_to_new_node.get)

        distances_to_rest_node = {
            node: abs(y - data['pos'][1])  for node, data in graph.nodes(data=True)
                                            if 'col' in data and data['col'] == ch
        }
        graph.add_node(id, pos=(x, y), col=ch)
        graph.add_edge(id, closest_node, weight=d*1.4)
        if(closest_node!=id_source):
            graph.add_edge(id, closest_node1,
                            weight=distances_to_new_node[closest_node1]*1.4)

        print(distances_to_rest_node)
        if len(distances_to_rest_node)>0:
            closest_node = min(distances_to_rest_node, key=distances_to_rest_node.get)
            d = distances_to_rest_node[closest_node]
            distances_to_rest_node.pop(closest_node)
            closest_node1 = min(distances_to_rest_node, key=distances_to_rest_node.get)

            graph.add_edge(id, closest_node, weight=d)

            graph.add_edge(id, closest_node1,
                            weight=distances_to_rest_node[closest_node1])
    else:
        distances_to_new_node = {node: ((x - data['pos'][0])**2 + (
            y - data['pos'][1])**2)**0.5 for node, data in graph.nodes(data=True)
        }
        closest_node = min(distances_to_new_node, key=distances_to_new_node.get)
        d = distances_to_new_node[closest_node]

        distances_to_new_node.pop(closest_node)

        closest_node1 = min(distances_to_new_node, key=distances_to_new_node.get)

        graph.add_node(id, pos=(x, y) ,col = s, line = l )

        graph.add_edge(id, closest_node, weight=d)
        if(closest_node!=id_source):
            graph.add_edge(id, closest_node1,
                           weight=distances_to_new_node[closest_node1])

    return id



# Find the shortest path based on physical distances
# The output is a list of nodes that the robot has to visit in order to reach the goal
# It does NOT contain the start position but it contains the goal position
def shortest_path(source,target,at_rest=False):
    '''
        Convention: 
            *node 0 is the source
            *node 200 is the goal
    '''
    id_source = addDynamicNode(0,source[0],source[1],at_rest = at_rest)
    id_goal = addDynamicNode(200,target[0],target[1],id_source)

    # Find the shortest path based on physical distances
    shortest_path = nx.shortest_path(graph, id_source, id_goal, weight='weight')
    i=1
    cols = False
    lines=False
    time.sleep(0.1)  #CHECK IF NEEDED

    node1 = graph.nodes[shortest_path[1]]
    node_source = graph.nodes[id_source]

    #If we are at a position that is not matching any col and line don't remove the two first nodes
    # of the shortest path (source + first destination) so start by i = 3
    if 'col' in node_source and 'line' in node_source:
        if node1['col'] != node_source['col'] and node1['line'] != node_source['line']:
            i=3


    #The task of these conditions is to remove the nodes that are on the same line or column
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


            if i < len(shortest_path) and not cols and 'line' in graph.nodes[shortest_path[i]] and 'line' in graph.nodes[shortest_path[i-1]]:
                if graph.nodes[shortest_path[i]]['line']==graph.nodes[shortest_path[i-1]]['line']:

                        shortest_path.pop(i-1)    
                        i=i-1
                        lines = True
                else:
                    if lines:        
                        if(len(shortest_path)-i>0):
                            #i = i + 1   
                            lines = False

            i=i+1



    #after setting the path remove the nodes of the source and goal from the graph 
    #since they are not needed anymore (only if they do not superpose with other nodes that are already in the graph)
    if(id_source == 0):
        graph.remove_node(0)
        #remove first element since its node will be removed
        if shortest_path[0]==0:
            shortest_path.pop(0)
    if(id_goal == 200):
        graph.remove_node(200)

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
plotGraph()




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

