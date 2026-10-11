def vigenere_encrypt(plaintext, keyword):
    ciphertext = []
    keyword = keyword.upper()
    keyword_index = 0
    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            p_val = ord(char) - ord('A')
            k_char = keyword[keyword_index % len(keyword)]
            k_val = ord(k_char) - ord('A')
            encrypted_val = (p_val + k_val) % 26
            encrypted_char = chr(encrypted_val + ord('A'))

            if not is_upper:
                encrypted_char = encrypted_char.lower()
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(char)
        keyword_index += 1
    return "".join(ciphertext)

# test function
if __name__ == "__main__":
    message = "THE EAGLE HAS LANDED"
    key = "DAVINCI"
    encrypted_message = vigenere_encrypt(message, key)
    print(f"Plaintext: {message}")
    print(f"Keyword: {key}")
    print(f"Ciphertext: {encrypted_message}")

# printing vigenere square
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def vigenere_sq(alphabet):
    header = " | " + " | ".join(alphabet) + " |"
    print(header)
    print("-" * len(header))
# loop through each row
for i in range(len(alphabet)):
    row_letters = []
    for j in range(len(alphabet)):
        shifted_index = (j + i) % len(alphabet)
        row_letters.append(alphabet[shifted_index])
    row_str = F"{alphabet[i]} | " + " | ".join(row_letters) + " |"
    print(row_str)

# test
vigenere_sq(alphabet)

# encryption functions
def letter_to_index(letter, alphabet):
    return alphabet.index(letter.upper())
def index_to_letter(index, alphabet):
    return alphabet[index % len(alphabet)]

def vigenere_index(key_letter, plaintext_letter, alphabet):
    p_idx = letter_to_index(plaintext_letter, alphabet)
    k_idx = letter_to_index(key_letter, alphabet)
    cipher_idx = (p_idx + k_idx) % len(alphabet)
    return index_to_letter(cipher_idx, alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    ciphertext = []
    key_index = 0

    for char in plaintext:
        if char.upper() in alphabet:
            is_upper = char.isupper()
            current_key_char = key[key_index % len(key)]
            encrypted_char = vigenere_index(current_key_char, char, alphabet)
            if not is_upper:
                encrypted_char = encrypted_char.lower()
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(char)
        key_index += 1
    return "".join(ciphertext)

# test code
if __name__ == "__main__":
    message = "WHO IS THERE"
    key = "HELLO"
    encrypted = encrypt_vigenere(key, message, alphabet)
    print(f"Plaintext: {message}")
    print(f"Keyword: {key}")
    print(f"Ciphertext: {encrypted}")

# decryption bonus
def undo_vigenere(key_letter, cipher_letter, alphabet):
    c_idx = letter_to_index(cipher_letter, alphabet)
    k_idx = letter_to_index(key_letter, alphabet)
    plain_idx = (c_idx - k_idx) % len(alphabet)
    return index_to_letter(plain_idx, alphabet)

def decrypt_vigenere(key, cipher_text, alphabet):
    plaintext = []
    key_index = 0

    for char in cipher_text:
        if char.upper() in alphabet:
            is_upper = char.isupper()
            current_key_char = key[key_index % len(key)]

            plain_char = undo_vigenere(current_key_char, char, alphabet)

            if not is_upper:
                plain_char = plain_char.lower()
            plaintext.append(plain_char)
        else:
            plaintext.append(char)
        key_index += 1
    return "".join(plaintext)

# app bonus
def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while True:
        print("\n--- Vigenere Cipher App ---")
        print("1) Encrypt")
        print("2) Decrypt")
        print("3) Exit")
        choice = input("Select an option (1, 2, or 3): ")

        if choice == "1":
            plaintext = input("Enter plaintext message: ")
            key = input("Enter keyword: ")
            result = encrypt_vigenere(key, plaintext, alphabet)
            print(f"Ciphertext: {result}")

        elif choice == "2":
            ciphertext = input("Enter ciphertext message: ")
            key = input("Enter keyword: ")
            result = decrypt_vigenere(key, ciphertext, alphabet)
            print(f"Plaintext: {result}")

        elif choice == "3":
            print("Exiting app. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
