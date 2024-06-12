
import heapq

def generate_next_states(state):
    empty_row, empty_col = find_empty(state)
    next_states = []
    for row, col in [(empty_row-1, empty_col), (empty_row+1, empty_col), (empty_row, empty_col-1), (empty_row, empty_col+1)]:
        if 0 <= row < len(state) and 0 <= col < len(state[0]):
            new_state = swap(state, empty_row, empty_col, row, col)
            next_states.append((new_state, (row, col)))
    return next_states

def find_empty(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == '_':
                return i, j

def swap(state, row1, col1, row2, col2):
    new_state = [list(row) for row in state]
    new_state[row1][col1], new_state[row2][col2] = new_state[row2][col2], new_state[row1][col1]
    return new_state

def manhattan_distance(state):
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] != '_':
                num, goal_row, goal_col = state[i][j], i, j
                distance += abs(num // 10 - goal_row) + abs(num % 10 - goal_col)
    return distance

def a_star(start):
    queue = [(manhattan_distance(start), 0, start)]
    while queue:
        _, cost, state = heapq.heappop(queue)
        if is_goal(state):
            return get_sequence(cost)
        for new_state, (row, col) in generate_next_states(state):
            heapq.heappush(queue, (manhattan_distance(new_state) + cost + 1, cost + 1, new_state))

def is_goal(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] != '_' and state[i][j] != str(i*10 + j + 1):
                return False
    return True

def get_sequence(cost):
    sequence = []
    while cost > 0:
        sequence.append(swaps[cost])
        cost -= 1
    return sequence[::-1]

swaps = {}

def main():
    start = [[61, '_', 99, 70], [42, 81, 90, 16], [41, 54, 28, 45]]
    print(a_star(start))

main()
