from pynq import List
import unittest

class SelectTest (unittest.TestCase):
    def setUp(self):
        self.l = List( [1, 2, 3, 4, 5 ] )
    def test_select(self):
        a = self.l.select(lambda x: x-1)
        self.assertEquals(a, [0,1,2,3,4])
        
class GroupCase (unittest.TestCase):
    def setUp(self):
        self.l = List(["aardvark", "apple", "bear", "awesome", "bone"])
    def test_group(self):
        r = self.l.group(lambda x: x[0])
        self.assertEquals( r.keys(), ["a", "b"] )
        
class ChainCase (unittest.TestCase):
    def setUp(self):
        self.l = List([0,2,3,6,7,4,9,8,10])
        self.r = List(["aardvark", "apple", "bear", "awesome", "bone"])
    def test_chaining(self):
        r = self.l.select(lambda x: x-2).group(lambda y: y%2)
        self.assertEquals(r, {0: [-2, 0, 4, 2, 6, 8], 1:[1, 5, 7]})
        
        s = self.r.group(lambda x: x[0]).select(lambda y: s[y].average( lambda x: len(x) ) )
        self.assertFalse(False)
        
        
        
if __name__=="__main__":
    unittest.main()