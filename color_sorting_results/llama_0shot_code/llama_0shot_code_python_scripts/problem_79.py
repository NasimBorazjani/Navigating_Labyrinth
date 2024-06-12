
def sort_it(tubes):
    moves = []
    while True:
        source = None
        destination = None
        for i in range(len(tubes)):
            if tubes[i]:
                color = tubes[i][-1]
                if tubes[i].count(color) != len(tubes[i]):
                    source = i
                    break
        if source is None:
            return moves
        for i in range(len(tubes)):
            if tubes[i] and tubes[i][-1] == color and len(tubes[i]) < 9:
                destination = i
                break
        if destination is None:
            tubes.append([color])
            destination = len(tubes) - 1
        moves.append((source, destination))
        tubes[source].pop()
        tubes[destination].append(color)

tubes = [['Red', 'Green', 'Red', 'Blue', 'Blue', 'Green'], 
         ['Green', 'Green', 'Red', 'Red', 'Blue', 'Blue'], 
         ['Blue', 'Red', 'Green', 'Blue', 'Green', 'Red']]

print(sort_it(tubes))
