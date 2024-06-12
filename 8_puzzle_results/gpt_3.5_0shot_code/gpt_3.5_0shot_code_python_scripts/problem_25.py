
import heapq

def manhattan_distance(state):
    goal_state = [[45, 13, 12], [66, 41, 76], [85, 21, 74]]
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != '_':
                x, y = divmod(state[i][j] - 1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_row, empty_col = next((i, j) for i in range(3) for j in range(3) if state[i][j] == '_')
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = empty_row + dr, empty_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row.copy() for row in state]
            new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
            neighbors.append((new_state, (new_row, new_col)))
    return neighbors

def a_star_search(initial_state):
    heap = [(manhattan_distance(initial_state), 0, initial_state, [])]
    visited = set()
    
    while heap:
        _, cost, state, path = heapq.heappop(heap)
        
        if state == [[45, 13, 12], [66, 41, 76], [85, 21, 74]]:
            return path
        
        visited.add(str(state))
        
        for neighbor, move in get_neighbors(state):
            if str(neighbor) not in visited:
                new_cost = cost + 1
                priority = new_cost + manhattan_distance(neighbor)
                heapq.heappush(heap, (priority, new_cost, neighbor, path + [neighbor[move[0]][move[1]]]))

initial_state = [[45, 13, 12], [66, 41, 76], [85, 21, 74]]
solution = a_star_search(initial_state)
print(solution)
