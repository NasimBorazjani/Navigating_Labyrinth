
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
    queue = [(0, 0, start, '_')]
    visited = {tuple(row) for row in start}
    while queue:
        _, _, state, swapped = heapq.heappop(queue)
        if swapped == '_':
            return []
        if manhattan_distance(state) == 0:
            return [swapped]

        for new_state, new_swapped in generate_next_states(state):
            if tuple(new_state) not in visited:
                visited.add(tuple(new_state))
                heapq.heappush(queue, (manhattan_distance(new_state) + len(swapped), len(swapped), new_state, new_swapped))

    return []

initial_state = [['_', 94, 43, 58, 77], [96, 100, 75, 84, 52], [50, 29, 60, 27, 74]]
print(a_star(initial_state))
