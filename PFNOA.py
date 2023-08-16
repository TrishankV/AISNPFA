from queue import PriorityQueue
import random

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    # Create a priority queue to store the cells to explore
    frontier = PriorityQueue()
    frontier.put(start, 0)
    
    # Create dictionaries to store the cost of reaching a cell and the previous cell
    cost_so_far = {}
    came_from = {}
    cost_so_far[start] = 0
    came_from[start] = None
    
    while not frontier.empty():
        current = frontier.get()
        
        # Check if we have reached the goal
        if current == goal:
            break
        
        # Explore the neighbors of the current cell
        for next in neighbors(grid, current):
            new_cost = cost_so_far[current] + 1 # Assume all movements have a cost of 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
    
    # Reconstruct the path from the goal to the start
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    
    return path

def neighbors(grid, current):
    # Returns the list of valid neighbors of the current cell
    x, y = current
    neighbors = []
    
    if x > 0 and grid[x-1][y] == 0:
        neighbors.append((x-1, y))
    if x < len(grid)-1 and grid[x+1][y] == 0:
        neighbors.append((x+1, y))
    if y > 0 and grid[x][y-1] == 0:
        neighbors.append((x, y-1))
    if y < len(grid[0])-1 and grid[x][y+1] == 0:
        neighbors.append((x, y+1))
    
    return neighbors

def generate_grid(size, obstacle_probability):
    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            if random.random() < obstacle_probability:
                row.append(1) # Add an obstacle
            else:
                row.append(0) # Add an empty cell
        grid.append(row)
    return grid

# Example usage
grid_size = 10
obstacle_probability = 0.2

grid = generate_grid(grid_size, obstacle_probability)
start = (0, 0)
goal = (grid_size-1, grid_size-1)

path = a_star(grid, start, goal)

# Print the grid and the path
for i in range(grid_size):
    row = ''
    for j in range(grid_size):
        if (i, j) in path:
            row += 'P'
        elif grid[i][j] == 1:
            row += 'o'
        else:
            row += '.'
    print(row)

# Print the final path
print("Final path:", path)
