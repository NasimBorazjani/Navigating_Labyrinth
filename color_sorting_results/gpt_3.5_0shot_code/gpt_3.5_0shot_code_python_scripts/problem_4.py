
def is_sorted(tubes):
    for tube in tubes:
        if len(set(tube)) != 1:
            return False
    return True

def sort_it(tubes, moves=[]):
    if is_sorted(tubes):
        return moves
    
    shortest_moves = None
    for i in range(3):
        for j in range(3):
            if i != j and tubes[i] and (not tubes[j] or tubes[i][-1] == tubes[j][-1]):
                new_tubes = [tube.copy() for tube in tubes]
                new_tubes[j].append(new_tubes[i].pop())
                new_moves = moves + [(i, j)]
                result = sort_it(new_tubes, new_moves)
                
                if result and (not shortest_moves or len(result) < len(shortest_moves)):
                    shortest_moves = result
    
    return shortest_moves

initial_state = [['Red', 'Red', 'Blue', 'Blue'], ['Red', 'Blue', 'Red', 'Green'], ['Green', 'Blue', 'Green', 'Green']]
solution = sort_it(initial_state)

print(solution)
