
def sort_it(tubes):
    colors = {'Red': 0, 'Green': 1, 'Blue': 2}
    moves = []
    while True:
        full_tubes = [tube for tube in tubes if len(tube) == 8]
        if not full_tubes:
            break
        for tube in full_tubes:
            ball = tube.pop()
            src = tubes.index(tube)
            dest = next(i for i, t in enumerate(tubes) if i != src and len(t) < 8 and colors[t[-1]] < colors[ball])
            tubes[dest].append(ball)
            moves.append((src, dest))
    return moves

tubes = [['Red', 'Blue', 'Blue', 'Blue', 'Green'], ['Red', 'Green', 'Green', 'Red', 'Green'], ['Red', 'Red', 'Blue', 'Green', 'Blue']]
print(sort_it(tubes))
