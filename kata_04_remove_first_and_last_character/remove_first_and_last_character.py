from typing import Callable


def remove_char(text: str) -> str: return text[1:-1]


lambda_remove_char: Callable[[str], str] = lambda text: text[1:-1]
