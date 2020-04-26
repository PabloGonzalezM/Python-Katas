from typing import Callable, Union


def positive_sum(arr: list) -> Union[int, float]: return sum(x for x in arr if x > 0)


lambda_positive_sum: Callable[[list], int] = lambda arr: sum(x for x in arr if x > 0)
