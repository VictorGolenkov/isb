import argparse
from enum import Enum

from cryptography.exceptions import InvalidKey, UnsupportedAlgorithm

from modes_manager import ModesManager
from tools import FileWork


class Modes(Enum):
    KEY_GEN = "mode_1"
    ENCRYPT = "mode_2"
    DECRYPT = "mode_3"

def parser_for_program() -> argparse.Namespace:
    """Parses arguments
    Returns:
        argparse.Namespace: object with parsed arguments
    """
    parser = argparse.ArgumentParser(
            description='Program for working with CAST-5 encryption',
            epilog='Usage example: python program.py --mode mode_1 --key_length 128 --settings settings.json'
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
        
    return args



def main():
    """Entry point to the program
    """
    try:
        args = parser_for_program()
        
        path_to_stgs = args.settings_file
        FileWork.is_file_exists(path_to_stgs)  
        
        settings = FileWork.read_json(path_to_stgs)
        
        key_length = args.key_length
        if not (40 <= key_length <= 128):
            raise ValueError(f"CAST-5 key length must be 40-128 bits, got: {key_length}")
        if key_length % 8 != 0:
            raise ValueError(f"Key length must be multiple of 8, got: {key_length}")
        
        mode = args.mode
        match mode:
            case Modes.KEY_GEN.value:
                ModesManager.mode_1(key_length, settings)
            case Modes.ENCRYPT.value:
                ModesManager.mode_2(settings)
            case Modes.DECRYPT.value:
                ModesManager.mode_3(settings)
            case _:
                raise ValueError("This operating mode does not exist.\n"
                                "Use \"python main.py --help\" for information about existing modes")
    
    
    except PermissionError as e:
        print(f"PermissionError: {e}") 
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}") 
    except ValueError as e:
        print(f"ValueError: {e}")
    except KeyError as e:
        print(f"Missing setting: {e}")
    except UnsupportedAlgorithm as e:
        print(f"Cryptographic algorithm not supported: {e}")
    except InvalidKey as e:
        print(f"Key serialization error: {e}")
    except Exception as e:
        print(f"Error: {e}")     
        
if __name__ == "__main__":
    main()