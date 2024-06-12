import copy

def is_feasible(initial_tubes, tube_capacity, cost_dict, moves, called_from_correct = False):
    tubes = copy.deepcopy(initial_tubes)
    
    num_tubes = len(initial_tubes)
    cost = 0
    # Iterate over the moves
    for move in moves:   
        move = tuple(int(i) for i in move)
        if len(move) != 2 or not 0 <= move[0] <= num_tubes -1 or not 0 <= move[1] <= num_tubes - 1:
            if called_from_correct:
                return False, None, None
            return False 
        if not tubes[move[0]]:
            if called_from_correct:
                return False, None, None
            return False
        if len(tubes[move[1]]) >= tube_capacity:
            if called_from_correct:
                return False, None, None
            return False      
        
        ball_to_move = tubes[move[0]].pop(0)
        tubes[move[1]].insert(0, ball_to_move)
        if move[1] in cost_dict:
            cost += cost_dict[move[1]]
        else:
            cost += cost_dict[str(move[1])]
        
    if called_from_correct:
        return True, tubes, cost
    return True
    
def is_correct(initial_tubes, tube_capacity, cost_dict, num_blocks_per_tube_final, moves):
    feasible, tubes, cost = is_feasible(initial_tubes, tube_capacity, cost_dict, moves, called_from_correct=True)
    if not feasible:
        return False, None
    for tube in tubes:
        if (len(set(tube)) == 1 and len(tube) == num_blocks_per_tube_final) or len(tube) == 0:
            continue
        else:
            return False, None
    return True, cost
    

"""initial_tubes = [['Green', 'Green', 'Blue', 'Green'],
['Blue', 'Red', 'Green', 'Red'],
['Red', 'Red', 'Blue', 'Blue']]
moves = [(0, 1), (0, 1), (0, 2), (1, 0), (1, 0),(1, 0), (1, 0), (1, 2), (0, 1), (0, 1), (2, 0), (2, 0), (1, 0), (2, 1), (2, 1), (0, 2), (0, 2) ]
print(solution_is_correct(initial_tubes, moves, 6))"""
