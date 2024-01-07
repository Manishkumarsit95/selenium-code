# -k stands for method names execution, -s logs in output, -v stand for more info metadata
# You can run specific file with py.test <filename>
# for run specific file - py.test test_Demo2.py -v -s
# To run one test case from 1st file and one test case from 2nd file having CreditCard present in method
# py.test -k CreditCard -v -s
# You can mark (tag) tests @pytest.mark.smoke and then run with -m
# You can skip the test using @pytest.mark.skip
# You can skip the report status of that test case but need to run for further test case use - @pytest.mark.xfail
# Fixtures are used as setup and tear down methode for the test cases - Conftest file to generlaized
# fixture and make it avialable to all the test cases
# datadriven and parameterization can be done with return statement in tuple formate
# when you define the fixure scope to class only it will run once before class is initiated at the end
import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_firstprogram():
    msg = "Hello"
    assert msg == "Hi", "Test Failed because string do not match"

def test_SecondprogramCreditCard():
    a = 4
    b = 6
    assert a + 2 == 6, "Test Failed because value do not match"
