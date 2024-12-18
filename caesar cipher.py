def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    shift = shift if mode == "encrypt" else -shift

    for char in text:
        if char.isalpha():  # Check if the character is a letter
            offset = 65 if char.isupper() else 97  # ASCII value for 'A' or 'a'
            result += chr((ord(char) - offset + shift) % 26 + offset) #% 26: Wraps the result within the alphabet range (since there are 26 letters).
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result

# Example Usage
plaintext=input("Enter the plaintext: ") # in case of user input
# plaintext = "CYBERSECURITY"
shift = 4
ciphertext = caesar_cipher(plaintext, shift)
print("Ciphertext:", ciphertext)

decrypted_text = caesar_cipher(ciphertext, shift, mode="decrypt")
print("Decrypted Text:", decrypted_text)