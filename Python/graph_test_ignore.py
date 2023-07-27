import networkx as nx
import matplotlib.pyplot as plt
# Create an empty graph
graph = nx.Graph()

# Define positions, col, and line attributes for each node
positions = {
    # -------colonne1--------
    1: {'pos': (27, 57), 'col': 1, 'line': 1},
    2: {'pos': (27, 627), 'col': 1, 'line': 2},
    3: {'pos': (27, 1219), 'col': 1, 'line': 3},
    # Add more nodes and their attributes here...
}

# Add nodes with positions and other attributes to the graph
graph.add_nodes_from(positions)

# Set the node attributes in the graph
nx.set_node_attributes(graph, positions)

# Accessing attributes of a specific node
node_1_attributes = graph.nodes[1]
print(node_1_attributes)
# Output: {'pos': (27, 57), 'col': 1, 'line': 1}

# Accessing a specific attribute of a node
node_2_col = graph.nodes[2]['col']
print(node_2_col)
# Output: 1
pos = nx.get_node_attributes(graph, 'pos')
nx.draw(graph, pos, with_labels=True, node_size=500, font_size=12)
edge_labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

plt.show()