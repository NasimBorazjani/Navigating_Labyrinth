
def sort_it(tubes):
    def is_sorted(tubes):
        return all([len(set(tube)) == 1 for tube in tubes])

    def move_ball(tubes, from_tube, to_tube):
        ball = tubes[from_tube].pop(0)
        tubes[to_tube].insert(0, ball)

    moves = []
    while not is_sorted(tubes):
        for i in range(3):
            for j in range(3):
                if i != j and tubes[i] and (not tubes[j] or tubes[i][0] == tubes[j][0]):
                    move_ball(tubes, i, j)
                    moves.append((i, j))
                    break

    return moves

initial_state = [['Green', 'Green', 'Green', 'Red', 'Blue', 'Blue'], ['Blue', 'Red', 'Red', 'Red', 'Green', 'Green'], ['Blue', 'Green', 'Blue', 'Red', 'Red', 'Blue']]
moves = sort_it(initial_state)
print(moves)
