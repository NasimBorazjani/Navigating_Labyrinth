
from queue import PriorityQueue

def bfs(initial_state, goal_state, costs):
    queue = PriorityQueue()
    queue.put((0, initial_state, []))
    visited = set()
    while not queue.empty():
        cost, state, path = queue.get()
        if state == goal_state:
            return path
        if state in visited:
            continue
        visited.add(state)
        for next_state, move in possible_moves(state):
            next_cost = cost + costs[move[1]]
            queue.put((next_cost, next_state, path + [move]))
    return []

def possible_moves(state):
    moves = []
    for i in range(len(state)):
        for j in range(len(state)):
            if i != j and state[i] and (not state[j] or state[i][-1] == state[j][-1]):
                next_state = state[:]
                next_state[j] = next_state[j] + [next_state[i].pop()]
                moves.append((next_state, (i, j)))
    return moves

initial_state = [[], [], ['Green', 'Blue', 'Blue', 'Blue'], ['Yellow', 'Red', 'Yellow', 'Red'], ['Green', 'Red', 'Green', 'Yellow'], []]
goal_state = [['Blue', 'Blue', 'Blue'], ['Red', 'Red', 'Red'], ['Green', 'Green', 'Green'], ['Yellow', 'Yellow', 'Yellow'], [], []]
costs = {0: 1, 1: 7, 2: 2, 3: 4, 4: 6, 5: 5}

print(bfs(initial_state, goal_state, costs))
