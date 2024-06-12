
import heapq

def manhattan_distance(state):
    goal_state = [[93, 81, 68, 57, 28, 6], [55, 54, 58, 69, 38, 10], [21, 19, 18, 44, 51, '_']]
    distance = 0
    for i in range(3):
        for j in range(6):
            if state[i][j] != '_':
                x, y = divmod(state[i][j] - 1, 6)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_i, empty_j = None, None
    for i in range(3):
        for j in range(6):
            if state[i][j] == '_':
                empty_i, empty_j = i, j
                break
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i, new_j = empty_i + di, empty_j + dj
        if 0 <= new_i < 3 and 0 <= new_j < 6:
            new_state = [row.copy() for row in state]
            new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]
            neighbors.append(new_state)
    return neighbors

def a_star_search(initial_state):
    heap = [(manhattan_distance(initial_state), 0, initial_state, [])]
    visited = set()
    
    while heap:
        _, cost, state, path = heapq.heappop(heap)
        
        if state == [[93, 81, 68, 57, 28, 6], [55, 54, 58, 69, 38, 10], [21, 19, 18, 44, 51, '_']]:
            return path
        
        visited.add(str(state))
        
        for neighbor in get_neighbors(state):
            if str(neighbor) not in visited:
                new_cost = cost + 1
                heapq.heappush(heap, (new_cost + manhattan_distance(neighbor), new_cost, neighbor, path + [neighbor[empty_i][empty_j]]))

initial_state = [[93, 81, 68, 57, 28, 6], [55, 54, 58, 69, 38, 10], [21, '_', 19, 44, 51, 18]]
solution = a_star_search(initial_state)
print(solution)
