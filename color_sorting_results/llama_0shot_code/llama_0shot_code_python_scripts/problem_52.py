
def perform_move(tubes, from_tube, to_tube):
    # Remove a ball from the 'from_tube' and add it to the 'to_tube'
    ball = tubes[from_tube].pop()
    tubes[to_tube].append(ball)
    return tubes

def sort_it(initial_tubes):
    tubes = [[balls.pop() for balls in initial_tubes[::-1]]]
    moves = []
    while tubes[-1] != [['Green', 'Green', 'Green', 'Red', 'Red', 'Red', 'Blue', 'Blue']]:
        for i in range(len(tubes[-1])):
            for j in range(len(tubes[-1])):
                if i != j and len(tubes[-1][j]) < 8:
                    tubes.append(perform_move(tubes[-1], i, j))
                    moves.append((i, j))
                    break
            else:
                continue
            break
    return moves

initial_tubes = [['Green', 'Green', 'Blue', 'Red', 'Green'], ['Red', 'Red', 'Blue', 'Red', 'Blue'], ['Green', 'Blue', 'Blue', 'Red', 'Green']]
print(sort_it(initial_tubes))
