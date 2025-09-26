from typing import Any

from mode_1.asymmetric_cipher import RSAEncryption
from mode_1.keys_generation import KeyGeneration
from mode_1.keys_serialization import KeySerialization
from mode_2.simmetric_encrypt import CAST5_encrypt
from mode_3.simmetric_decrypt import CAST5_decrypt
from tools import FileWork


class ModesManager:
    """
    Class, that contains methods for each mode of this programm
    """
    @staticmethod
    def mode_1(sym_key_len: int, settings: dict[str, Any]):
        """Сontains all the functions calls needed to generate keys 

        Args:
            sym_key_len (int): Length of the simmetric key
            settings (dict[str, Any]): Contains settings, file paths, etc.
        """
        print("Generating a symmetric encryption key.")
        symmetric_key = KeyGeneration.generate_symmetric_key(sym_key_len)
        print("Generating private and public keys for asymmetric encryption..")
        private_key, public_key = KeyGeneration.generate_assymetric_keys()
        
        print("Encrypting symmetric key...")
        encrypted_symmetric_key = RSAEncryption.RSA_encrypt(public_key, symmetric_key)
        print("Saving symmetric key.")
        FileWork.save_byte_txt(settings["symmetric_key_file"], encrypted_symmetric_key)
        
        print("Serializing private key..")
        KeySerialization.serialize_private_key(private_key, settings["private_key_file"])
        print("Serializing public key...")
        KeySerialization.serialize_public_key(public_key, settings["public_key_file"])
        
        print("Program completed successfully!")
        return
        
        
    @staticmethod    
    def mode_2(settings: dict[str, Any]):
        """Сontains all the functions calls needed to encrypt text

        Args:
            settings (dict[str, Any]): Contains settings, file paths, etc.
        """
        private_key = KeySerialization.deserialize_private_key(settings["private_key_file"])
        symmetric_enkey = FileWork.read_byte_txt(settings["symmetric_key_file"])
        symmetric_key = RSAEncryption.RSA_decrypt(private_key, symmetric_enkey) # type: ignore
        
        plaintext = FileWork.read_txt(settings["plaintext_file"])
        byte_plaintext = plaintext.encode()
        
        encoded_text = CAST5_encrypt(byte_plaintext, symmetric_key)
        FileWork.save_byte_txt(settings["ciphertext_file"], encoded_text)
        return
    
    
    @staticmethod
    def mode_3(settings: dict[str, Any]):
        """Сontains all the functions calls needed to decrypt text

        Args:
            settings (dict[str, Any]): Contains settings, file paths, etc.
        """
        private_key = KeySerialization.deserialize_private_key(settings["private_key_file"])
        symmetric_enkey = FileWork.read_byte_txt(settings["symmetric_key_file"])
        symmetric_key = RSAEncryption.RSA_decrypt(private_key, symmetric_enkey) # type: ignore
        
        ciphertext = FileWork.read_byte_txt(settings["ciphertext_file"])
        
        byte_plaintext = CAST5_decrypt(ciphertext, symmetric_key)
        plaintext = byte_plaintext.decode("utf-8")

        FileWork.save_txt(settings["decrypted_text_file"], plaintext)
        return