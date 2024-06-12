
from collections import deque

def bfs(board, target):
    start = "".join(["".join(row) for row in board])
    queue = deque([(start, "")])
    visited = set([start])
    while queue:
        state, swaps = queue.popleft()
        if state == target:
            return swaps
        for i in range(len(state)):
            for j in range(len(state)):
                if i > 0 and state[i - 1:i + 1] == '_' + state[i:i + 1]:
                    new_state = state[:i - 1] + state[i:i + 2]
                    new_state = new_state[:j] + '_' + new_state[j + 1:]
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, swaps + "U"))
                if i < len(state) - 1 and state[i:i + 2] == state[i + 1:i + 2] + '_':
                    new_state = state[:i] + '_' + state[i + 1:]
                    new_state = new_state[:j + 1] + state[j:j + 1] + new_state[j + 2:]
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, swaps + "D"))
                if j > 0 and state[j - 1:j + 1] == '_' + state[j:j + 1]:
                    new_state = state[:j - 1] + state[j:j + 2]
                    new_state = new_state[:i] + '_' + new_state[i + 1:]
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, swaps + "L"))
                if j < len(state) - 1 and state[j:j + 2] == state[j + 1:j + 2] + '_':
                    new_state = state[:j] + '_' + state[j + 1:]
                    new_state = new_state[:i] + state[i:i + 1] + new_state[i + 1:]
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, swaps + "R"))

initial_board = [['_', 'p', 'h', 'm', 'p'], ['s', 'a', 'd', 'r', 'e'], ['i', 'u', 'n', 'i', 'r'], ['u', 'a', 'z', 'e', 'n']]
target_words = "pimp sadhe aurir unzen"

print(bfs(initial_board, target_words.replace(" ", "")))
