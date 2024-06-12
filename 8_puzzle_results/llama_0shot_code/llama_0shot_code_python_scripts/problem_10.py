
import heapq

def generate_next_states(state):
    empty_x, empty_y = 0, 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == '_':
                empty_x, empty_y = i, j
                break
        else:
            continue
        break

    next_states = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = empty_x + dx, empty_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row.copy() for row in state]
            new_state[empty_x][empty_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_x][empty_y]
            next_states.append(new_state)

    return next_states

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != '_':
                goal_i, goal_j = divmod(state[i][j] - 1, 3)
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

def a_star(start):
    queue = [(manhattan_distance(start), start, [])]
    visited = {tuple(row) for row in start}
    while queue:
        _, state, swaps = heapq.heappop(queue)
        if state == [[1, 2, 3], [4, 5, 6], [7, 8, '_']]:
            return swaps

        for next_state in generate_next_states(state):
            if tuple(next_state[i]) not in visited:
                visited.add(tuple(next_state[i]))
                heapq.heappush(queue, (manhattan_distance(next_state) + len(swaps), next_state, swaps + [next_state[1][2]]))

initial_state = [[93, 88, 60], [28, 18, 24], ['_', 47, 53]]
print(a_star(initial_state))
