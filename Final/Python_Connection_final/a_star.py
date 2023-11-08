import heapq
# import time
li = []
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def astar(graph, start, goal):
    open_set = [(0, start)]
    closed_set = set()
    g_scores = {node: float('inf') for node in graph.graph}
    g_scores[start] = 0
    came_from = {}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = reconstruct_path(came_from, current,graph)
            return path

        closed_set.add(current)

        for neighbor, cost in graph.graph[current].items():  # Iterate over keys and values of the dictionary
            if neighbor in closed_set:
                continue

            tentative_g_score = g_scores[current] + cost
            if tentative_g_score < g_scores[neighbor]:
                came_from[neighbor] = current
                g_scores[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))
                # print(f"{neighbor}...{f_score}...Sleeping {cost}")
                # time.sleep(cost)  

    return None  # No path found

def reconstruct_path(came_from, current, graph):
    path = [current]
    while current in came_from:
        previous = came_from[current]
        cost = graph.graph[previous][current]  # Access the cost directly from the graph attribute
        li.append(cost)
        # print(f"sleeping..{cost}to{current}")
        # time.sleep(cost)  # Sleep for the cost of the edge
        path.insert(0, previous)
        current = previous
    return path



def heuristic(node, goal):
    # In this example, we'll use a simple heuristic that assumes zero cost to reach the goal.
    return 0

    # Create a sample directed graph
def a_starr(start,end):
    graph = Graph()
    graph.add_edge("A", {"B": 0.95, "C": 1.27})
    graph.add_edge("B", {"A": 0.95 })
    graph.add_edge("C", {"D": 1.91,"E": 1.81,"A":1.27})
    graph.add_edge("D", {"C": 1.91,"E": 1.50,"F":1.68,"H":1.47})
    graph.add_edge("E", {"D": 1.50,"C": 1.81})
    graph.add_edge("F", {"D": 1.68,"G": 1.66})
    graph.add_edge("G", {"F":1.66})
    graph.add_edge("H", {"D": 1.47,"K": 1.75 , "I":1.46 ,"L":1.93})
    graph.add_edge("I", {"H": 1.46,"J": 2.43})
    graph.add_edge("J", {"I": 1.43,"K": 1.59})
    graph.add_edge("K", {"H": 1.75,"J": 1.59,"L":1.12})
    graph.add_edge("L", {"K": 1.12,"M": 2.02,"N":1.60 ,"H":1.93})
    graph.add_edge("M", {"L":2.02})
    graph.add_edge("N", {"L":1.60})

    start_node = start
    goal_node = end

    path = astar(graph, start_node, goal_node)

    if path:
        print(f"Shortest path from {start_node} to {goal_node}: {path}")
    else:
        print(f"No path found from {start_node} to {goal_node}")
    return path

# def cost(src,des):
#     [x,y,z] = src
#     [a,b,c] = des
#     i = abs(x-a)
#     j = abs(y-b)
#     k = abs(z-c)
#     return (i+j+k)*10
    
    
if __name__=="__main__":
     path = a_starr("G","N")
     print(li)
