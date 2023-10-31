from Automating_Web_Application_Testing_in_Python.check_text import check_text
import pytest

def test_step():
    assert "корова" in check_text("карава")


if __name__ == '__main__':
    pytest.main(["-vv"])