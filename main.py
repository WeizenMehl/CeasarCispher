eng_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ger_alphabet = eng_alphabet + ['ä', 'ö', 'ü', 'ß']
ita_alphabet = eng_alphabet + ['à', 'è', 'é', 'ì', 'ò', 'ù']
combined_alphabet = eng_alphabet + ['ä', 'ö', 'ü', 'ß'] + ['à', 'è', 'é', 'ì', 'ò', 'ù']

def crypting(text,shift,alphabet,type):
    alphabet_length = len(alphabet)
    cryptedText = []
    for c in text:
        if(c.lower() in alphabet):
            index = alphabet.index(c.lower())
            if type: temp = alphabet[(index - shift) % alphabet_length]
            else: temp = alphabet[(index + shift) % alphabet_length]
            if(c.isupper()):
                temp = temp.upper()
        else:
            temp = c
        cryptedText.append(temp)
    return cryptedText

def decryptGuess(text,alphabet):
    alphabet_length = len(alphabet)
    guesses = []
    for i in range(1,alphabet_length):
        guesses.append(''.join(crypting(text,i, alphabet,True)))
    return guesses

print(f"Select a alphabet you want to use:\n\tEng[0]\n\tGer[1]\n\tIta[2]\n\tCombined Alphabet[3]")
selection = int(input())
alphabet = []
if selection == 0:
    alphabet = eng_alphabet
elif selection == 1:
    alphabet = ger_alphabet
elif selection == 2:
    alphabet = ita_alphabet
elif selection == 3:
    alphabet = combined_alphabet

print(f"Encrypt Text[0]\nDecrypt Text[1]")
b = bool(int(input()))
if(b):
    print("Input Text:")
    text = input()
    print(f"Do you know the Shift Value?\nYes[1]\nNo[0]")
    b = bool(int(input()))
    if(b):
        print("Input shift Value")
        shift = int(input())
        print("Decrypted Text: " + ''.join(crypting(text,shift,alphabet,True)))
    else:
        guesses = decryptGuess(text,alphabet)
        i = 1
        for guess in guesses:
            print(f"Guess {i}\n-----------------------------------")
            print(guess)
            print(f"-----------------------------------\n")
            i += 1
else:
    print("Input Text:")
    text = input()
    print("Input shift Value")
    shift = int(input())
    print("Encrypted Text: " + ''.join(crypting(text,shift,alphabet,False)))

