
def sort_it(tubes):
    moves = []
    colors = set()
    
    for tube in tubes:
        colors.update(set(tube))
    
    sorted_tubes = [sorted(tube, key=lambda x: list(colors).index(x)) for tube in tubes]
    
    for color in colors:
        for i in range(3):
            if sorted_tubes[i][0] == color:
                for j in range(3):
                    if i != j and len(tubes[j]) < 9 and (not tubes[j] or tubes[j][0] == color):
                        moves.append((i, j))
                        tubes[j].insert(0, tubes[i].pop(0))
                        break
    
    return moves

tubes = [['Red', 'Green', 'Blue', 'Blue', 'Green', 'Blue'], 
         ['Red', 'Green', 'Green', 'Blue', 'Green', 'Blue'], 
         ['Red', 'Red', 'Blue', 'Red', 'Green', 'Red']]

print(sort_it(tubes))
