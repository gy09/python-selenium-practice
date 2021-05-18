import pytest


@pytest.mark.run(order=2)
def test_run_method_A():
    print("Running the method A")


@pytest.mark.run(order=3)
def test_run_method_B():
    print("Running the method B")


@pytest.mark.run(order=1)
def test_run_method_C():
    print("Running method C")
