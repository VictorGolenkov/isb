import argparse
import tools as t

class modes(Enum):
    MODE_1 = "mode_1"
    MODE_2 = "mode_2"
    MODE_3 = "mode_3"

def parser_for_program() -> argparse.Namespace:
    """Считывает аргументы командной строки при запуске
    Returns:
        argparse.Namespace: 
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--settings_file', '-sf', type=str, help='The path to .json file with settings', default='settings.json')
    parser.add_argument('--mode', '-m', type=str, help='Modes: \t1. mode_1 - keys generation\n' +
                                                              '\t2. mode_2 - encrypt data\n' +
                                                              '\t3. mode_3 - decrypt data\n'
                                                              , default='mode_1')
    args = parser.parse_args()

    return args

def main():
    args = parser_for_program()   
    mode = args.mode
    path_to_stgs = args.settings_file
        
    settings = tools.read_json(path_to_stgs)
    
    match mode:
        case modes.MODE_1:
            
        case modes.MODE_2:
            
        case modes.MODE_3:
            
        case _:
            return
        
        
if __name__ == "__main__":
    main()