import NIST_tests as tst
import tools as t

def gen_report(binary_sequence: str, filename: str, lan: str):
    """Сохраняет в файле отчёт о проверке бинарной последовательности тестами NIST.

    Args:
        binary_sequence (str): Проверяемая бинарная последовательность
        filename (str): Имя файла, в котором необходимо сохранить отчёт
        lan (str): Язык, с помощью которого была сгенерирована бинарная последовательность

    Raises:
        ValueError: Значение P = -1
    """
    try:
        with open(filename, 'w', encoding="utf-8") as f:
            
            results = [tst.frequency_test(binary_sequence), 
                    tst.indentical_bits(binary_sequence), 
                    tst.longest_seq(binary_sequence)]
            
            print(f"Двоичная последовательность, сгенерированная с помощью стандартного ГСПЧ языка {lan}: ", file = f)
            print(binary_sequence, file = f)
            f.write("\n")
            print("Результаты тестов NIST для данной двоичной последовательности: ", file = f)

            print(f"Частотный побитовый тест: P = {results[0]}", file = f)
            print(f"Тест на одинаковые подряд идущие биты: P = {results[1]}", file = f)
            print(f"Тест на самую длинную последовательность единиц в блоке: P = {results[2]}", file = f)
                
            check: list[bool] = []
            for P in results:
                if P >= 0.01:
                    check.append(True)
                elif P < 0.01 or P >= 0:
                    check.append(False)
                else:
                    raise ValueError("Получено некорректное значение P")
                    
            f.write("\n")
            if all(check):
                print("Нулевая гипотеза принимается, альтернативная гипотеза опровергается:", file = f)
                print("Последовательность является истинно случайной", file = f)
            else:
                print("Альтернативная гипотеза принимается, нулевая гипотеза опровергается:", file = f)
                print("Последовательность не является истинно случайной", file = f)
                
    except ValueError as e:
        print(f"Ошибка в данных: {e}")
        return
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return

def main():
    
    stgs = t.read_json("settings.json")
    
    sequences = t.read_json(stgs["gen_seq"])
    
    cpp_sequence = sequences["cpp"]
    java_sequence = sequences["java"]
    
    gen_report(cpp_sequence, stgs["Report_C++"], stgs["lan_1"])
    gen_report(java_sequence, stgs["Report_Java"], stgs["lan_2"])
        
if __name__ == "__main__":
    main()
    