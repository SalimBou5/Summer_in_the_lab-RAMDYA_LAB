import time
import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
graph = nx.Graph()

# Define positions (physical coordinates) for each node
positions = {
    # -------colonne1--------
    1: (27, 57),
    2: (27, 627),
    3: (27, 1219),
    4: (27, 1781),
    5: (27, 2370),
    6: (27, 2925),
    # -------colonne2--------
    7: (109, 57),
    8: (109, 627),
    9: (109, 1219),
    10: (117, 1781),
    11: (121, 2370),
    12: (121, 2925),
    # ------colonne3--------
    13: (200, 57),
    14: (200, 627),
    15: (207, 1219),
    16: (207, 1781),
    17: (213, 2370),
    18: (213, 2925),
    # -------colonne4--------
    19: (287, 57),
    20: (287, 627),
    21: (293, 1219),
    22: (293, 1781),
    23: (300, 2370),
    24: (300, 2925),
    # -------colonne5--------
    25: (369, 57),
    26: (369, 627),
    27: (373, 1219),
    28: (373, 1781),
    29: (377, 2370),
    30: (377, 2925),
    # -------colonne6--------
    31: (457, 57),
    32: (457, 627),
    33: (461, 1219),
    34: (461, 1781),
    35: (465, 2370),
    36: (465, 2925),
    # -------colonne7--------
    37: (555, 57),
    38: (555, 627),
    39: (555, 1219),
    40: (555, 1781),
    41: (555, 2370),
    42: (555, 2925),
    # ************************************************************
    # -------colonne8--------
    43: (1500, 52),
    44: (1500, 617),
    45: (1500, 1214),
    46: (1500, 1775),
    47: (1500, 2362),
    48: (1500, 2925),
    # -------colonne9--------
    49: (1607, 52),
    50: (1607, 617),
    51: (1609, 1214),
    52: (1610, 1775),
    53: (1611, 2362),
    54: (1612, 2927),
    # -------colonne10--------
    55: (1691, 52),
    56: (1691, 617),
    57: (1696, 1214),
    58: (1696, 1775),
    59: (1699, 2362),
    60: (1699, 2927),
    # -------colonne11--------
    61: (1779, 52),
    62: (1779, 617),
    63: (1783, 1214),
    64: (1783, 1775),
    65: (1787, 2362),
    66: (1787, 2927),
    # -------colonne12--------
    67: (1866, 52),
    68: (1866, 617),
    69: (1868, 1214),
    70: (1868, 1775),
    71: (1870, 2362),
    72: (1870, 2927),
    # -------colonne13--------
    73: (1952, 52),
    74: (1952, 617),
    75: (1955, 1214),
    76: (1955, 1775),
    77: (1959, 2362),
    78: (1959, 2927),
    # -------colonne14--------
    79: (2043, 52),
    80: (2043, 617),
    81: (2043, 1214),
    82: (2043, 1775),
    83: (2043, 2362),
    84: (2043, 2927),
    # *******************************************
    # -------colonne15--------
    85: (3011, 52),
    86: (3011, 617),
    87: (3011, 1214),
    88: (3011, 1775),
    89: (3011, 2362),
    90: (3011, 2927),
    # -------colonne16--------
    91: (3101, 52),
    92: (3101, 617),
    93: (3104, 1214),
    94: (3104, 1775),
    95: (3106, 2362),
    96: (3106, 2927),
    # -------colonne17--------
    97: (3187, 52),
    98: (3187, 617),
    99: (3190, 1214),
    100: (3190, 1775),
    101: (3194, 2362),
    102: (3194, 2927),
    # -------colonne18--------
    103: (3273, 52),
    104: (3273, 617),
    105: (3277, 1214),
    106: (3277, 1775),
    107: (3278, 2362),
    108: (3278, 2927),
    # -------colonne20--------
    109: (3359, 52),
    110: (3359, 617),
    111: (3362, 1214),
    112: (3362, 1775),
    113: (3366, 2362),
    114: (3366, 2927),
    # -------colonne20--------
    115: (3447, 52),
    116: (3447, 617),
    117: (3450, 1214),
    118: (3450, 1775),
    119: (3454, 2362),
    120: (3454, 2927),
    # -------colonne21--------
    121: (3537, 52),
    122: (3537, 617),
    123: (3537, 1214),
    124: (3537, 1775),
    125: (3537, 2362),
    126: (3537, 2927),
    # *********************************************
    # ---------------REST POSITIONS----------------
    127: (1040, 617),
    128: (1040, 1775),
    129: (1040, 2927),
    130: (2516, 617),
    131: (2516, 1775),
    132: (2516, 2927),


}

# Add nodes with positions to the graph
graph.add_nodes_from(positions)

# Set the node positions as attributes in the graph
nx.set_node_attributes(graph, positions, 'pos')

# Calculate the Euclidean distance between two nodes in the real world


def distance(node1, node2):
    x1, y1 = positions[node1]
    x2, y2 = positions[node2]
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5


def addEdge(node1, node2, coeff=1):
    graph.add_edge(node1, node2, weight=distance(node1, node2)*coeff)


def linkCol(nodeStart, coeff=1):
    for i in range(5):
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
linkLine(1, 2)
# ------Line2---------
linkLine(2, 1.5)
# ------Line3---------
linkLine(3, 1.5)
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


# --------------CHECK---------------------------
def addDynamicNodeGoal(id, x, y):
    distances_to_new_node = {node: ((x - data['pos'][0])**2 + (
        y - data['pos'][1])**2)**0.5 for node, data in graph.nodes(data=True)}
    closest_node = min(distances_to_new_node, key=distances_to_new_node.get)
    graph.add_node(id, pos=(x, y))
    graph.add_edge(id, closest_node,
                   weight=distances_to_new_node[closest_node])
    graph.add_edge(id, closest_node+1,
                   weight=distances_to_new_node[closest_node+1])
    graph.add_edge(id, closest_node+6,
                   weight=distances_to_new_node[closest_node+6])
    graph.add_edge(id, closest_node+7,
                   weight=distances_to_new_node[closest_node+7])


def addDynamicNodePos(id, x, y):
    distances_to_new_node = {node: ((x - data['pos'][0])**2 + (
        y - data['pos'][1])**2)**0.5 for node, data in graph.nodes(data=True)}
    closest_node = min(distances_to_new_node, key=distances_to_new_node.get)
    # distances_to_new_node.remove(closest_node)
    closest_node1 = min(distances_to_new_node, key=distances_to_new_node.get)
    graph.add_node(id, pos=(x, y))
    graph.add_edge(id, closest_node,
                   weight=distances_to_new_node[closest_node])
    graph.add_edge(id, closest_node1,
                   weight=distances_to_new_node[closest_node1])


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


# Find the shortest path based on physical distances
shortest_path = nx.shortest_path(graph, source=1, target=97, weight='weight')
# graph.remove_node(300)
print(time.time()-t0)
print("Shortest path based on physical distances:", shortest_path)



# Visualize the graph with node positions
pos = nx.get_node_attributes(graph, 'pos')
nx.draw(graph, pos, with_labels=True, node_size=500, font_size=12)

# You can also draw edges with attributes (e.g., weights)
# edge_labels = nx.get_edge_attributes(graph, 'weight')
# nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

plt.show()
