
from collections import deque

def bfs(board, words):
    visited = set()
    queue = deque([(str(board), '')])
    while queue:
        current, actions = queue.popleft()
        if current == '_'.join(words):
            return actions
        for i in range(len(current)):
            if current[i] == '_':
                for j in range(4):
                    new_current = current[:i] + current[i+1:i+2] + '_' + current[i+2:]
                    new_actions = actions + 'udrl'[j]
                    if new_current not in visited:
                        visited.add(new_current)
                        queue.append((new_current, new_actions))

words = ['man', 'cute', 'dazy', 'down', 'oryx']
board = [['u', 'm', 'a', 'n'], ['c', 'd', 't', 'e'], ['o', 'a', '_', 'y'], ['d', 'n', 'w', 'y'], ['o', 'r', 'z', 'x']]

print(bfs(board, words))
