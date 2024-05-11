import string
import random
# from typing import Any
from pyperclip import copy
# Stub for pyperclip module
# class Pyperclip:
#     @staticmethod
#     def copy(text: str) -> None:
#         pass

# # Dummy variable to make MyPy happy
# pyperclip: Any = Pyperclip()

def generate_random_string(length: int) -> str:
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(length))
    copy(random_string)
    return random_string
inputLength:int = int(input("Enter the length of the string You want to generate...It automatically copied ->   "))
print(generate_random_string(inputLength))
print("\ncopied to clipboard! paste it anywhere you want...")
