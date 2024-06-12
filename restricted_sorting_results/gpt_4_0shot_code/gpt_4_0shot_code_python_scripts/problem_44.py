
import heapq

def get_moves(state):
    moves = []
    for i, stack in enumerate(state):
        if stack:
            for j, target in enumerate(state):
                if i != j and (not target or target[-1] == stack[-1]):
                    moves.append((i, j))
    return moves

def get_cost(move, costs):
    return costs[move[1]]

def is_sorted(state):
    for stack in state:
        if len(set(stack)) > 1:
            return False
    return True

def restricted_sorting(state, costs):
    queue = [(0, state, [])]
    visited = set()

    while queue:
        cost, state, path = heapq.heappop(queue)
        if str(state) in visited:
            continue
        visited.add(str(state))
        if is_sorted(state):
            return path
        for move in get_moves(state):
            new_state = state[:]
            new_state[move[1]] = new_state[move[1]] + [new_state[move[0]].pop()]
            new_cost = cost + get_cost(move, costs)
            heapq.heappush(queue, (new_cost, new_state, path + [move]))

state = [[], [], ['Blue', 'Blue', 'Green', 'Black', 'Red'], [], ['Red', 'Green', 'Red', 'Black', 'Yellow'], [], ['Blue', 'Yellow', 'Green', 'Yellow', 'Black'], ['Yellow', 'Green', 'Black', 'Red', 'Blue']]
costs = {0: 6, 1: 2, 2: 7, 3: 1, 4: 1, 5: 5, 6: 3, 7: 2}

print(restricted_sorting(state, costs))
