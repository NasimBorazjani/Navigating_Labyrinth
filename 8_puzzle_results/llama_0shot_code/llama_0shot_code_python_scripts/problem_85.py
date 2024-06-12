
import heapq

def generate_next_states(state):
    empty_x, empty_y = 0, 0
    for i in range(3):
        for j in range(5):
            if state[i][j] == '_':
                empty_x, empty_y = i, j
                break
        else:
            continue
        break

    next_states = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = empty_x + dx, empty_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 5:
            new_state = [row.copy() for row in state]
            new_state[empty_x][empty_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_x][empty_y]
            next_states.append((new_state, (abs(new_x - empty_x), abs(new_y - empty_y))))
    return next_states

def manhattan_distance(state):
    return sum(abs(state[i][j] - str(i * 3 + j + 1)) for i in range(3) for j in range(5) if state[i][j] != '_')

def a_star(start):
    queue = [(0, 0, start)]
    visited = {tuple(row) for row in start}
    while queue:
        _, cost, state = heapq.heappop(queue)
        if state == [['8', '7', '6', '5', '4'], ['3', '_', '2', '1', '16'], ['15', '14', '13', '12', '11']]:
            return cost, state

        for new_state, (dx, dy) in generate_next_states(state):
            if tuple(new_state) not in visited:
                visited.add(tuple(new_state))
                heapq.heappush(queue, (cost + 1 + dx + dy, cost + 1 + manhattan_distance(new_state), new_state))

initial_state = [['93', '26', '39', '51', '69'], ['27', '_', '43', '7', '89'], ['63', '91', '23', '68', '17']]
_, final_state = a_star(initial_state)

print([final_state[i][j] for i in range(3) for j in range(5) if final_state[i][j] != '_'])
