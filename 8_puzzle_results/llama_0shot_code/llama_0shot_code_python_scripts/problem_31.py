
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
    for i, j in [(empty_x-1, empty_y), (empty_x+1, empty_y), (empty_x, empty_y-1), (empty_x, empty_y+1)]:
        if 0 <= i < 2 and 0 <= j < 4:
            new_state = [row.copy() for row in state]
            new_state[empty_x][empty_y], new_state[i][j] = new_state[i][j], '_'
            next_states.append((new_state, (abs(i - (1 - empty_x)) + abs(j - (3 - empty_y)))))
    return next_states

def a_star(start):
    queue = [(0, 0, start)]
    visited = set()
    while queue:
        _, cost, state = heapq.heappop(queue)
        if state not in visited:
            visited.add(state)
            if state == [['_', 14, 90, 43], [75, 53, 73, 62], [21, 17, 51, 27]]:
                return cost
            for next_state, next_cost in generate_next_states(state):
                heapq.heappush(queue, (cost + next_cost + 1, cost + next_cost, next_state))
    return None

initial_state = [['75', '53', '73', '62'], ['_', '14', '90', '43'], ['21', '17', '51', '27']]
print(a_star(initial_state))
