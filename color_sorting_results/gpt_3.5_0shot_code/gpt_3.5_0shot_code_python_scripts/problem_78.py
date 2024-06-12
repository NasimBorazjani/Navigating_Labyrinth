
def sort_it(tubes):
    def is_sorted(tubes):
        return all(all(ball == tubes[0][0] for ball in tube) for tube in tubes)

    def move_ball(tubes, moves, from_tube, to_tube):
        new_tubes = [tube.copy() for tube in tubes]
        new_tubes[to_tube].insert(0, new_tubes[from_tube].pop(0))
        return new_tubes, moves + [(from_tube, to_tube)]

    def backtrack(tubes, moves):
        if is_sorted(tubes):
            return moves
        shortest_moves = []
        for from_tube in range(3):
            for to_tube in range(3):
                if from_tube != to_tube and len(tubes[to_tube]) < 9 and (not tubes[from_tube] or tubes[from_tube][0] == tubes[to_tube][0]):
                    new_tubes, new_moves = move_ball(tubes, moves, from_tube, to_tube)
                    result = backtrack(new_tubes, new_moves)
                    if result and (not shortest_moves or len(result) < len(shortest_moves)):
                        shortest_moves = result
        return shortest_moves

    return backtrack(tubes, [])

# Initial state of the tubes
tubes = [['Red', 'Green', 'Blue', 'Red', 'Green', 'Blue'], ['Blue', 'Blue', 'Red', 'Blue', 'Green', 'Red'], ['Green', 'Red', 'Green', 'Blue', 'Green', 'Red']]

# Find the shortest list of move tuples to sort the balls
result = sort_it(tubes)
print(result)
