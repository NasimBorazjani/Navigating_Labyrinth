
from collections import deque

def generate_next_states(state):
    next_states = []
    blank_row, blank_col = state['blank']
    for dr, dc in [(-1, 1), (1, 1), (-1, -1), (1, -1)]: # up-right, down-right, up-left, down-left
        new_row, new_col = blank_row + dr, blank_col + dc
        if 0 <= new_row < len(state['board']) and 0 <= new_col < len(state['board'][0]):
            new_state = [row.copy() for row in state['board']]
            new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
            new_state = {'board': new_state, 'blank': (new_row, new_col)}
            next_states.append(new_state)
    return next_states

def is_target_state(state, target_words):
    board = state['board']
    for i, word in enumerate(target_words):
        for j, char in enumerate(word):
            if board[i][j] != char:
                return False
    return True

def bfs(initial_state, target_words):
    queue = deque([(initial_state, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if is_target_state(state, target_words):
            return path
        for next_state in generate_next_states(state):
            if tuple(next_state['board']) not in visited:
                visited.add(tuple(next_state['board']))
                queue.append((next_state, path + [next_state['blank']]))
    return None

initial_board = [['r', 'u', 'p', 'f', 'y', 'w'], ['b', 'l', 'o', 'e', 'l', 'o'], ['n', 'r', '_', 'g', 'h', 't'], ['u', 'b', 'r', 'i', 'o', 't']]
target_words = ['unfew', 'brolly', 'bright', 'uproot']

initial_state = {'board': initial_board, 'blank': (2, 2)}
path = bfs(initial_state, target_words)

print(path)
