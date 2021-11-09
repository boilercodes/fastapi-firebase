from typing import Any

from app.utils.decorators import use_callbacks


class Object:
    """An example of an object."""

    def __init__(self):
        self.result = None
        self.error = None

    def callback(self, result: Any) -> None:
        """Execute when the pool is completed."""
        self.result = result

    def error_callback(self, error: BaseException) -> None:
        """Execute when the pool throws an error."""
        self.error = error

    @use_callbacks
    def run_successful(self) -> bool:
        """A function that runs successfully."""
        return True

    @use_callbacks
    def run_error(self) -> None:
        """A function that raises an error."""
        raise Exception()


def test_use_callbacks() -> None:
    """Test the use_callbacks decorator."""
    obj = Object()

    obj.run_successful()
    assert obj.result

    obj.run_error()
    assert isinstance(obj.error, Exception)
