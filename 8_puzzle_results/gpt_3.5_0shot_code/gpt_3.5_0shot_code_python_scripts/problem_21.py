
import heapq

def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != '_':
                x, y = divmod(state[i][j] - 1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance

def possible_moves(state):
    moves = []
    x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == '_')
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= x + dx < 3 and 0 <= y + dy < 3:
            new_state = [row.copy() for row in state]
            new_state[x][y], new_state[x + dx][y + dy] = new_state[x + dx][y + dy], new_state[x][y]
            moves.append(new_state)
    return moves

def a_star_search(initial_state, goal_state):
    heap = [(manhattan_distance(initial_state, goal_state), 0, initial_state, [])]
    visited = set()
    
    while heap:
        _, cost, state, path = heapq.heappop(heap)
        
        if state == goal_state:
            return path
        
        visited.add(tuple(map(tuple, state)))
        
        for move in possible_moves(state):
            if tuple(map(tuple, move)) not in visited:
                new_cost = cost + 1
                heapq.heappush(heap, (new_cost + manhattan_distance(move, goal_state), new_cost, move, path + [move[x][y]]))

initial_state = [[25, 71, 58], [61, 94, 53], [50, 18, '_']]
goal_state = [[94, 71, 58], [61, 53, 50], [25, 18, '_']]

solution = a_star_search(initial_state, goal_state)
print(solution)
