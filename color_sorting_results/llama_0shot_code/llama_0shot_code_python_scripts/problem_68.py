
def sort_it(tubes):
    color_to_tube = {}
    moves = []

    for tube_index, tube in enumerate(tubes):
        for ball_color in tube:
            if ball_color not in color_to_tube:
                color_to_tube[ball_color] = tube_index

    while True:
        new_moves = []

        for tube_index, tube in enumerate(tubes):
            for ball_color in tube:
                target_tube = color_to_tube[ball_color]

                if tube_index != target_tube and len(tubes[target_tube]) < 8:
                    new_moves.append((tube_index, target_tube))
                    tubes[target_tube].append(ball_color)
                    tubes[tube_index].remove(ball_color)

                    if len(tubes[tube_index]) == 0:
                        del tubes[tube_index]
                        break

        if not new_moves:
            break

        moves.extend(new_moves)

    return moves


tubes = [['Blue', 'Green', 'Blue', 'Blue', 'Blue'],
         ['Blue', 'Green', 'Red', 'Red', 'Green'],
         ['Green', 'Red', 'Red', 'Green', 'Red']]

print(sort_it(tubes))
