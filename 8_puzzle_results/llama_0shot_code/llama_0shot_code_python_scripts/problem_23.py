
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
    heap = [(manhattan_distance(start), start)]
    visited = set()

    while heap:
        _, state = heapq.heappop(heap)
        if state not in visited:
            visited.add(tuple(map(tuple, state)))

            if state == goal_state:
                return []

            for next_state in generate_next_states(state):
                empty_x, empty_y = 0, 0
                for i in range(3):
                    for j in range(3):
                        if next_state[i][j] == '_':
                            empty_x, empty_y = i, j
                            break
                        elif next_state[i][j] == state[empty_x][empty_y]:
                            next_state[i][j] = '_'
                            next_state[empty_x][empty_y] = state[i][j]
                            break
                    else:
                        continue
                    break

                heapq.heappush(heap, (manhattan_distance(next_state) + len(next_state[empty_x]) + len(next_state[empty_y]), next_state))

    return None

start = [[62, 43, 28], [59, 34, 53], [29, 76, '_']]
goal_state = [[8, 7, 6], [5, 4, 3], [2, 1, '_']]

print(a_star(start))
