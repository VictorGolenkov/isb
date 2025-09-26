from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.types import (PrivateKeyTypes,
                                                             PublicKeyTypes)



class KeySerialization:
    """
    Class, that contains methods for key serialization
    """
    @staticmethod
    def serialize_public_key(public_key: PublicKeyTypes, file_path: str) -> None:
        """
        Serialize public key to PEM file
        
        Args:
            public_key: RSA public key object
            file_path: Path to save the public key
        """ 
        with open(file_path, 'wb') as f:
            pem_data = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
            f.write(pem_data)


    @staticmethod
    def deserialize_public_key(file_path: str) -> PublicKeyTypes:
        """
        Deserialize public key from PEM file
        
        Args:
            file_path: Path to public key file
        
        Returns:
            RSA public key object
        """
        with open(file_path, 'rb') as f:
            public_key = serialization.load_pem_public_key(f.read())
        return public_key


    @staticmethod
    def serialize_private_key(private_key: PrivateKeyTypes, file_path: str) -> None:
        """
        Serialize private key to PEM file
        
        Args:
            private_key: RSA private key object
            file_path: Path to save the private key
        """ 
        with open(file_path, 'wb') as f:
            f.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption())
                )


    @staticmethod
    def deserialize_private_key(file_path: str) -> PrivateKeyTypes:
        """
        Deserialize private key from PEM file
        
        Args:
            file_path: Path to private key file
            password: Password if key is encrypted
        
        Returns:
            RSA private key object
        """
        with open(file_path, 'rb') as f:
            private_key = serialization.load_pem_private_key(f.read(),password=None,)
        return private_key
