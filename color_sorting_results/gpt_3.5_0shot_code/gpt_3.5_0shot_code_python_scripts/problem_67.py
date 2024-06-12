
def sort_it(tubes):
    moves = []
    colors = ['Blue', 'Green', 'Red']
    
    # Helper function to check if tubes are sorted
    def is_sorted(tubes):
        for tube in tubes:
            if len(set(tube)) != 1:
                return False
        return True
    
    # Helper function to find index of color in tubes
    def find_color_index(tubes, color):
        for i, tube in enumerate(tubes):
            if tube and tube[0] == color:
                return i
        return -1
    
    while not is_sorted(tubes):
        for color in colors:
            index = find_color_index(tubes, color)
            if index != -1:
                for i in range(3):
                    if i != index and len(tubes[i]) < 8:
                        moves.append((index, i))
                        tubes[i].insert(0, tubes[index].pop(0))
                        break
    
    return moves

# Initial state of the tubes
tubes = [['Blue', 'Blue', 'Green', 'Red', 'Red'], ['Green', 'Blue', 'Green', 'Blue', 'Blue'], ['Red', 'Green', 'Red', 'Red', 'Green']]

# Solve the 'Sort It' game
solution = sort_it(tubes)
print(solution)
