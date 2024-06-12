
def sort_it(tubes):
    def find_next_ball():
        for i, tube in enumerate(tubes):
            for j in range(len(tube)-1, -1, -1):
                if tube[j] != tubes[i][-1]:
                    return i, j
        return None

    def find_move_to():
        for i, tube in enumerate(tubes):
            if len(tube) < 9 and tube[-1] == tubes[i][-1]:
                return i
        return None

    moves = []
    while True:
        ball = find_next_ball()
        if ball is None:
            break
        tube_to = find_move_to()
        if tube_to is None:
            break
        moves.append((ball[0], tube_to))
        tubes[ball[0]].pop(ball[1])
    return moves

tubes = [['Red', 'Green', 'Blue', 'Blue', 'Blue', 'Red'], 
         ['Red', 'Red', 'Green', 'Blue', 'Green', 'Blue'], 
         ['Red', 'Red', 'Green', 'Green', 'Blue', 'Green']]

print(sort_it(tubes))
