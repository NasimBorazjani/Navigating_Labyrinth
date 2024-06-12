
def sort_it(tubes):
    color_to_tube = {'Red': 0, 'Blue': 1, 'Green': 2}
    tubes = [{'colors': list(tube), 'index': 0} for tube in tubes]
    moves = []

    while True:
        moving_tube = None
        for tube in tubes:
            if tube['colors'][tube['index']] != tubes[color_to_tube[tube['colors'][tube['index']]]]['colors'][0]:
                moving_tube = tube
                break

        if moving_tube is None:
            break

        receiving_tube = tubes[color_to_tube[moving_tube['colors'][moving_tube['index']]]]
        if len(receiving_tube['colors']) == 6 or receiving_tube is moving_tube:
            moving_tube['index'] += 1
        else:
            receiving_tube['colors'].append(moving_tube['colors'].pop(moving_tube['index']))
            moves.append((tubes.index(moving_tube), color_to_tube[receiving_tube['colors'][-1]]))

    return moves
