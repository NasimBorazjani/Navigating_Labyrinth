
from collections import deque

def get_moves(state):
    moves = []
    for i, stack in enumerate(state):
        if stack:
            for j, target in enumerate(state):
                if i != j and (not target or target[-1] == stack[-1]) and len(target) < 4:
                    moves.append((i, j))
    return moves

def bfs(start):
    queue = deque([(start, [])])
    visited = set([start])
    while queue:
        state, path = queue.popleft()
        if all(len(set(stack)) <= 1 for stack in state):
            return path
        for move in get_moves(state):
            new_state = state[:]
            new_state[move[1]] = new_state[move[1]] + [new_state[move[0]].pop()]
            if tuple(new_state) not in visited:
                queue.append((new_state, path + [move]))
                visited.add(tuple(new_state))

stacks = [[], ['Blue', 'Yellow', 'Blue', 'Yellow'], [], [], ['Red', 'Blue', 'Yellow', 'Green'], ['Green', 'Green', 'Red', 'Red']]
print(bfs(stacks))
