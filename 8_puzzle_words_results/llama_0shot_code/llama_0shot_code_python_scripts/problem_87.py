
from collections import deque

def get_neighbors(state):
    blank_index = state.find('_')
    row, col = divmod(blank_index, 5)
    neighbors = []
    if row > 0:
        neighbors.append((state[0:blank_index - 1] + state[blank_index] + state[blank_index - 1] + state[blank_index + 1:], 'up-left'))
    if row < 3:
        neighbors.append((state[0:blank_index - 5] + state[blank_index] + state[blank_index - 5] + state[blank_index + 1:], 'down-right'))
    if col > 0:
        neighbors.append((state[0:blank_index - 5] + state[blank_index] + state[blank_index - 1] + state[blank_index + 1:], 'up-right'))
    if col < 4:
        neighbors.append((state[0:blank_index - 1] + state[blank_index] + state[blank_index - 5] + state[blank_index + 1:], 'down-left'))
    return neighbors

def solve_puzzle(initial_board, target_words):
    initial_state = '#'.join([''.join(row) for row in initial_board])
    target_state = '#' + '#'.join(target_words)
    queue = deque([(initial_state, [])])
    visited = set([initial_state])
    while queue:
        state, actions = queue.popleft()
        if state == target_state:
            return actions[::-1]
        for next_state, action in get_neighbors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, [action] + actions))
    return None

initial_board = [['e', 'e', 'l', 'h', 'o'], ['m', 'r', 't', 'u', 'n'], ['p', 'e', '_', 'c', 'i'], ['t', 'c', 'l', 'h', 'p'], ['m', 'u', 'i', 'g', 'a']]
target_words = ['echo', 'metin', 'perch', 'tulip', 'mulga']
print(solve_puzzle(initial_board, target_words))
