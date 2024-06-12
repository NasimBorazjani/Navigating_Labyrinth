import copy

def is_feasible(initial_tubes, tube_capacity, moves, called_from_is_correct = False):
    tubes = copy.deepcopy(initial_tubes)
    num_tubes = len(initial_tubes)
    # Iterate over the moves
    for move in moves:   
        move = tuple(int(i) for i in move)
        if len(move) != 2 or not 0 <= move[0] <= num_tubes -1 or not 0 <= move[1] <= num_tubes - 1:
            if called_from_is_correct:
                return False, None
            else:
                return False 
        if not tubes[move[0]]:
            if called_from_is_correct:
                return False, None
            else:
                return False 
        if len(tubes[move[1]]) >= tube_capacity:
            if called_from_is_correct:
                return False, None
            else:
                return False 
        
        ball_to_move = tubes[move[0]].pop(0)
        tubes[move[1]].insert(0, ball_to_move)
    
    if called_from_is_correct:    
        return True, tubes
    else:
        return True
    
def is_correct(initial_tubes, tube_capacity, moves):
    feasible, tubes = is_feasible(initial_tubes, tube_capacity, moves, called_from_is_correct = True)
    if not feasible:
        return False, None
    for tube in tubes:
        if len(set(tube)) != 1:
            return False, None
    return True, len(moves)
    

"""initial_tubes = [['Green', 'Red', 'Green', 'Red'], ['Blue', 'Blue', 'Red', 'Green'], ['Red', 'Blue', 'Green', 'Blue']]
moves =[(0, 1), (0, 2), (0, 1), (2, 0), (2, 0), (1, 0), (1, 0), (2, 1), (2, 0), (1, 2), (1, 2), (1, 2), (1, 2), (0, 1), (0, 1), (0, 1), (2, 0)]#[(0, 1), (0, 1), (0, 2), (1, 0), (1, 0),(1, 0), (1, 0), (1, 2), (0, 1), (0, 1), (2, 0), (2, 0), (1, 0), (2, 1), (2, 1), (0, 2), (0, 2) ]
print(is_correct(initial_tubes, 6, moves))"""
