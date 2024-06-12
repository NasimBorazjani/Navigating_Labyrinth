
import heapq

def generate_next_states(state):
    empty_x, empty_y = 0, 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == '_':
                empty_x, empty_y = i, j
                break
        else:
            continue
        break

    next_states = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = empty_x + dx, empty_y + dy
        if 0 <= new_x < len(state) and 0 <= new_y < len(state[0]):
            new_state = [row.copy() for row in state]
            new_state[empty_x][empty_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_x][empty_y]
            next_states.append((new_state, new_state[new_x][new_y]))
    return next_states

def manhattan_distance(state):
    return sum(abs(row - (i+1)) + abs(col - (j+1)) 
               for i, row in enumerate(state) 
               for j, col in enumerate(row) 
               if col != '_' and (row, col) != (i+1, j+1))

def a_star(start):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        _, state, swaps = heapq.heappop(queue)
        if state not in visited:
            visited.add(state)
            if state == goal_state:
                return swaps
            for next_state, tile in generate_next_states(state):
                heapq.heappush(queue, (manhattan_distance(next_state) + len(swaps) + 1, next_state, swaps + [tile]))

goal_state = [['_', 10, 9, 8, 7], [6, 5, 4, 3, 2], [1, 12, 11, 13, 14]]
start_state = [[54, 100, 91, 80, 56], [19, '_', 38, 74, 29], [14, 36, 44, 13, 10]]

print(a_star(start_state))
