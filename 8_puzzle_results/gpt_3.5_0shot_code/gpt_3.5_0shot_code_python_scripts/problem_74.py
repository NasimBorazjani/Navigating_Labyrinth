
import heapq

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def possible_moves(state):
    moves = []
    empty_pos = None
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == '_':
                empty_pos = (i, j)
                break
    if empty_pos[0] > 0:
        moves.append((empty_pos, (empty_pos[0]-1, empty_pos[1])))
    if empty_pos[0] < len(state)-1:
        moves.append((empty_pos, (empty_pos[0]+1, empty_pos[1])))
    if empty_pos[1] > 0:
        moves.append((empty_pos, (empty_pos[0], empty_pos[1]-1)))
    if empty_pos[1] < len(state[0])-1:
        moves.append((empty_pos, (empty_pos[0], empty_pos[1]+1)))
    return moves

def apply_move(state, move):
    new_state = [row.copy() for row in state]
    new_state[move[0][0]][move[0][1]], new_state[move[1][0]][move[1][1]] = new_state[move[1][0]][move[1][1]], new_state[move[0][0]][move[0][1]]
    return new_state

def a_star_search(initial_state):
    goal_state = [[49, 44, 72, 78, 81], [57, 52, 46, 77, 20], [41, 27, 16, 45, '_']]
    frontier = [(0, initial_state)]
    heapq.heapify(frontier)
    visited = set()
    while frontier:
        cost, state = heapq.heappop(frontier)
        if state == goal_state:
            return cost
        visited.add(tuple(map(tuple, state)))
        for move in possible_moves(state):
            new_state = apply_move(state, move)
            if tuple(map(tuple, new_state)) not in visited:
                new_cost = cost + 1
                heapq.heappush(frontier, (new_cost + manhattan_distance(move[1], (len(state)-1, len(state[0])-1)), new_state))

initial_state = [[49, 20, 77, 78, 57], [41, '_', 52, 44, 72], [27, 81, 45, 16, 46]]
shortest_path_cost = a_star_search(initial_state)
print(shortest_path_cost)
