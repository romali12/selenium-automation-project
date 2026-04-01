import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo(self):
        print("I will execute steps in fixturedDemo method")

    def test_fixtureDemo1(self):
        print("I will execute steps in fixturedDemo1 method")

    def test_fixtureDemo2(self):
        print("I will execute steps in fixturedDemo2 method")

    def test_fixtureDemo3(self):
        print("I will execute steps in fixturedDemo3 method")
