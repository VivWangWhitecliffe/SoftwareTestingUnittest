import inc_dec    # The code to test 

import unittest   # The test framework 
class Test_TestIncrementDecrement(unittest.TestCase): 

    def test_increment(self): 

        self.assertEqual(inc_dec.increment(3), 4)  # Test increment function 

  

    def test_decrement(self): 

        self.assertEqual(inc_dec.decrement(5), 4)  # This test is designed to fail 
    
    def test_power(self): 

        self.assertEqual(inc_dec.tothepoweroftwo(3), 9)  # This test is designed to fail 
        
    if __name__ == '__main__': 

        unittest.main() 