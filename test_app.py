import app
import unittest   # The test framework 
class Test_TestaddFuction(unittest.TestCase):
    def testadd(self):
        self.assertEqual(app.add(3,1), 4)  # Test add function 
    def testadd(self):
        self.assertEqual(app.add(3,2), 5)  # Test add function 


if __name__ == '__main__': 

        unittest.main() 

