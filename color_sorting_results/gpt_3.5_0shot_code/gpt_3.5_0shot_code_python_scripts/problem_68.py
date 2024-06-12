
def sort_it(tubes):
    target_tubes = [[color]*8 for color in set(sum(tubes, []))]
    moves = []
    
    for target_tube in target_tubes:
        for color in target_tube:
            for i, tube in enumerate(tubes):
                if color in tube:
                    while tube[-1] != color:
                        j = next(j for j, ball in enumerate(tube) if ball == color)
                        moves.append((i, tubes.index([ball for ball in tubes if color not in ball])))
                        tubes[tubes.index([ball for ball in tubes if color not in ball])].append(tube.pop(j))
    
    return moves

initial_state = [['Blue', 'Green', 'Blue', 'Blue', 'Blue'], ['Blue', 'Green', 'Red', 'Red', 'Green'], ['Green', 'Red', 'Red', 'Green', 'Red']]
result = sort_it(initial_state)
print(result)
