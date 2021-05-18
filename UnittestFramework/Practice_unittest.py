import unittest


class Unittest_demo(unittest.TestCase):
    def setUp(self):
        print("Run before every test case ")

    def test_methodA(self):
        print("Running the test menthod A")

    def test_methodB(self):
        print("Running the test method B")

    def tearDown(self):
        print("Running after every test case")


if __name__ == "__main__":
    unittest.main(verbosity=2)
