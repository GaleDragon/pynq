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
        print r
        self.assertEquals( r.keys(), ["a", "b"] )
        
if __name__=="__main__":
    unittest.main()