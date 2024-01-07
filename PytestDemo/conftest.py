import pytest


#@pytest.fixture()
@pytest.fixture(scope="class") # if required only class level one start the class and end the class
def setup():
    print("I will Execute First")
    yield
    print("I will execute last")


@pytest.fixture()
def dataLoad():
    print("User Profile data is being created")
    return ("Manish", "Kumar", "rahulshettyacademy.com")


@pytest.fixture(params=[("chrome", "Manish", "Kumar"),("Firefox", "Kumar"),("IE", "MK")])
def crossBrowser(request): # when Params value pass in fixture need to used request
    return request.param


