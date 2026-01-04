import pytest
import func as pf


def test_to_uppercase():
    assert pf.to_uppercase("hello") == "HELLO"
    assert pf.to_uppercase("World") == "WORLD"
    assert pf.to_uppercase("") == ""


if __name__ == "__main__":
    pytest.main()