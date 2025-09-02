import task_1.encryption as t1

import tools as tools

def main():
    
    settings = tools.read_json("settings.json")

    
    #text: str, key: int, alphabet: str
    encrypted_text = t1.caesar_encrypt(
        tools.read_txt(settings["original_text"]),
        settings["key"],
        settings["alphabet"]
    )
    
    # decrypted_text = t1.ceasar_decrypt(
    #     encrypted_text,
    #     settings["key"],
    #     settings["alphabet"]
    # )
    
    # print(encrypted_text)
    # print(decrypted_text)
    
    tools.save_txt(settings["encrypted_text"], encrypted_text)  

if __name__ == "__main__":
    main()