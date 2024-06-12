
import heapq

def generate_next_states(state):
    empty_x, empty_y = 0, 0
    for i in range(3):
        for j in range(4):
            if state[i][j] == '_':
                empty_x, empty_y = i, j
                break
        else:
            continue
        break

    next_states = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = empty_x + dx, empty_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 4:
            new_state = [row.copy() for row in state]
            new_state[empty_x][empty_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_x][empty_y]
            next_states.append((new_state, (abs(new_x - empty_x), abs(new_y - empty_y))))
    return next_states

def manhattan_distance(state):
    return sum(abs(row - col) for row, line in enumerate(state) for col, num in enumerate(line) if num != '_' and (row, col) != (2, 3))

def a_star(start):
    queue = [(0, 0, start)]
    visited = {tuple(row) for row in start}
    while queue:
        _, cost, state = heapq.heappop(queue)
        if state == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, '_']]:
            return cost, state

        for new_state, (dx, dy) in generate_next_states(state):
            if tuple(new_state) not in visited:
                visited.add(tuple(new_state))
                heapq.heappush(queue, (cost + 1 + dx + dy, cost + 1 + manhattan_distance(new_state), new_state))

def solve_8_puzzle(start):
    _, final_states = a_star(start)
    return [final_states[i][j] for i in range(3) for j in range(4) if final_states[i][j] != '_']

start = [[8, 2, 39, 54], [55, 62, 53, 35], [69, 16, 11, 71]]
print(solve_8_puzzle(start))
