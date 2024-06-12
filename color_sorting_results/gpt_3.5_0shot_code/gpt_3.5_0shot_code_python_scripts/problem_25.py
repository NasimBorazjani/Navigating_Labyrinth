
def sort_it(tubes, moves=[]):
    if all(len(set(tube)) == 1 for tube in tubes):
        return moves
    
    shortest_moves = None
    
    for i in range(3):
        for j in range(3):
            if i != j and tubes[i] and (not tubes[j] or tubes[i][-1] == tubes[j][-1]):
                new_tubes = [tube.copy() for tube in tubes]
                new_tubes[j].append(new_tubes[i].pop())
                new_moves = moves + [(i, j)]
                
                result = sort_it(new_tubes, new_moves)
                
                if result is not None and (shortest_moves is None or len(result) < len(shortest_moves)):
                    shortest_moves = result
    
    return shortest_moves

initial_state = [['Green', 'Green', 'Red', 'Red'], ['Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Red', 'Green', 'Red']]
solution = sort_it(initial_state)

print(solution)
