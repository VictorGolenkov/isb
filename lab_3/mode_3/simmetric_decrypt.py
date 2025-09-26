from cryptography.hazmat.decrepit.ciphers.algorithms import CAST5
from cryptography.hazmat.primitives.ciphers import Cipher, modes
from cryptography.hazmat.primitives import padding


def remove_padding(data: bytes, block_size: int = 8) -> bytes:
    """Remove padding from plaintext, when it decrypted

    Args:
        data (bytes): text needed to remove padding
        block_size (int, optional): Size of block for depadding. Defaults to 8

    Returns:
        bytes: _description_
    """
    unpadder = padding.ANSIX923(block_size * 8).unpadder()
    return unpadder.update(data) + unpadder.finalize()

def CAST5_decrypt(ciphertext: bytes, key: bytes) -> bytes:
    """Decrypts ciphertext using CAST5 encryption algorithm

    Args:
        ciphertext (bytes): Initialization vector + ciphertext needed to decrypt
        key (bytes): simmetric key

    Returns:
        bytes: encrypted text
    """
    iv = ciphertext[:8]
    encrypted_data = ciphertext[8:]

    algorithm = CAST5(key)
    cipher = Cipher(algorithm, modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(encrypted_data) + decryptor.finalize()

    plaintext = remove_padding(padded_plaintext)
    
    return plaintext