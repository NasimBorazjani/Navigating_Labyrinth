
from collections import deque

def get_neighbors(state):
    blank_index = state.find('_')
    row, col = divmod(blank_index, 5)
    neighbors = []
    if row > 0:
        neighbors.append(swap(state, blank_index, blank_index - 5))
    if row < 3:
        neighbors.append(swap(state, blank_index, blank_index + 5))
    if col > 0:
        neighbors.append(swap(state, blank_index, blank_index - 1))
    if col < 4:
        neighbors.append(swap(state, blank_index, blank_index + 1))
    return neighbors

def swap(state, i, j):
    list_state = list(state)
    list_state[i], list_state[j] = list_state[j], list_state[i]
    return ''.join(list_state)

def solve(initial_board, target_words):
    initial_state = ''.join(map(lambda x: ''.join(x), initial_board))
    target_state = '#'.join(target_words)
    queue = deque([(initial_state, [])])
    visited = set([initial_state])
    while queue:
        state, actions = queue.popleft()
        if state == target_state:
            return actions
        for next_state in get_neighbors(state):
            if next_state not in visited:
                queue.append((next_state, actions + [next_state[state.find('_') + 5 * 2 + 2]]))
                visited.add(next_state)
    return []

initial_board = [['a', 'f', 'w', 'g', 'e'], ['p', 'f', 'l', 'm', 'y'], ['o', 'o', 'a', 'r', 'a'], ['g', 'a', 'm', 'e', 't'], ['p', 'u', '_', 'f', 'y']]
target_words = ['fage', 'palay', 'mowra', 'gemot', 'puffy']
print(solve(initial_board, target_words))
