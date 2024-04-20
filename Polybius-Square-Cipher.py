def generate_polybius_square():
    grid = [['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'K'],
            ['L', 'M', 'N', 'O', 'P'],
            ['Q', 'R', 'S', 'T', 'U'],
            ['V', 'W', 'X', 'Y', 'Z']]
    return grid
def encode_message(message, grid):
    encoded_message = ""
    for char in message:
        if char.upper() == 'J':
            char = 'I'
        for i in range(5):
            for j in range(5):
                if grid[i][j] == char.upper():
                    encoded_message += str(i+1) + str(j+1)
    return encoded_message