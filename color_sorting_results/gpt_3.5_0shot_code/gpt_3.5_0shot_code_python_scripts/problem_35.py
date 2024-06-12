
def sort_it(tubes):
    moves = []
    colors = ['Red', 'Blue', 'Green']
    
    def move_ball(from_tube, to_tube):
        moves.append((from_tube, to_tube))
        tubes[to_tube].append(tubes[from_tube].pop())
    
    def find_color_index(color):
        for i, tube in enumerate(tubes):
            if tube and tube[-1] == color:
                return i
        return -1
    
    for color in colors:
        while True:
            color_index = find_color_index(color)
            if color_index == -1:
                break
            if len(tubes[color_index]) == 7:
                empty_tube_index = (color_index + 1) % 3
                if len(tubes[empty_tube_index]) == 7:
                    empty_tube_index = (empty_tube_index + 1) % 3
                move_ball(color_index, empty_tube_index)
            else:
                move_ball(color_index, color_index)
    
    return moves

initial_state = [['Red', 'Blue', 'Blue', 'Red'], ['Blue', 'Green', 'Blue', 'Green'], ['Green', 'Red', 'Green', 'Red']]
result = sort_it(initial_state)
print(result)
