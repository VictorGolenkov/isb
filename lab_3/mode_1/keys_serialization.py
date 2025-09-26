from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.types import (PrivateKeyTypes,
                                                             PublicKeyTypes)

from tools import FileWork


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
        pem_data = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        FileWork.save_byte_txt(file_path, pem_data)


    @staticmethod
    def deserialize_public_key(file_path: str) -> PublicKeyTypes:
        """
        Deserialize public key from PEM file
        
        Args:
            file_path: Path to public key file
        
        Returns:
            RSA public key object
        """
        pem_data = FileWork.read_byte_txt(file_path)
        public_key = serialization.load_pem_public_key(pem_data)
        return public_key


    @staticmethod
    def serialize_private_key(private_key: PrivateKeyTypes, file_path: str) -> None:
        """
        Serialize private key to PEM file
        
        Args:
            private_key: RSA private key object
            file_path: Path to save the private key
        """ 
        pem_data = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption())
        FileWork.save_byte_txt(file_path, pem_data)


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
        pem_data = FileWork.read_byte_txt(file_path)
        private_key = serialization.load_pem_private_key(pem_data,password=None,)
        return private_key
