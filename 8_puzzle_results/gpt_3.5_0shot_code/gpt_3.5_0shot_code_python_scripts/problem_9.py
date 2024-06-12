
import heapq

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def possible_moves(state):
    moves = []
    empty_pos = None
    for i in range(3):
        for j in range(3):
            if state[i][j] == '_':
                empty_pos = (i, j)
    
    if empty_pos[0] > 0:
        moves.append((empty_pos, (empty_pos[0]-1, empty_pos[1])))
    if empty_pos[0] < 2:
        moves.append((empty_pos, (empty_pos[0]+1, empty_pos[1])))
    if empty_pos[1] > 0:
        moves.append((empty_pos, (empty_pos[0], empty_pos[1]-1)))
    if empty_pos[1] < 2:
        moves.append((empty_pos, (empty_pos[0], empty_pos[1]+1)))
    
    return moves

def make_move(state, move):
    new_state = [row.copy() for row in state]
    new_state[move[0][0]][move[0][1]], new_state[move[1][0]][move[1][1]] = new_state[move[1][0]][move[1][1]], new_state[move[0][0]][move[0][1]]
    return new_state

def a_star_search(initial_state):
    goal_state = [[68, 43, 30], [31, 23, 19], [12, 6, '_']]
    frontier = [(0, initial_state, [])]
    heapq.heapify(frontier)
    explored = set()
    
    while frontier:
        _, state, path = heapq.heappop(frontier)
        
        if state == goal_state:
            return path
        
        explored.add(str(state))
        
        for move in possible_moves(state):
            new_state = make_move(state, move)
            if str(new_state) not in explored:
                new_path = path.copy()
                new_path.append(new_state[move[0][0]][move[0][1]])
                new_cost = len(new_path) + manhattan_distance(move[1], (2, 2))
                heapq.heappush(frontier, (new_cost, new_state, new_path))

initial_state = [[23, 30, 43], [12, 31, 19], [6, 68, '_']]
solution = a_star_search(initial_state)
print(solution)
