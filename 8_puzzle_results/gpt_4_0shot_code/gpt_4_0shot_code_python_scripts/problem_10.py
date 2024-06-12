
def find_position(state, value):
    for i in range(3):
        for j in range(3):
            if state[i][j] == value:
                return i, j

def swap(state, pos1, pos2):
    state[pos1[0]][pos1[1]], state[pos2[0]][pos2[1]] = state[pos2[0]][pos2[1]], state[pos1[0]][pos1[1]]
    return state

initial_state = [[93, 88, 60], [28, 18, 24], ['_', 47, 53]]
goal_state = [[93, 88, 60], [53, 47, 28], [24, 18, '_']]
moves = []

while initial_state != goal_state:
    empty_pos = find_position(initial_state, '_')
    goal_value = goal_state[empty_pos[0]][empty_pos[1]]
    goal_value_pos = find_position(initial_state, goal_value)
    initial_state = swap(initial_state, empty_pos, goal_value_pos)
    moves.append(goal_value)

print(moves)
