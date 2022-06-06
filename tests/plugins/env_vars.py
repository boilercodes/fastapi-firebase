import os

import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_load_initial_conftests() -> None:
    """Initiate required environment variables."""
    os.environ["FIREBASE_PROJECT_ID"] = ""
    os.environ["FIREBASE_PRIVATE_KEY"] = ""
    os.environ["FIREBASE_CLIENT_EMAIL"] = ""
