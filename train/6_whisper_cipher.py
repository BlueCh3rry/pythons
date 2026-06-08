# DONE
def whisper_cipher(text: str, shift: int) -> str:
    if not text:
        return ""
    new_txt = ""
    for char in text:
        if char.isalpha():
            asc_char = ord(char)
            while shift > 25:
                shift = shift % 25
            if asc_char >= 77 or asc_char >= 109:
                new_txt = new_txt + chr(asc_char + shift)
        else:
            new_txt += char
    return new_txt


def main():
    test = whisper_cipher("xyz", 3)
    print(test)


main()
