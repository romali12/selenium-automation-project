#Any pytest file should start with test_or end with_test
#pytest method names should start with test
#Any code should be wrapped in method only
#Method name should have sense
# -k stands for method names execution, -s logs in out put -v stands for more info metadata
#you can run specific file with py.test <filename>
#you can mark (tag) tests @pytest.mark.smoke and then run with -m
#you can skip tests with @pytest.mark.skip
#Any code should be wrapped in method only
#@pytest.mark.xfail
#fixtures are used as setup and tear down method for test cases -conftest file to generalize
#fixture and make it available to all test cases
#datadriven and parameterization can be done with return statement in tuple formate
#when you define fixture scope to class only, it will run once before class is initiated and at the end
import pytest

@pytest.mark.smoke
#@pytest.mark.skip
def test_firstProgram():
    msg = "Hello" #operations
    assert msg == "Hi", "Test failed because strings do not match"

def test_SecondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"
