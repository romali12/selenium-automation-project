import pytest

@pytest.fixture
def dataLoad():
    print("User profile data is being created")
    return ["Rahul", "Shetty", "google.com"]

@pytest.fixture(params=[("chrome", "Rahul","Shetty"), ("Firefox", "Rahul")])
def crossBrowser(request):
    return request.param

@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_editprofile(self, dataLoad):
        print(dataLoad[0])
        print(dataLoad[2])
        #assert dataLoad[0] == "Rahul"

def test_crossBrowser(crossBrowser):
        print(crossBrowser)
