"""[Onsite Day 2] Atbash Cipher"""
def main():
    """main"""
    text = input()
    for i in range(len(text)):
        word = text[i]
        if word.isalpha() == False:
            print(word, end="")
        elif word.islower():
            word = (ord("a") + ord("z")) - ord(word)
            print(chr(word), end="")
        elif word.isupper():
            word = (ord("A") + ord("Z")) - ord(word)
            print(chr(word), end="")
main()
