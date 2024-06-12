
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
            for j in range(i + 1, len(state)):
                if state[i] == state[j] and state[i] != '_':
                    new_state = list(state)
                    new_state[i], new_state[j] = new_state[j], new_state[i]
                    new_state = "".join(new_state)
                    if new_state not in visited:
                        queue.append((new_state, actions + [new_state[i:i+2]]))
                        visited.add(new_state)

initial_board = [['u', 't', '_', 'e'], ['j', 'd', 'd', 'u'], ['o', 'e', 'z', 'n'], ['b', 'i', 'r', 'y'], ['w', 'i', 'r', 'y']]
target_words = ['tue', 'judy', 'zein', 'bord', 'wiry']
print(bfs(initial_board, target_words))
