
def sort_it(tubes):
    moves = []
    while True:
        to_move = None
        for i, tube in enumerate(tubes):
            if len(tube) > 0 and (to_move is None or tube[0] == tubes[to_move][0]):
                to_move = i
        if to_move is None:
            break
        to_tube = None
        for i, tube in enumerate(tubes):
            if len(tube) > 0 and tube[0] == tubes[to_move][0] and len(tube) < 9:
                to_tube = i
                break
        if to_tube is None:
            min_balls = float('inf')
            for i, tube in enumerate(tubes):
                if len(tube) < min_balls and len(tube) < 9:
                    min_balls = len(tube)
                    to_tube = i
        moves.append((to_move, to_tube))
        tubes[to_tube].append(tubes[to_move].pop(0))
    return moves
