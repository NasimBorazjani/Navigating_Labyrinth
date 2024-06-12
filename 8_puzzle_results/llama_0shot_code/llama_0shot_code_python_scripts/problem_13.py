
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
                number = int(state[i][j])
                goal_i, goal_j = divmod(number - 1, 3)
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

def a_star(start):
    queue = [(manhattan_distance(start), start, [])]
    visited = set()

    while queue:
        _, state, swaps = heapq.heappop(queue)
        if state not in visited:
            visited.add(state)
            if state == goal_state:
                return swaps

            for next_state in generate_next_states(state):
                new_swaps = swaps + [next_state[i][j] for i in range(3) for j in range(3) if next_state[i][j] == '_']
                heapq.heappush(queue, (manhattan_distance(next_state) + len(new_swaps), next_state, new_swaps))

    return None

initial_state = [[41, 36, 82], [29, 97, 43], ['_', 51, 61]]
goal_state = [[82, 61, '_'], [51, 43, 41], [36, 29, 97]]

print(a_star(initial_state))
