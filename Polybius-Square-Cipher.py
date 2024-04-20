import string

def generate_polybius_table(variant="ADFGX"):
    variant = variant.upper()
    if variant == "ADFGX":
        return [
            ['M', 'P', 'R', 'T', 'X'],
            ['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I/J', 'K'],
            ['L', 'N', 'O', 'Q', 'S'],
            ['U', 'V', 'W', 'Y', 'Z']
        ]
    elif variant == "ADFGVX":
        return [
            ['P', 'H', '0', 'Q', 'G'],
            ['6', '4', 'B', '2', 'E'],
            ['N', '1', '5', 'D', 'F'],
            ['3', '7', '9', 'C', 'I'],
            ['8', 'R', 'L', 'A', 'K'],
            ['M', 'O', 'S', 'T', 'U'],
            ['V', 'W', 'X', 'Y', 'Z']
        ]
    elif variant == "ADFGVXZ":
        return [
            ['P', 'H', '0', 'Q', 'G'],
            ['6', '4', 'B', '2', 'E'],
            ['N', '1', '5', 'D', 'F'],
            ['3', '7', '9', 'C', 'I'],
            ['8', 'R', 'L', 'A', 'K'],
            ['M', 'O', 'S', 'T', 'U'],
            ['V', 'W', 'X', 'Y', 'Z'],
            ['Z', 'Z', 'Z', 'Z', 'Z']
        ]
    else:
        raise ValueError("Ky variant nuk i eshte pjese e Polybius.")

def polybius_encrypt(message, variant="ADFGX"):
    message = message.upper().replace("J", "I")
    table = generate_polybius_table(variant)
    cipher = ""
    for char in message:
        if char in string.ascii_uppercase:
            for i in range(5):
                for j in range(5):
                    if table[i][j] == char:
                        cipher += "ADFGX"[i] + "ADFGX"[j]
        elif char == " ":
            cipher += " "
    return cipher

def polybius_decrypt(cipher, variant="ADFGX"):
    table = generate_polybius_table(variant)
    decrypted = ""
    i = 0
    while i < len(cipher):
        if cipher[i] != ' ':
            row_index = "ADFGX".index(cipher[i])
            col_index = "ADFGX".index(cipher[i + 1])
            decrypted += table[row_index][col_index]
            i += 2
        else:
            decrypted += " "
            i += 1
    return decrypted

if __name__ == "__main__":
    while True:
        print("\nPolybius Square Cipher")
        print("1. Enkripto")
        print("2. Dekripto")
        print("3. Dil")
        choice = input("Shtyp zgjedhjen tende (1/2/3): ")

        if choice == '1':
            # Get user input
            message = input("Shtyp nje mesazh per enkriptim: ")

            print("\nZgjidh nje variant te Polybius:")
            print("1. ADFGX")
            print("2. ADFGVX")
            print("3. ADFGVXZ")
            variant_choice = input("Shtyp zgjedhjen tende (1/2/3): ")

            if variant_choice == '1':
                variant = "ADFGX"
            elif variant_choice == '2':
                variant = "ADFGVX"
            elif variant_choice == '3':
                variant = "ADFGVXZ"
            else:
                print("Zgjedhje e gabuar! Kthehemi te ADFGX.")
                variant = "ADFGX"

            # Encrypting a message
            encrypted_message = polybius_encrypt(message, variant)
            print("\nMesazhi i enkriptuar:", encrypted_message)

        elif choice == '2':
            # Get user input
            message = input("Shtypni nje mesazh per dekriptim: ")

            print("\nZgjidh nje variant te Polybius:")
            print("1. ADFGX")
            print("2. ADFGVX")
            print("3. ADFGVXZ")
            variant_choice = input("Shtyp zgjedhjen tende (1/2/3): ")

            if variant_choice == '1':
                variant = "ADFGX"
            elif variant_choice == '2':
                variant = "ADFGVX"
            elif variant_choice == '3':
                variant = "ADFGVXZ"
            else:
                print("Zgjedhje e gabuar! Kthehemi te ADFGX.")
                variant = "ADFGX"

            # Decrypting a message
            decrypted_message = polybius_decrypt(message, variant)
            print("\nMesazhi i dekriptuar:", decrypted_message)

        elif choice == '3':
            print("Dalje...")
            break

        else:
            print("Zgjedhje e gabuar! Ju lutem zgjidhni 1, 2, or 3.")