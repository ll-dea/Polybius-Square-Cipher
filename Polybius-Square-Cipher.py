def generate_polybius_square(variant):
    if variant == "ADFGVX":
        grid = [['A', 'D', 'F', 'G', 'V', 'X'],
                ['B', 'C', 'E', 'I', 'K', 'L'],
                ['M', 'N', 'O', 'P', 'Q', 'R'],
                ['S', 'T', 'U', 'W', 'Y', 'Z'],
                ['0', '1', '2', '3', '4', '5'],
                ['6', '7', '8', '9', ',', '.']]
    elif variant == "ADFGX":
        grid = [['A', 'D', 'F', 'G', 'X'],
                ['B', 'C', 'E', 'I', 'K'],
                ['L', 'M', 'N', 'O', 'P'],
                ['Q', 'R', 'S', 'T', 'U'],
                ['V', 'W', 'Y', 'Z', '0']]
    elif variant == "ADFGVXZ":
        grid = [['A', 'D', 'F', 'G', 'V', 'X', 'Z'],
                ['B', 'C', 'E', 'I', 'K', 'L', 'M'],
                ['N', 'O', 'P', 'Q', 'R', 'S', 'T'],
                ['U', 'W', 'Y', '0', '1', '2', '3'],
                ['4', '5', '6', '7', '8', '9', ','],
                ['.', ' ', '!', '?', '@', '#', '$'],
                ['%', '&', '*', '(', ')', '-', '/']]
    else:
        raise ValueError("Varianti eshte gabim! Ju lutem zgjedhni nje nga keto opsione: ADFGVX, ADFGX, ADFGVXZ")
    return grid
def encrypt_message(message, grid):
    encrypted_message = ""
    for char in message:
        if char.upper() == 'J':
            char = 'I'
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == char.upper():
                    encrypted_message += str(i) + str(j)
    return encrypted_message

def decrypt_message(encrypted_message, grid):
    decrypted_message = ""
    for i in range(0, len(encrypted_message), 2):
        row = int(encrypted_message[i])
        col = int(encrypted_message[i+1])
        decrypted_message += grid[row][col]
    return decrypted_message
