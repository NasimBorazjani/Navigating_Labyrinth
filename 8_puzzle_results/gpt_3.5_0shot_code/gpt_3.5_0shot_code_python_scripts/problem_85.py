
import heapq

def manhattan_distance(state):
    goal_state = [[93, 26, 39, 51, 69], [27, '_', 43, 7, 89], [63, 91, 23, 68, 17]]
    distance = 0
    for i in range(3):
        for j in range(5):
            if state[i][j] != '_':
                x, y = divmod(goal_state.index(state[i][j]), 5)
                distance += abs(i - x) + abs(j - y)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_i, empty_j = [(i, j) for i in range(3) for j in range(5) if state[i][j] == '_'][0]
    for move_i, move_j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i, new_j = empty_i + move_i, empty_j + move_j
        if 0 <= new_i < 3 and 0 <= new_j < 5:
            new_state = [row.copy() for row in state]
            new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]
            neighbors.append((new_state, (new_i, new_j)))
    return neighbors

def a_star_search(initial_state):
    frontier = [(manhattan_distance(initial_state), 0, initial_state, [])]
    heapq.heapify(frontier)
    visited = set()
    
    while frontier:
        _, cost, state, path = heapq.heappop(frontier)
        
        if state == [[93, 26, 39, 51, 69], [27, '_', 43, 7, 89], [63, 91, 23, 68, 17]]:
            return path
        
        visited.add(str(state))
        
        for neighbor_state, move in get_neighbors(state):
            if str(neighbor_state) not in visited:
                new_cost = cost + 1 + manhattan_distance(neighbor_state)
                heapq.heappush(frontier, (new_cost, cost + 1, neighbor_state, path + [neighbor_state[move[0]][move[1]]]))

initial_state = [[93, 26, 39, 51, 69], [27, '_', 43, 7, 89], [63, 91, 23, 68, 17]]
solution = a_star_search(initial_state)
print(solution)
