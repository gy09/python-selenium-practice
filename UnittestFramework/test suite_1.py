import unittest
from UnittestFramework.assertunittest import AssertClass
from UnittestFramework.Practice_unittest import Unittest_demo
from UnittestFramework.Unittest_Firsttest import test

tc1 = unittest.TestLoader().loadTestsFromTestCase(AssertClass)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Unittest_demo)
tc3 = unittest.TestLoader().loadTestsFromTestCase(test)

Regression = unittest.TestSuite([tc1, tc2, tc3])

unittest.TextTestRunner().run(Regression)


