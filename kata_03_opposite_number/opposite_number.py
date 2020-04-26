from typing import Callable, Union


def opposite(num: (int, float)) -> Union[int, float]: return -num


lambda_opposite: Callable[[int, float], int] = lambda num: -num
