import os
import pytest

from galiboo import Galiboo


@pytest.fixture()
def galiboo():
    """Return galiboo client"""
    return Galiboo(api_key="<API-KEY>")


def full_path(rel_path):
    """Return the full path of given relative path."""
    return os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            rel_path
        )
    )
