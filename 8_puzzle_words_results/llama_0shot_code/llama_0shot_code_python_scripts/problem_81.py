
from collections import deque

def bfs(start, target):
    queue = deque([(start, '')])
    visited = set()
    while queue:
        current, swaps = queue.popleft()
        if current not in visited:
            visited.add(current)
            if current == target:
                return swaps
            for direction in ['ur', 'dr', 'ul', 'dl']:
                next_state = swap(current, direction)
                if next_state:
                    queue.append((next_state, swaps + direction + ' '))
    return None

def swap(board, direction):
    rows = board.split(' ')
    blank = rows[0].find('_')
    if direction == 'ur':
        if blank < len(rows[0]) - 1 and blank < len(rows) - 1:
            rows[blank][blank], rows[blank + 1][blank + 1] = rows[blank + 1][blank + 1], rows[blank][blank]
            rows[blank], rows[blank + 1] = rows[blank + 1], rows[blank]
            return ' '.join(rows)
    elif direction == 'dr':
        if blank < len(rows[0]) - 1 and blank > 0:
            rows[blank][blank], rows[blank - 1][blank + 1] = rows[blank - 1][blank + 1], rows[blank][blank]
            rows[blank], rows[blank - 1] = rows[blank - 1], rows[blank]
            return ' '.join(rows)
    elif direction == 'ul':
        if blank > 0 and blank < len(rows) - 1:
            rows[blank][blank], rows[blank + 1][blank - 1] = rows[blank + 1][blank - 1], rows[blank][blank]
            rows[blank], rows[blank + 1] = rows[blank + 1], rows[blank]
            return ' '.join(rows)
    elif direction == 'dl':
        if blank > 0 and blank > 1:
            rows[blank][blank], rows[blank - 1][blank - 1] = rows[blank - 1][blank - 1], rows[blank][blank]
            rows[blank], rows[blank - 1] = rows[blank - 1], rows[blank]
            return ' '.join(rows)
    else:
        return None

start = '_ e c o r e r e u t l r i i c i k n z e l i z h l'
target = 'core reuel rinch kizil iztle'

swaps = bfs(start, target)
print(swaps.strip())
