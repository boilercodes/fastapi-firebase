import functools
from typing import Callable


def use_callbacks(func: Callable) -> Callable:
    """Call the callback or error_callback methods when the function ends."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> None:
        try:
            args[0].callback(func(*args, **kwargs))  # Run callback from self
        except Exception as e:
            args[0].error_callback(e)

    return wrapper
