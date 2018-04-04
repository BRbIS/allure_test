
import pytest
import allure


@pytest.fixture()
def fix_ture(request):

    text = "hello"
    return text

'''
def pytest_generate_tests(metafunc):
    if 'stringinput' in metafunc.fixturenames:
        metafunc.parametrize("stringinput",
                             metafunc.config.getoption('stringinput'))
'''


def pytest_generate_tests(metafunc):
    allure.feature(metafunc.module.__name__)(metafunc.function)
    allure.story(metafunc.function.__name__)(metafunc.function)

