import json
from typing import Any


class FileWork:
    """
    Class, that contains methods for work with files
    """
    @staticmethod
    def read_txt(file_name: str) -> str:
        """Reading text from .txt file

        Args:
            file_name (str): File path

        Returns:
            str: File contents
        """
        try:
            with open(file_name, 'r', encoding="utf-8") as f:
                text: str = f.read()
                return text
        except Exception as e:
            print(f"Error: {e}")
            return ""
    
    
    @staticmethod
    def save_txt(file_name: str, text: str):
        """Deletes the contents of a file and stores new text in it
        If file doesn't exists, creates it

        Args:
            file_name (str): File path
            text (str): Text to be saved
        """
        try:
            with open(file_name, 'w', encoding="utf-8") as f:
                f.write(text)
        except Exception as e:
            print(f"Error: {e}")
            
            
    @staticmethod
    def read_json(file_name: str) -> dict[str, Any]:
        """Reading data from .json file

        Args:
            file_name (str): File path

        Returns:
            Dict[str, Any]: A dictionary of objects contained in the .json file
        """
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                return(json.load(f))
        except Exception as e:
            print(f"Error: {e}")
            return {}
    
    
    @staticmethod    
    def save_json(file_name: str, data: dict[str, Any]):
        """Deletes the contents of the .json file and stores new data in it
        If file doesn't exists, creates it

        Args:
            file_name (str): File path
            text (str): Dictionary with to be saved
        """
        try:
            with open(file_name, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error: {e}")
            
            
    @staticmethod
    def read_byte_txt(file_name: str) -> bytes:
        """Reading text in binary mode from .txt file

        Args:
            file_name (str): File path

        Returns:
            bytes: File contents
        """
        try:
            with open(file_name, "rb") as f:
                data = f.read()
            return data
        except Exception as e:
            print(f"Error: {e}")
            return b''
    
    
    @staticmethod
    def save_byte_txt(file_name: str, data: bytes):
        """Deletes the contents of a file and stores in binaru mode new text in it
        If file doesn't exists, creates it

        Args:
            file_name (str): File path
            text (str): Data to be saved
        """
        try:
            with open(file_name, 'wb') as f:
                f.write(data)
        except Exception as e:
            print(f"Error: {e}")