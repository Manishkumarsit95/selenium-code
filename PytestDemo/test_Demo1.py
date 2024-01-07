# Any Pytest files start with test_ or end with _test
# pytest methode name start with test
# any code should be wrapped in to methode only
# can not used same methode in same python file.
# Methode name should have sense
import pytest


@pytest.mark.smokez
def test_firstprogram(setup):
    print("Hello")
@pytest.mark.xfail
def test_GrettingCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])