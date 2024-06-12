
from collections import deque

def bfs(board, words):
    start = "".join(["".join(row) for row in board])
    queue = deque([(start, "")])
    visited = set([start])
    while queue:
        current, swaps = queue.popleft()
        if current == "".join(words):
            return swaps
        for i in range(len(current)):
            if current[i] == "_":
                for j in ["u", "d", "l", "r"]:
                    new_current = current[:i] + current[i+1:i+2] + "_" + current[i+2:]
                    new_swaps = swaps + j
                    if new_current not in visited:
                        visited.add(new_current)
                        queue.append((new_current, new_swaps))

board = [['e', 'h', 'r', 'y'], ['w', 'f', 'r', 'r'], ['_', 'u', 'd', 'd'], ['f', 'a', 'i', 'b']]
words = ["hay", "werf", "rudd", "frib"]
print(bfs(board, words))
