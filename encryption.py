def encrypt_message(message):
    encrypted_message = ""
    skip_next = False

    for i in range(len(message)):
        if skip_next:
            skip_next = False
            continue
        
        char = message[i]

        if char == 'Q':
            if i + 1 < len(message):
                next_char = message[i + 1]
                encrypted_message += shift_left(next_char) + '`'
                skip_next = True
        elif char == 'A':
            if i + 1 < len(message):
                next_char = message[i + 1]
                encrypted_message += shift_left(next_char).upper()
                skip_next = True
        elif char == 'Z':
            if i + 1 < len(message):
                next_char = message[i + 1]
                encrypted_message += '"' + shift_left(next_char)
                skip_next = True
        else:
            encrypted_message += shift_left(char)

    return encrypted_message


def decrypt_message(message):
    decrypted_message = ""
    skip_next = False

    i = 0
    while i < len(message):
        if skip_next:
            skip_next = False
            i += 1
            continue

        char = message[i]

        if i + 1 < len(message) and message[i + 1] == '`':
            decrypted_message += shift_right(char)
            skip_next = True
        elif char == '"':
            decrypted_message += shift_right(message[i + 1])
            skip_next = True
        else:
            decrypted_message += shift_right(char)

        i += 1

    return decrypted_message


def shift_left(char):
    qwerty = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
    shifted_index = qwerty.find(char.lower()) - 1
    if shifted_index < 0:
        return char
    return qwerty[shifted_index]


def shift_right(char):
    qwerty = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
    shifted_index = qwerty.find(char.lower()) + 1
    if shifted_index >= len(qwerty):
        return char
    return qwerty[shifted_index]


def main():
    print("Projek Enkripsi Gabut wkwkwkwkwk")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        message = input("Enter the message to encrypt: ")
        encrypted_message = encrypt_message(message)
        print("Encrypted message:", encrypted_message)
    elif choice == '2':
        message = input("Enter the message to decrypt: ")
        decrypted_message = decrypt_message(message)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Exiting.")


if __name__ == "__main__":
    main()
