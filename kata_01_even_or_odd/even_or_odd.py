from typing import Callable


def even_or_odd(number: int) -> str: return 'Even' if number % 2 == 0 else 'Odd'


lambda_even_or_odd: Callable[[int], str] = lambda number: 'Even' if number % 2 == 0 else 'Odd'
