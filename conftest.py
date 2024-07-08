import pytest
from fixture.application import Application


@pytest.fixture(scope="function", autouse=True)
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
