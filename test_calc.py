import unittest
import calc
import math
import random

# for all the operations in the calculator I take basic operarions as default test cases like checking with (+,-)(-,+)(-,-)(+,+) and by including zeros and float values
class TestCalc(unittest.TestCase):

#For addition I check the test cases with mathmatical functions by importing math module

    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(10,-5),5)
        self.assertEqual(calc.add(-10,5),-5)
        self.assertEqual(calc.add(-10,-5),-15)
        self.assertEqual(calc.add(0,0),0)
        self.assertEqual(calc.add(0.5,0.5),1)
        self.assertEqual(calc.add(1,-0.5),0.5)
        self.assertEqual(calc.add(math.sqrt(4),math.sqrt(4)),4)
        self.assertEqual(calc.add(math.sqrt(4),math.sqrt(4)),4)
        self.assertEqual(calc.add(math.pow(2,2),math.pow(2,2)),8)
        self.assertEqual(calc.add(math.factorial(2),math.factorial(2)),4)
        self.assertEqual(calc.add(math.pow(2,2),math.pow(2,2)),8)
        #self.assertEqual(calc.add(math.nan,0),0) #failure test case
        #self.assertEqual(calc.add(math.pi,math.pi),0)   #failure test case

        


#For subtraction I check the test cases with random modules by importing the random module
#But I make them as comments to show the output without failure test cases
    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5),5)
        self.assertEqual(calc.subtract(10,-5),15)
        self.assertEqual(calc.subtract(-10,5),-15)
        self.assertEqual(calc.subtract(-10,-5),-5)
        self.assertEqual(calc.subtract(0,0),0)
        #self.assertEqual(calc.subtract(random.random(),random.random()),random.random()) #failed test case  because we don't know the random numbers to get the result
        #self.assertEqual(calc.subtract(random.randrange(1,3,1),random.randrange(1,3,1)),0)



    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5),50)
        self.assertEqual(calc.multiply(10,-5),-50)
        self.assertEqual(calc.multiply(-10,5),-50)
        self.assertEqual(calc.multiply(-10,-5),50)
        self.assertEqual(calc.multiply(0,0),0)
        self.assertEqual(calc.multiply(0,55),0)
        self.assertEqual(calc.multiply(-55,0),0)

    def test_divide(self):
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(-1,1),-1)
        self.assertEqual(calc.divide(5,2),2.5)
        self.assertEqual(calc.divide(10,10),1)
        #self.assertEqual(calc.divide(0,0),0)

        with self.assertRaises(ValueError):
            calc.divide(10,0)
            calc.divide(0,0)
        

if __name__ == '__main__':
    unittest.main()