import pytest


@pytest.fixture()
def test_data():
    num = 10
    return num

    # yield
    #
    # print("test passed")


def test_method1(test_data):
    assert test_data == 100


def test_method2(test_data):
    assert test_data == 10
