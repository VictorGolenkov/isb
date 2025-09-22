import task_1.ceasar_cipher as t1
import task_2.encryption_helper as t2
import argparse

import tools as tools

def parser_for_program() -> argparse.Namespace:
    """Считывает аргументы командной строки при запуске

    Returns:
        argparse.Namespace: 
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--settings_file', '-sf', type=str, help='The path to .json file with settings', default='settings.json')
    parser.add_argument('--mode', '-m', type=str, help='Modes: \t1. task_1 - encrypt/decrypt with ceasar chipher\n' +
                                                      '\t2. task_2 - this mode helps with frequency analysis', default='task_2')
    args = parser.parse_args()
    
    return args

def dialog(original_path: str, decrypted_path: str):
    text = tools.read_txt(original_path)
    while(True):
        command = input("Введите команду: ")
        match command:
            case "stat":
                t2.print_stat(text, len(text))
            case "exit":
                return
            case replace_cmd if len(replace_cmd) == 2:
                text = text.replace(command[0], command[1])
            case _:
                print("Ошибка: Такой команды не существует")
        tools.save_txt(decrypted_path, text)

def main():
    
    args = parser_for_program()
    path_to_stgs = args.settings_file
    mode = args.mode
    
    settings = tools.read_json(path_to_stgs)
    
    match mode:
        case "task_1_enc":
            encrypted_text = t1.caesar_encrypt(
                tools.read_txt(settings["original_t1"]),
                settings["key"],
                settings["alphabet"]
            )
            
            tools.save_txt(settings["encrypted_t1"], encrypted_text)
            tools.save_txt(settings["key_path_t1"], str(settings["key"]))  
            
        case "task_1_dec":
            decrypted_text = t1.ceasar_decrypt(
                tools.read_txt(settings["encrypted_t1"]),
                settings["key"],
                settings["alphabet"]
            )    
            
            tools.save_txt(settings["decrypted_t1"], decrypted_text)   
            tools.save_txt(settings["key_path_t1"], str(settings["key"])) 
        
        case "task_2":
            dialog(settings["original_t2"], settings["decrypted_t2"])
            t2_key = t2.create_key(tools.read_txt(settings["original_t2"]), tools.read_txt(settings["decrypted_t2"]))
            tools.save_json(settings["key_path_t2"], t2_key)
            
        case _:
            print("Такого режима не существует")
        
    
if __name__ == "__main__":
    main()