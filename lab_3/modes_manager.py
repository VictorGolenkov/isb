from typing import Any

from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey

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
        
        
    @staticmethod    
    def mode_2(settings: dict[str, Any]):
        """Сontains all the functions calls needed to encrypt text

        Args:
            settings (dict[str, Any]): Contains settings, file paths, etc.
        """
        print("Deserializing asymmeytic encryption private key.")
        private_key = KeySerialization.deserialize_private_key(settings["private_key_file"])
        if not isinstance(private_key, RSAPrivateKey):
            raise TypeError("Expected RSA private key, but got different type")
        
        print("Deserializing symmetric encryption key..")
        symmetric_enkey = FileWork.read_byte_txt(settings["symmetric_key_file"])
        print("Decrypting symmetric encryption key...")
        symmetric_key = RSAEncryption.RSA_decrypt(private_key, symmetric_enkey)
        
        print("Reading and encoding plaintext.")
        plaintext = FileWork.read_txt(settings["plaintext_file"])
        byte_plaintext = plaintext.encode()
        
        print("Encrypting plaintext..")
        encoded_text = CAST5_encrypt(byte_plaintext, symmetric_key)
        print("Saving ciphertext...")
        FileWork.save_byte_txt(settings["ciphertext_file"], encoded_text)
        
        print("Program completed successfully!")
    
    
    @staticmethod
    def mode_3(settings: dict[str, Any]):
        """Сontains all the functions calls needed to decrypt text

        Args:
            settings (dict[str, Any]): Contains settings, file paths, etc.
        """
        print("Deserializing asymmeytic encryption private key.")
        private_key = KeySerialization.deserialize_private_key(settings["private_key_file"])
        if not isinstance(private_key, RSAPrivateKey):
            raise TypeError("Expected RSA private key, but got different type")
        print("Deserializing symmetric encryption key..")
        symmetric_enkey = FileWork.read_byte_txt(settings["symmetric_key_file"])
        print("Decrypting symmetric encryption key...")
        symmetric_key = RSAEncryption.RSA_decrypt(private_key, symmetric_enkey)
        
        print("Reading ciphertext.")
        ciphertext = FileWork.read_byte_txt(settings["ciphertext_file"])

        print("Decrypting and decoding ciphertext..")
        byte_plaintext = CAST5_decrypt(ciphertext, symmetric_key)
        plaintext = byte_plaintext.decode("utf-8")

        print("Saving decrypted text...")
        FileWork.save_txt(settings["decrypted_text_file"], plaintext)
        
        print("Program completed successfully!")