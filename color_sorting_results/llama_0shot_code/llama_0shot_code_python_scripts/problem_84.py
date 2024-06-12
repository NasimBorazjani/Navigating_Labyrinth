
def sort_it(tubes):
    moves = []
    while True:
        max_color_tube = max(tubes, key=lambda tube: (len([ball for ball in tube if ball == tube[0]]), -tube.count(tube[0])), default=None)
        if max_color_tube is None:
            break
        max_color = max_color_tube[0]
        receiving_tubes = [tube for tube in tubes if tube != max_color_tube and len(tube) < 9 and tube[0] != max_color]
        if len(receiving_tubes) == 1:
            receiving_tubes[0].append(max_color_tube.pop())
            moves.append((tubes.index(max_color_tube), tubes.index(receiving_tubes[0])))
        else:
            min_other_color_count = min([len([ball for ball in tube if ball != max_color]) for tube in receiving_tubes])
            receiving_tube = next(tube for tube in receiving_tubes if len([ball for ball in tube if ball != max_color]) == min_other_color_count)
            receiving_tube.append(max_color_tube.pop())
            moves.append((tubes.index(max_color_tube), tubes.index(receiving_tube)))
    return moves
