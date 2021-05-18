import unittest
import unittest


class AssertClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('#' * 30)
        print("This Class method will be printed only once at the beginning")
        print('#' * 30)

    @classmethod
    def tearDownClass(cls):
        print('#' * 30)
        print("This Class method will be printed only once at the end ")
        print('#' * 30)

    def setUp(self):
        print("This method will run Before every test method")

    def tearDown(self):
        print("This method will run after every test method")

    def test_assertmethodA(self):
        a = True
        self.assertTrue(a, 'a is false')

        b = False
        self.assertFalse(b, 'b' is False)

    def test_assertequalmtd(self):
        a = 10
        b = 20

        self.assertNotEqual(a, b, msg="Both are  equal")


if __name__ == "__main__":
    unittest.main()
