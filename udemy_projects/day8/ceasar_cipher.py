alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(_text, _shift):
    container = []
    for char in _text:
        if char.isalpha():
            index_found = alphabet.index(char)
            encrypted_index = (index_found + _shift) % 26
            container.append(alphabet[encrypted_index])
        else:
            container.append(char) 
    char_joined = ''.join(container)
    print(f"ENCRYPT : The encoded text is {char_joined}")
    return char_joined


def decrypt(_text, _shift):
    container = []
    for char in _text:
        if char.isalpha():
            index_found = alphabet.index(char)
            encrypted_index = (index_found - _shift) % 26
            container.append(alphabet[encrypted_index])
        else:
            container.append(char) 
    char_joined = ''.join(container)
    print(f"DECRYPT : Decoded text is {char_joined}")

if __name__ == '__main__':
    e = encrypt(text, shift)
    decrypt(e, shift)