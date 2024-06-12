
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
        new_empty_x, new_empty_y = empty_x + dx, empty_y + dy
        if 0 <= new_empty_x < len(state) and 0 <= new_empty_y < len(state[0]):
            new_state = [row.copy() for row in state]
            new_state[empty_x][empty_y], new_state[new_empty_x][new_empty_y] = new_state[new_empty_x][new_empty_y], new_state[empty_x][empty_y]
            next_states.append((new_state, (abs(new_empty_x - dx) + abs(new_empty_y - dy))))
    return next_states

def a_star(start):
    heap = [(0, start, [])]
    visited = set()
    while heap:
        _, state, path = heapq.heappop(heap)
        if state not in visited:
            visited.add(state)
            if state == goal:
                return path
            for next_state, cost in generate_next_states(state):
                heapq.heappush(heap, (len(path) + cost, next_state, path + [next_state[1][1][1]]))
    return None

initial_state = [[86, 100, 92, 37, 95], [88, '_', 97, 10, 67], [32, 82, 19, 53, 4]]
goal = [[100, 95, 92, 86, 97], [88, '_', 67, 10, 53], [32, 82, 19, 4, 37]]

print(a_star(initial_state))
