# DONE
def whisper_cipher(text: str, shift: int) -> str:
    if not text:
        return ""
    new_txt = ""
    for char in text:
        if char.isalpha():
            new_txt = new_txt + chr(ord(char) + shift)
        else:
            new_txt += char
    return new_txt


def main():
    test = whisper_cipher("ABC123def", 5)
    print(test)


main()
