def caesar_encrypt(text: str, key: int, alphabet: str) -> str:
    """Шифрует текст с помощью шифра Цезаря

    Args:
        text (str): текст, который необходимо зашифровать
        key (int): сдвиг
        alphabet (str): алфавит, по которому будет производиться сдвиг

    Returns:
        str: зашифрованный текст
    """
    coded_words: list[str] = []
    for char in text:
        if char.lower() in alphabet: 
            index = (alphabet.index(char.lower()))
            new_char = alphabet[((index + key) % len(alphabet))]
            if char.isupper():
                new_char = new_char.upper()
            coded_words.append(new_char)
        else:
            coded_words.append(char)
        
    return("".join(coded_words))

def ceasar_decrypt(text: str, key: int, alphabet: str) -> str:
    """Дешифрует текст с помощью шифра Цезаря

    Args:
        text (str): текст, который необходимо дешифровать
        key (int): сдвиг, изпользованный для шифрования задаваемого текста
        alphabet (str): алфавит, по которому будет производиться сдвиг

    Returns:
        str: _description_
    """
    coded_words: list[str] = []
    for char in text:
        if char.lower() in alphabet: 
            index = (alphabet.index(char.lower()))
            new_char = alphabet[((index - key) % len(alphabet))]
            if char.isupper():
                new_char = new_char.upper()
            coded_words.append(new_char)
        else:
            coded_words.append(char)
        
    return("".join(coded_words))