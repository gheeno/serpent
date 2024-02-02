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
    print(f"container is {char_joined}")    
    print(f"The encoded text is {_text}")

if __name__ == '__main__':
    encrypt(text, shift)