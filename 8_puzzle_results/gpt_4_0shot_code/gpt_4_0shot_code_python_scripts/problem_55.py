
def find_position(matrix, item):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == item:
                return row, col
    return None

def swap(matrix, pos1, pos2):
    matrix[pos1[0]][pos1[1]], matrix[pos2[0]][pos2[1]] = matrix[pos2[0]][pos2[1]], matrix[pos1[0]][pos1[1]]
    return matrix

initial_state = [[34, 68, 46, 20], [12, 18, '_', 5], [53, 7, 65, 47]]
goal_state = [[68, 65, 53, 47], [46, 34, 20, 18], [12, 7, 5, '_']]

moves = []
while initial_state != goal_state:
    empty_pos = find_position(initial_state, '_')
    goal_item = goal_state[empty_pos[0]][empty_pos[1]]
    goal_item_pos = find_position(initial_state, goal_item)
    initial_state = swap(initial_state, empty_pos, goal_item_pos)
    moves.append(goal_item)

print(moves)
