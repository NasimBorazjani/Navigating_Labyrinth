
def sort_it(tubes):
    def is_sorted(tubes):
        return all(all(ball == tube[0] for ball in tube) for tube in tubes)
    
    def move_ball(tubes, moves):
        if is_sorted(tubes):
            return moves
        
        shortest_moves = None
        for i in range(3):
            for j in range(3):
                if i != j and tubes[i] and (not tubes[j] or tubes[i][-1] == tubes[j][-1]):
                    new_tubes = [tube.copy() for tube in tubes]
                    new_tubes[j].append(new_tubes[i].pop())
                    new_moves = moves + [(i, j)]
                    result = move_ball(new_tubes, new_moves)
                    if result and (not shortest_moves or len(result) < len(shortest_moves)):
                        shortest_moves = result
        
        return shortest_moves
    
    return move_ball(tubes, [])

# Initial state of the tubes
tubes = [['Red', 'Blue', 'Blue', 'Red'], ['Blue', 'Green', 'Blue', 'Green'], ['Green', 'Red', 'Green', 'Red']]

# Solve the problem
solution = sort_it(tubes)

# Print the shortest list of move tuples
print(solution)
