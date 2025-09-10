def print_stat(text: str, n: int):
    """Печатает для каждого символа в тексте количество его появлений и 
    и долю появлений от общего числа символов.

    Args:
        text (str): Текст, который необходимо обработать
        n (int): Длина обрабатываемого текста
    """
    try:
        set_of_symbols = set(text)
        symbols = {symbol: text.count(symbol) for symbol in set_of_symbols if symbol != '\n'}
        for symbol, num in sorted(symbols.items(), key = lambda item: item[1], reverse = True):
            print(f"'{symbol}'\t{num}\t{round(num/n, 6)}")
    except Exception as e:
        print(f"Error: {e}")
        
def create_key(text1: str, text2: str) -> dict[str, str]:
    """
    Создает словарь подстановки, где каждому символу из text1
    соответствует символ из text2 с тем же порядковым номером.
    
    Args:
        text1 (str): исходный текст (ключи)
        text2 (str): зашифрованный текст (значения)
    
    Returns:
        dict: словарь подстановки
    """
    try:
        substitution_dict: dict[str, str] = {}
        for char1, char2 in zip(text1, text2):
            if char1 != '\n' and char2 != '\n':
                substitution_dict[char2] = char1
    except ValueError as e:
        print(f"Ошибка: {e}")
        return {}
    else:
        return dict(sorted(substitution_dict.items()))