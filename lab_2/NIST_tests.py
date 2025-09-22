import math
import numpy as np
from scipy import special

def frequency_test(sequence: str, N: int) -> float:
    """Функция реализует частотный побитовый тест NIST 

    Args:
        sequence (str): Бинарная последовательность длиной 128

    Raises:
        ValueError: Генерирует исключение если последовательность пустая
        ValueError: Генерирует исключение если последовательность содержит какие-либо символы кроме "0" и "1"
        ValueError: Генерирует исключение если длина последовательности не 128 бит

    Returns:
        float: P-значение
    """
    try:
        if not sequence:
            raise ValueError("Пустая последовательность")
        if not all(bit in '01' for bit in sequence):
            raise ValueError("Последовательность должна содержать только '0' и '1'")
    
        S_n = 0
        for bit in sequence:
            S_n += 1 if bit == '1' else -1
        S_n = S_n/np.sqrt(len(sequence))
    
        P = math.erfc(S_n / np.sqrt(2))

    except ValueError as e:
        print(f"Ошибка в данных: {e}")
        return -1
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return -1
    
    return P

def indentical_bits(sequence: str, N: int) -> float:
    """Функция реализует тест NIST на одинаковые подряд идущие биты

    Args:
        sequence (str): Бинарная последовательность длиной 128

    Raises:
        ValueError: Генерирует исключение если последовательность пустая
        ValueError: Генерирует исключение если последовательность содержит какие-либо символы кроме "0" и "1"
        ValueError: Генерирует исключение если длина последовательности не 128 бит

    Returns:
        float: P-значение
    """
    try:
        if not sequence:
            raise ValueError("Пустая последовательность")
        if not all(bit in '01' for bit in sequence):
            raise ValueError("Последовательность должна содержать только '0' и '1'")
    
        zeta = sum(int(bit) for bit in sequence) / N
        
        if(np.abs(zeta-0.5) >= 2/np.sqrt(N)):
            return 0
        
        V_n = 0
        prev = sequence[0]
        for bit in sequence[1:]:
            if bit != prev:
                V_n += 1
            prev = bit
                
        P = math.erfc(abs(V_n - (2 * N * zeta * (1-zeta))) /
            (2 * np.sqrt(2 * N) * zeta * (1 - zeta)))
            
    except ValueError as e:
        print(f"Ошибка в данных: {e}")
        return -1
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return -1
    
    return P

def longest_seq(sequence: str, p_i: str, N: int, M: int) -> float:
    """Функция реализует тест NIST на самую длинную последовательность единиц в блоке
    Args:
        sequence (str): Бинарная последовательность длиной 128

    Raises:
        ValueError: Генерирует исключение если последовательность пустая
        ValueError: Генерирует исключение если последовательность содержит какие-либо символы кроме "0" и "1"
        ValueError: Генерирует исключение если длина последовательности не 128 бит

    Returns:
        float: P-значение
    """
    try:
        if not sequence:
            raise ValueError("Пустая последовательность")
        if not all(bit in '01' for bit in sequence):
            raise ValueError("Последовательность должна содержать только '0' и '1'")
    
        num_of_blocks = N // M
        blocks = (sequence[i * M:(i + 1) * M] for i in range(num_of_blocks))
        
        statistics = [0] * 4
        
        for block in blocks:  
            curr_n = 0          
            max_n = 0
            
            for bit in block:
                if bit == "1":
                    curr_n += 1
                    max_n = max(max_n, curr_n)
                else:
                    curr_n = 0
                    
            match max_n:
                case n if n <= 1:
                    statistics[0] += 1
                case 2:
                    statistics[1] += 1
                case 3:
                    statistics[2] += 1
                case _:
                    statistics[3] += 1 
        
        xi_square = 0
        p_in = (float(p) for p in p_i)
                
        for v, p in zip(statistics, p_in):
            xi_square += (v - 16 * p) ** 2 / (16 * p)
        
        P = (special.gammaincc(3/2, xi_square/2))
    
    except ValueError as e:
        print(f"Ошибка в данных: {e}")
        return -1
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return -1
    
    return P