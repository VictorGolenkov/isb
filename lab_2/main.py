import NIST_tests as tst
import tools as t

def gen_report(binary_sequence: str, filename: str, lan: str, p_i: str, len_of_binary_sequense: int, len_of_block: int):
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
            
            results = [tst.frequency_test(binary_sequence, len_of_binary_sequense), 
                    tst.indentical_bits(binary_sequence, len_of_binary_sequense), 
                    tst.longest_seq(binary_sequence, p_i, len_of_binary_sequense, len_of_block)]
            
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
    SETTINGS = t.read_json("settings.json")
    SEQUENCES = t.read_json(SETTINGS["gen_seq"])
    
    CPP_SEQUENCE = SEQUENCES["cpp"]
    JAVA_SEQUENCE = SEQUENCES["java"]
    
    CPP_REPORT_PATH = SETTINGS["Lan_1_report"]
    JAVA_REPORT_PATH = SETTINGS["Lan_2_report"]
    CPP_LANGUAGE_NAME = SETTINGS["Lan_1"]
    JAVA_LANGUAGE_NAME = SETTINGS["Lan_2"]
    P_I = SETTINGS["p_i"]
    SEQUENCE_LENGTH = int(SETTINGS["len_of_seq"])
    BLOCK_LENGTH = int(SETTINGS["len_of_block"])
    
    gen_report(CPP_SEQUENCE, CPP_REPORT_PATH, CPP_LANGUAGE_NAME, 
                P_I, SEQUENCE_LENGTH, BLOCK_LENGTH)
    gen_report(JAVA_SEQUENCE, JAVA_REPORT_PATH, JAVA_LANGUAGE_NAME, 
               P_I, SEQUENCE_LENGTH, BLOCK_LENGTH)
        
if __name__ == "__main__":
    main()
    