
import heapq
import copy

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(4):
            if state[i][j] != '_':
                x, y = divmod(state[i][j]-1, 4)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_moves(state):
    moves = []
    for i in range(3):
        for j in range(4):
            if state[i][j] == '_':
                if i > 0: moves.append((i-1, j))
                if i < 2: moves.append((i+1, j))
                if j > 0: moves.append((i, j-1))
                if j < 3: moves.append((i, j+1))
    return moves

def solve(initial_state):
    goal_state = [[74, 70, 54, 37], [33, 22, 21, 11], [9, 4, 2, '_']]
    queue = [(manhattan_distance(initial_state), initial_state, [])]
    visited = set()

    while queue:
        _, state, path = heapq.heappop(queue)
        if state == goal_state:
            return path
        for move in get_moves(state):
            new_state = copy.deepcopy(state)
            i, j = move
            x, y = divmod(path[-1] if path else 0, 4)
            new_state[x][y], new_state[i][j] = new_state[i][j], new_state[x][y]
            if str(new_state) not in visited:
                visited.add(str(new_state))
                heapq.heappush(queue, (manhattan_distance(new_state) + len(path), new_state, path + [new_state[i][j]]))

initial_state = [[74, 37, 2, 22], [4, 21, '_', 54], [33, 70, 9, 11]]
print(solve(initial_state))
