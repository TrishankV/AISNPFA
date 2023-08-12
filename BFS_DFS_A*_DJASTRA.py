import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue

# Create a sample graph
G = nx.Graph()
edges = [
    (1, 2, {'weight': 2}),
    (1, 3, {'weight': 4}),
    (2, 4, {'weight': 1}),
    (2, 5, {'weight': 3}),
    (3, 6, {'weight': 2}),
    (4, 5, {'weight': 2}),
    (5, 6, {'weight': 3}),
]
G.add_edges_from(edges)

# Define algorithms
def a_star(graph, start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph.nodes}
    g_score[start] = 0

    while not open_list.empty():
        _, current = open_list.get()

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in graph.neighbors(current):
            tentative_g_score = g_score[current] + graph[current][neighbor]['weight']
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = g_score[neighbor] + heuristic(neighbor, goal)
                open_list.put((f_score, neighbor))

    return None

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def heuristic(node, goal):
    return abs(node - goal)  # Simple heuristic for demonstration

def dijkstra(graph, start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph.nodes}
    g_score[start] = 0

    while not open_list.empty():
        _, current = open_list.get()

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in graph.neighbors(current):
            tentative_g_score = g_score[current] + graph[current][neighbor]['weight']
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                open_list.put((g_score[neighbor], neighbor))

    return None

def bfs(graph, start, goal):
    queue = [start]
    visited = set()
    came_from = {}

    while queue:
        current = queue.pop(0)

        if current == goal:
            return reconstruct_path(came_from, current)

        visited.add(current)

        for neighbor in graph.neighbors(current):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
                came_from[neighbor] = current

    return None

def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    came_from = {}

    while stack:
        current = stack.pop()

        if current == goal:
            return reconstruct_path(came_from, current)

        visited.add(current)

        for neighbor in graph.neighbors(current):
            if neighbor not in visited and neighbor not in stack:
                stack.append(neighbor)
                came_from[neighbor] = current

    return None

# Define start and goal nodes
start_node = 1
goal_node = 6

# Run algorithms
a_star_path = a_star(G, start_node, goal_node)
dijkstra_path = dijkstra(G, start_node, goal_node)
bfs_path = bfs(G, start_node, goal_node)
dfs_path = dfs(G, start_node, goal_node)

print("Paths found by different algorithms:")
print("A* Path:", a_star_path)
print("Dijkstra's Path:", dijkstra_path)
print("BFS Path:", bfs_path)
print("DFS Path:", dfs_path)

# Visualize the graph and paths
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000)
nx.draw_networkx_nodes(G, pos, nodelist=[start_node, goal_node], node_color='g', node_size=1000)
if a_star_path:
    nx.draw_networkx_edges(G, pos, edgelist=list(zip(a_star_path, a_star_path[1:])), edge_color='r', width=2)
if dijkstra_path:
    nx.draw_networkx_edges(G, pos, edgelist=list(zip(dijkstra_path, dijkstra_path[1:])), edge_color='b', width=2)
if bfs_path:
    nx.draw_networkx_edges(G, pos, edgelist=list(zip(bfs_path, bfs_path[1:])), edge_color='y', width=2)
if dfs_path:
    nx.draw_networkx_edges(G, pos, edgelist=list(zip(dfs_path, dfs_path[1:])), edge_color='purple', width=2)

plt.show()
