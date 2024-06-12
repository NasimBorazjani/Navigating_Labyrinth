
from queue import PriorityQueue

def manhattan_distance(state):
    goal_state = [[72, 92, 85, 78, 74], [70, 67, 50, 75, 66], [48, 42, 32, 26, '_']]
    distance = 0
    for i in range(3):
        for j in range(5):
            if state[i][j] != '_':
                x, y = divmod(state[i][j] - 1, 5)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_i, empty_j = None, None
    for i in range(3):
        for j in range(5):
            if state[i][j] == '_':
                empty_i, empty_j = i, j
                break
    for i, j in [(empty_i-1, empty_j), (empty_i+1, empty_j), (empty_i, empty_j-1), (empty_i, empty_j+1)]:
        if 0 <= i < 3 and 0 <= j < 5:
            new_state = [row.copy() for row in state]
            new_state[empty_i][empty_j], new_state[i][j] = new_state[i][j], new_state[empty_i][empty_j]
            neighbors.append(new_state)
    return neighbors

def solve_puzzle(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {tuple(map(tuple, initial_state)): None}
    g_score = {tuple(map(tuple, initial_state)): 0}
    
    while not frontier.empty():
        current = frontier.get()[1]
        
        if current == [[72, 92, 85, 78, 74], [70, 67, 50, 75, 66], [48, 42, 32, 26, '_']]:
            path = []
            while current != initial_state:
                path.append(current[2][4])
                current = came_from[tuple(map(tuple, current))]
            return path[::-1]
        
        for neighbor in get_neighbors(current):
            new_g_score = g_score[tuple(map(tuple, current))] + 1
            if tuple(map(tuple, neighbor)) not in g_score or new_g_score < g_score[tuple(map(tuple, neighbor))]:
                g_score[tuple(map(tuple, neighbor))] = new_g_score
                priority = new_g_score + manhattan_distance(neighbor)
                frontier.put((priority, neighbor))
                came_from[tuple(map(tuple, neighbor))] = current
    
    return None

initial_state = [[72, 92, '_', 78, 74], [70, 67, 85, 75, 66], [48, 42, 32, 26, 50]]
solution = solve_puzzle(initial_state)
print(solution)
