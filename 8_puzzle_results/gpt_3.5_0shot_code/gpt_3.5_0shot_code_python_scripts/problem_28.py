
import heapq

def manhattan_distance(state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, '_']]
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != '_':
                num = state[i][j]
                x_goal, y_goal = divmod(num - 1, 3)
                distance += abs(x_goal - i) + abs(y_goal - j)
    return distance

def get_neighbors(state):
    neighbors = []
    x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == '_')
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row.copy() for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def a_star_search(initial_state):
    heap = [(manhattan_distance(initial_state), 0, initial_state, [])]
    visited = set()
    
    while heap:
        _, cost, state, path = heapq.heappop(heap)
        
        if state == [[1, 2, 3], [4, 5, 6], [7, 8, '_']]:
            return path
        
        visited.add(str(state))
        
        for neighbor in get_neighbors(state):
            if str(neighbor) not in visited:
                new_cost = cost + 1
                new_path = path + [neighbor[x][y]]
                heapq.heappush(heap, (new_cost + manhattan_distance(neighbor), new_cost, neighbor, new_path))

initial_state = [[10, 81, 46], [87, 74, 72], [36, 45, '_']]
solution = a_star_search(initial_state)
print(solution)
