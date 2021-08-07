from typing import Union, Callable


def get_percentage_difference(x: Union[int, float], y: Union[int, float]) -> float:
    return (abs(x - y) / x) * 100


def test_several_times(number_of_runs: int = 10) -> Callable:
    def decorator(test_function: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> None:
            successful_attempts_number = 0

            for i in range(number_of_runs):
                successful_attempts_number += test_function(*args, **kwargs)

            assert get_percentage_difference(number_of_runs, successful_attempts_number) <= 10

        return wrapper

    return decorator
