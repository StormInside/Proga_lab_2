import unittest
import random
from Arr import Arr

class TestMe(unittest.TestCase):

    def setUp(self):

        self.randomlist = random.sample(range(-1000, 1000), 50)
        print(self.randomlist)
        self.testlists = [[1,4,6,4,5,2], [-100,400,60,400,-5000,0], [100,100,100,100,100,100, 2], [5], []]

        self.arr1 = Arr()
        self.arr2 = Arr(ascending_order=False)

        self.arr3 = Arr(content = self.randomlist)
        self.arr4 = Arr(content = self.randomlist, ascending_order=False)


    def test_add_one(self):

        potential_list = self.randomlist
        potential_list.append(3)
        
        self.arr1.add_one(3)
        self.assertEqual(self.arr1.to_list(), [3])

        self.arr3.add_one(3)
        self.assertEqual(self.arr3.to_list(), sorted(potential_list))

        self.arr4.add_one(3)
        self.assertEqual(self.arr4.to_list(), sorted(potential_list, reverse=True)) 

        self.assertRaises(TypeError, self.arr3.add_one)
        self.assertRaises(TypeError, self.arr1.add_one, "a")


    def test_dell_one(self):

        potential_list = self.randomlist

        self.arr1.add_one(3)
        self.arr1.dell_one(3)
        self.assertEqual(self.arr1.to_list(), [])

        self.arr3.add_one(4)
        self.arr3.dell_one(4)
        self.assertEqual(self.arr3.to_list(), sorted(potential_list))
        
        self.arr4.add_one(4)
        self.arr4.dell_one(4)
        self.assertEqual(self.arr4.to_list(), sorted(potential_list, reverse=True))

        self.assertRaises(KeyError, self.arr3.dell_one, 3000)
        

    def test_clear(self):

        arr = self.arr4

        arr.clear()
        self.assertEqual(arr.to_list(), [])


    def test_merge(self):

        potential_list = self.randomlist

        potential_list = potential_list+potential_list

        li = self.arr3.merge(self.arr4, to_list=True)
        self.assertEqual(li, sorted(potential_list))

        li = self.arr4.merge(self.arr3, to_list=True)
        self.assertEqual(li, sorted(potential_list, reverse=True))

    def test_ch_order(self):

        potential_list = self.randomlist

        self.assertEqual(self.arr3.ch_order(), sorted(potential_list, reverse=True))

        self.assertEqual(self.arr4.ch_order(), sorted(potential_list))



if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
    
    
