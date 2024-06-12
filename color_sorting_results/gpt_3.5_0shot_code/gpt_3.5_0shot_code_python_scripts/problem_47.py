
def sort_it(tubes, moves=[]):
    if all(len(tube) == 0 for tube in tubes):
        return moves
    
    shortest_moves = None
    
    for i in range(len(tubes)):
        for j in range(len(tubes)):
            if i != j and (not tubes[i] or tubes[j] and tubes[i][-1] == tubes[j][-1]):
                continue
            
            if tubes[i] and (not tubes[j] or tubes[i][-1] < tubes[j][-1]):
                new_tubes = [tube.copy() for tube in tubes]
                new_tubes[j].append(new_tubes[i].pop())
                new_moves = moves + [(i, j)]
                
                result = sort_it(new_tubes, new_moves)
                
                if result and (not shortest_moves or len(result) < len(shortest_moves)):
                    shortest_moves = result
    
    return shortest_moves

initial_state = [['Blue', 'Red', 'Green', 'Green'], ['Green', 'Blue', 'Red', 'Blue'], ['Red', 'Green', 'Blue', 'Red']]
solution = sort_it(initial_state)

print(solution)
