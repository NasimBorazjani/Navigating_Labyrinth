
def sort_it(tubes, moves=[]):
    if all(len(tube) == 0 for tube in tubes):
        return moves
    
    shortest_moves = None
    
    for i in range(len(tubes)):
        for j in range(len(tubes)):
            if i != j and (not tubes[j] or tubes[i][-1] == tubes[j][-1]):
                new_tubes = [tube.copy() for tube in tubes]
                new_moves = moves.copy()
                
                if new_tubes[i]:
                    ball = new_tubes[i].pop()
                    new_tubes[j].append(ball)
                    new_moves.append((i, j))
                    
                    result = sort_it(new_tubes, new_moves)
                    
                    if result is not None and (shortest_moves is None or len(result) < len(shortest_moves)):
                        shortest_moves = result
    
    return shortest_moves

initial_state = [['Green', 'Blue', 'Blue', 'Green', 'Blue'], ['Blue', 'Red', 'Red', 'Blue', 'Red'], ['Red', 'Red', 'Green', 'Green', 'Green']]
result = sort_it(initial_state)

print(result)
