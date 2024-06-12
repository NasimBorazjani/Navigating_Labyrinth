
import heapq

initial_state = [[80, 62, 76], [47, 67, 82], [24, 73, '_']]
goal_state = [[82, 80, 76], [73, 67, 62], [47, 24, '_']]

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def possible_moves(state):
    moves = []
    empty_pos = None
    for i in range(3):
        for j in range(3):
            if state[i][j] == '_':
                empty_pos = (i, j)
                break
    if empty_pos[0] > 0:
        moves.append((empty_pos, (empty_pos[0]-1, empty_pos[1])))
    if empty_pos[0] < 2:
        moves.append((empty_pos, (empty_pos[0]+1, empty_pos[1])))
    if empty_pos[1] > 0:
        moves.append((empty_pos, (empty_pos[0], empty_pos[1]-1)))
    if empty_pos[1] < 2:
        moves.append((empty_pos, (empty_pos[0], empty_pos[1]+1)))
    return moves

def a_star_search(initial_state, goal_state):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, (0, initial_state, []))
    
    while open_list:
        _, state, path = heapq.heappop(open_list)
        if state == goal_state:
            return path
        if str(state) in closed_list:
            continue
        closed_list.add(str(state))
        
        for move in possible_moves(state):
            new_state = [row.copy() for row in state]
            new_state[move[0][0]][move[0][1]], new_state[move[1][0]][move[1][1]] = new_state[move[1][0]][move[1][1]], new_state[move[0][0]][move[0][1]]
            new_path = path.copy()
            new_path.append(new_state[move[1][0]][move[1][1]])
            heapq.heappush(open_list, (len(new_path) + manhattan_distance(move[1], (2, 2)), new_state, new_path))

solution = a_star_search(initial_state, goal_state)
print(solution)
