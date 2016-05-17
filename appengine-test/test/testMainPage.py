'''
Created on Apr 25, 2016

@author: user
'''
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        pass

    def testTwo(self):
        self.assertEqual(4, 2+2, None)
        self.assertEqual(6, 3*2, None)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()