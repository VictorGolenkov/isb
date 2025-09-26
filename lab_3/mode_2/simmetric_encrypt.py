import os

from cryptography.hazmat.decrepit.ciphers.algorithms import CAST5
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, modes


def add_padding(data: bytes, block_size: int = 8) -> bytes:
    """
    Добавить паддинг для блочного шифра
    
    Args:
        data: Исходные данные
        block_size: Размер блока (8 байт для CAST-5)
    
    Returns:
        Данные с паддингом
    """
    padder = padding.ANSIX923(block_size * 8).padder()  # PKCS7 лучше ANSIX923
    return padder.update(data) + padder.finalize()

def CAST5_encrypt(plaintext: bytes, key: bytes) -> bytes:
    """Encrypts ciphertext using CAST5 encryption algorithm

    Args:
        plaintext (bytes): plaintext needed to encrypt
        key (bytes): simmetric key

    Returns:
        bytes: Initialization vector + ciphertext
    """
    padded_text = add_padding(plaintext)

    iv = os.urandom(8)
    algorithm = CAST5(key)
    cipher = Cipher(algorithm, modes.CBC(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_text)

    return iv + ciphertext
        

        
