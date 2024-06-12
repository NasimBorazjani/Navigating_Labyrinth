
def sort_it(tubes):
    def is_sorted(tubes):
        return all(all(ball == tubes[0][0] for ball in tube) for tube in tubes)

    def move_ball(tubes, from_tube, to_tube):
        ball = tubes[from_tube].pop(0)
        tubes[to_tube].insert(0, ball)

    def solve(tubes, moves):
        if is_sorted(tubes):
            return moves
        shortest_moves = None
        for i in range(3):
            for j in range(3):
                if i != j and tubes[i] and (not tubes[j] or tubes[i][0] == tubes[j][0]):
                    new_tubes = [tube.copy() for tube in tubes]
                    new_moves = moves.copy()
                    move_ball(new_tubes, i, j)
                    new_moves.append((i, j))
                    result = solve(new_tubes, new_moves)
                    if result is not None and (shortest_moves is None or len(result) < len(shortest_moves)):
                        shortest_moves = result
        return shortest_moves

    return solve(tubes, [])

# Initial state of the tubes
tubes = [['Blue', 'Green', 'Green', 'Red'], ['Red', 'Blue', 'Green', 'Red'], ['Blue', 'Red', 'Green', 'Blue']]

# Solve the problem
solution = sort_it(tubes)
print(solution)
