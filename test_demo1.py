import pytest

@pytest.mark.smoke
def test_firstProgram():
    print("HELLO")

@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("GOOD MORNING")
