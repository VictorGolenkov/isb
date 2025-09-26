import os

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.rsa import (RSAPrivateKey,
                                                           RSAPublicKey)


class KeyGeneration:
    """
    Class, that contains methods for key generation
    """
    @staticmethod
    def generate_symmetric_key(key_len: int) -> bytes:
        """
        Generate a cryptographically secure symmetric key
        
        Args:
            key_len: Key length in bits (40-128, must be multiple of 8)
        
        Returns:
            bytes: Generated key as bytes object
        
        Raises:
            ValueError: If key length is invalid
        """
        byte_length = key_len // 8
        key = os.urandom(byte_length)

        return key
    
    
    @staticmethod
    def generate_assymetric_keys() -> tuple[RSAPrivateKey,RSAPublicKey]:
        """Generate RSA asymmetric key pair

        Returns:
            tuple[RSAPrivateKey,RSAPublicKey]: Tuple with private and public keys
        """
        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        private_key = keys
        public_key = keys.public_key()
        
        return private_key, public_key

