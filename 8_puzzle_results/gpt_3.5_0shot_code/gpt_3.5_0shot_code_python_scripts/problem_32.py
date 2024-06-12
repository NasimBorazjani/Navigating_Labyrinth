
from queue import PriorityQueue

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def possible_moves(state):
    moves = []
    empty_pos = None
    for i in range(3):
        for j in range(4):
            if state[i][j] == '_':
                empty_pos = (i, j)
                break
    if empty_pos[0] > 0:
        moves.append((empty_pos, (empty_pos[0]-1, empty_pos[1])))
    if empty_pos[0] < 2:
        moves.append((empty_pos, (empty_pos[0]+1, empty_pos[1])))
    if empty_pos[1] > 0:
        moves.append((empty_pos, (empty_pos[0], empty_pos[1]-1)))
    if empty_pos[1] < 3:
        moves.append((empty_pos, (empty_pos[0], empty_pos[1]+1)))
    return moves

def apply_move(state, move):
    new_state = [row.copy() for row in state]
    new_state[move[0][0]][move[0][1]], new_state[move[1][0]][move[1][1]] = new_state[move[1][0]][move[1][1]], new_state[move[0][0]][move[0][1]]
    return new_state

def a_star_search(initial_state):
    goal_state = [[69, 56, 47, 44], [30, 24, 15, 8], [67, 63, '_', 73]]
    frontier = PriorityQueue()
    frontier.put((0, initial_state, []))
    explored = set()
    
    while not frontier.empty():
        _, current_state, path = frontier.get()
        
        if current_state == goal_state:
            return path
        
        explored.add(str(current_state))
        
        for move in possible_moves(current_state):
            new_state = apply_move(current_state, move)
            if str(new_state) not in explored:
                new_path = path + [new_state[move[0][0]][move[0][1]]]
                priority = len(new_path) + sum(manhattan_distance((i, j), (goal_state[i][j]//4, goal_state[i][j]%4)) for i in range(3) for j in range(4))
                frontier.put((priority, new_state, new_path))

initial_state = [[69, 56, 8, 67], [15, 47, 44, 30], [73, '_', 24, 63]]
solution = a_star_search(initial_state)
print(solution)
