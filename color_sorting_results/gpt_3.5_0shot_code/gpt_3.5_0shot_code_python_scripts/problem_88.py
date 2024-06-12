
def sort_balls(tubes, moves=[]):
    if all(len(tube) == 0 for tube in tubes):
        return moves
    
    shortest_moves = None
    
    for i in range(len(tubes)):
        for j in range(len(tubes)):
            if i != j and len(tubes[i]) > 0 and len(tubes[j]) < 9:
                new_tubes = [tube.copy() for tube in tubes]
                ball = new_tubes[i].pop(0)
                new_tubes[j].insert(0, ball)
                new_moves = moves + [(i, j)]
                
                result = sort_balls(new_tubes, new_moves)
                
                if result is not None and (shortest_moves is None or len(result) < len(shortest_moves)):
                    shortest_moves = result
    
    return shortest_moves

initial_state = [['Blue', 'Green', 'Red', 'Green', 'Green', 'Red'], ['Green', 'Blue', 'Red', 'Blue', 'Blue', 'Red'], ['Red', 'Green', 'Blue', 'Blue', 'Green', 'Red']]
solution = sort_balls(initial_state)

print(solution)
