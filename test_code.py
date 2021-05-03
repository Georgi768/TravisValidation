import pytest
from src.Index import isHelloWorld


def test_isHelloWorld():
    word = 'Hello World'
    assert (isHelloWorld(word) == word)