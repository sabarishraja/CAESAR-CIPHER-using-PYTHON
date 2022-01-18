from logo import logo_1
print(logo_1)
print("WELCOME TO CAESAR CYPHER!!!!!!!!!!")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def caesar(text, shift, direction):
    crypt = ""
    if direction == "decode":
        shift *= -1
    for te in text:
        x = alphabet.index(te)
        y = x + shift
        crypt += alphabet[y]
    print(f"Here's the {direction}d result: {crypt}")
caesar(text,shift,direction)
