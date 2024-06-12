
import heapq

def generate_next_states(state):
    empty_x, empty_y = 0, 0
    for i in range(3):
        for j in range(6):
            if state[i][j] == '_':
                empty_x, empty_y = i, j
    next_states = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = empty_x + dx, empty_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 6:
            new_state = [row.copy() for row in state]
            new_state[empty_x][empty_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_x][empty_y]
            next_states.append((new_state, (abs(new_x - 1), abs(new_y - 5))))
    return next_states

def a_star(start):
    heap = [(0, start, [])]
    visited = set()
    while heap:
        _, state, path = heapq.heappop(heap)
        if state not in visited:
            visited.add(state)
            if state == goal_state:
                return path
            for next_state, cost in generate_next_states(state):
                heapq.heappush(heap, (len(path) + cost + sum(abs(i-j) for i, j in zip(next_state[1], goal_state[1])), next_state, path + [next_state[1][5]]))

initial_state = [[92, 72, 91, 79, 62, 24], [93, 67, 65, 63, 83, 74], [41, 34, 29, 27, 58, '_']]
goal_state = [[93, 83, 74, 72, 65, 63], [91, 67, 58, 51, 41, 34], [29, 27, 24, 15, 92, '_']]

print(a_star(initial_state))
