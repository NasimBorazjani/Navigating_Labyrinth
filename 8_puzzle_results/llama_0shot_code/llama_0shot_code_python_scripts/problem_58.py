
def get_next_states(state):
    empty_row, empty_col = None, None
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == '_':
                empty_row, empty_col = i, j
                break
        else:
            continue
        break

    next_states = []
    for i, j in [(empty_row - 1, empty_col), (empty_row + 1, empty_col), (empty_row, empty_col - 1), (empty_row, empty_col + 1)]:
        if 0 <= i < len(state) and 0 <= j < len(state[i]):
            new_state = [row.copy() for row in state]
            new_state[i][j], new_state[empty_row][empty_col] = new_state[empty_row][empty_col], new_state[i][j]
            next_states.append(new_state)

    return next_states
