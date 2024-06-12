
from collections import deque

def bfs(initial_board, target_words):
    initial_state = "".join(["".join(row) for row in initial_board])
    target_state = "_" + "".join(target_words)
    queue = deque([(initial_state, [])])
    visited = set([initial_state])

    while queue:
        state, actions = queue.popleft()
        if state == target_state:
            return actions
        for i in range(len(state)):
            for j in range(i+1, len(state)):
                if state[i] == '_' and state[j] != '_':
                    new_state = list(state)
                    new_state[i], new_state[j] = new_state[j], new_state[i]
                    new_state = "".join(new_state)
                    if new_state not in visited:
                        visited.add(new_state)
                        new_actions = actions + [f"swap({i}, {j})"]
                        queue.append((new_state, new_actions))

initial_board = [['t', 'w', 'y', 'l', '_'], ['s', 'a', 'u', 'f', 't'], ['o', 'a', 'e', 'm', 'n'], ['f', 'l', 'd', 'm', 'd']]
target_words = ['wolf', 'stunt', 'lammy', 'faded']
print(bfs(initial_board, target_words))
