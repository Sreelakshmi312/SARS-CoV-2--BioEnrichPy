import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from community import community_louvain
from collections import Counter

# Load the Excel file
file_path = "file-name"  # Replace with your file name
df = pd.read_excel(file_path)

# Standardize column names
df.columns = ['viral', 'human']

# Create graph from interactions
G = nx.Graph()
for _, row in df.iterrows():
    viral = row['viral']
    human = row['human']
    G.add_edge(viral, human)

# Louvain clustering
partition = community_louvain.best_partition(G)

# Get top cluster
cluster_counts = Counter(partition.values())
top_cluster_id = cluster_counts.most_common(1)[0][0]
top_nodes = [node for node in G.nodes if partition[node] == top_cluster_id]
top_subgraph = G.subgraph(top_nodes)

# Identify viral vs human nodes
viral_nodes = set(df['viral'].unique())

# Layout: Spring layout with increased spacing
pos = nx.spring_layout(top_subgraph, k=1.5, seed=42)

# Node colors
node_colors = ['red' if node in viral_nodes else 'skyblue' for node in top_subgraph.nodes]

# Plotting
plt.figure(figsize=(24, 20))  # Increase canvas size
nx.draw_networkx_edges(top_subgraph, pos, alpha=0.1, edge_color='gray', width=0.3)
nx.draw_networkx_nodes(top_subgraph, pos, node_color=node_colors, node_size=800, edgecolors='black', linewidths=1.2)
nx.draw_networkx_labels(top_subgraph, pos, font_size=6, font_weight='bold')  # Smaller labels

plt.title("Top Cluster Visualization", fontsize=20)
plt.axis('off')
plt.tight_layout()
plt.savefig("top_cluster.png", dpi=600)
plt.show()
