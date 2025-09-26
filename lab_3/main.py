import argparse
from enum import Enum

from modes_manager import ModesManager
from tools import FileWork


class Modes(Enum):
    KEY_GEN = "mode_1"
    ENCRYPT = "mode_2"
    DECRYPT = "mode_3"

# def validate_key(value: str) -> int:
#     """Checks if the key is correct

#     Args:
#         value (str): Key, that must be validated

#     Raises:
#         argparse.ArgumentTypeError: Not a number
#         argparse.ArgumentTypeError: Out of range 

#     Returns:
#         int: Validated key
#     """
#     try:
#         ivalue = int(value)
#     except ValueError:
#         raise argparse.ArgumentTypeError(f"Key length must be a number, got: '{value}'")
            
#     if ivalue < 40 or ivalue > 128:
#         raise argparse.ArgumentTypeError(f"Key length must be between 40-128, got: {ivalue}")
            
#     return ivalue

def parser_for_program() -> argparse.Namespace:
    """Parses arguments
    Returns:
        argparse.Namespace: object with parsed arguments
    """
    parser = argparse.ArgumentParser(
            description='Program for working with CAST-5 encryption',
            epilog='Usage example: python program.py --mode mode_2 --key_length 128 --settings settings.json'
        )
    
    parser.add_argument('--settings_file', '-sf', type=str, help='The path to .json file with settings', default='settings.json')
    parser.add_argument('--mode', '-m', type=str, help='Modes: \t1. mode_1 - keys generation\n' +
                                                              '\t2. mode_2 - encrypt data\n' +
                                                              '\t3. mode_3 - decrypt data\n'
                                                              , default=Modes.KEY_GEN)
    parser.add_argument('--key_length', '-kl', type=int, help='Length of the key, in the range from 40 to 128', default=128)
    args = parser.parse_args()

    print("Command line arguments:")
    print(f"  Settings file: {args.settings_file}")
    print(f"  Operation mode: {args.mode}")
    print(f"  Key length: {args.key_length} bits")
    
        #     # Проверка для CAST-5 (перенсти её отсюда)
        # if not (40 <= key_len <= 128):
        #     raise ValueError(f"CAST-5 key length must be 40-128 bits, got: {key_len}")
        
        # if key_len % 8 != 0:
        #     raise ValueError(f"Key length must be multiple of 8, got: {key_len}")
        
    return args



def main():
    args = parser_for_program()
    
    path_to_stgs = args.settings_file  
    settings = FileWork.read_json(path_to_stgs)
    mode = args.mode
    key_length = args.key_length
    
    match mode:
        case Modes.KEY_GEN.value:
            ModesManager.mode_1(key_length, settings)
        case Modes.ENCRYPT.value:
            ModesManager.mode_2(settings)
        case Modes.DECRYPT.value:
            ModesManager.mode_3(settings)
        case _:
            return
        
        
if __name__ == "__main__":
    main()