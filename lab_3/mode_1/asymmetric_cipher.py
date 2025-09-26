from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import (RSAPrivateKey,
                                                           RSAPublicKey)


class RSAEncryption:
    """
    Class, that contains encryption/decryption methods, which using RSA-OAEP
    """
    @staticmethod
    def RSA_encrypt(public_key: RSAPublicKey, plaintext: bytes) -> bytes:
        """Encrypts plaintext using PSA-OAEP algorithm

        Args:
            public_key (RSAPublicKey): Public key for RSA-OAEP
            plaintext (bytes): Text to encrypt

        Returns:
            bytes: Encrypted text
        """
        ciphertext: bytes = public_key.encrypt(plaintext, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                    algorithm=hashes.SHA256(),label=None))
        return ciphertext
        
        
    @staticmethod
    def RSA_decrypt(private_key: RSAPrivateKey, ciphertext: bytes) -> bytes:
        """Decrypts ciphertext using PSA-OAEP algorithm

        Args:
            public_key (RSAPublicKey): private key for RSA-OAEP
            plaintext (bytes): Text to decrypt

        Returns:
            bytes: Decrypted text
        """
        dc_text = private_key.decrypt(ciphertext,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                        algorithm=hashes.SHA256(),label=None))
        return dc_text
     
     



