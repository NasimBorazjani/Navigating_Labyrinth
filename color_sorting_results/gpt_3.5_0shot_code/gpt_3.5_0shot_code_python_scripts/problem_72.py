
def sort_it(tubes):
    def is_sorted(tubes):
        return all(all(ball == tubes[0][0] for ball in tube) for tube in tubes)
    
    def move_ball(tubes, moves, from_tube, to_tube):
        new_tubes = [tube.copy() for tube in tubes]
        new_moves = moves.copy()
        ball = new_tubes[from_tube].pop(0)
        new_tubes[to_tube].insert(0, ball)
        new_moves.append((from_tube, to_tube))
        return new_tubes, new_moves
    
    def backtrack(tubes, moves):
        if is_sorted(tubes):
            return moves
        
        shortest_moves = None
        for i in range(3):
            for j in range(3):
                if i != j and tubes[i] and len(tubes[j]) < 8:
                    new_tubes, new_moves = move_ball(tubes, moves, i, j)
                    result = backtrack(new_tubes, new_moves)
                    if result is not None and (shortest_moves is None or len(result) < len(shortest_moves)):
                        shortest_moves = result
        
        return shortest_moves
    
    initial_moves = []
    result = backtrack(tubes, initial_moves)
    return result

# Initial state of the tubes
tubes = [['Red', 'Red', 'Blue', 'Green', 'Red'], ['Blue', 'Green', 'Green', 'Red', 'Red'], ['Blue', 'Blue', 'Green', 'Green', 'Blue']]
solution = sort_it(tubes)
print(solution)
