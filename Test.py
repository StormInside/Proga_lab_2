import unittest
from Arr import Arr

class Test(unittest.TestCase):

    def setUp(self):

        randomlist = [1,4,6,4,5,2]

        self.arr1 = Arr()
        self.arr2 = Arr(ascending_order=False)

        self.arr3 = Arr(content=randomlist)
        self.arr4 = Arr(content=randomlist, ascending_order=False)

    def test_add_one(self):

        potential_list = [1,2,3,4,4,5,6]

        self.arr1.add_one(3)
        self.assertEqual(self.arr1.to_list(), [3])

        self.arr3.add_one(3)
        self.assertEqual(self.arr3.to_list(), potential_list)

        self.arr4.add_one(3)
        self.assertEqual(self.arr4.to_list(), sorted(potential_list, reverse=True))

    def test_dell_one(self):

        potential_list = [1,2,4,5,6]

        self.arr1.add_one(3)
        self.arr1.dell_one(3)
        self.assertEqual(self.arr1.to_list(), [])

        self.arr3.dell_one(4)
        self.assertEqual(self.arr3.to_list(), potential_list)

        self.arr4.dell_one(4)
        self.assertEqual(self.arr4.to_list(), sorted(potential_list, reverse=True))

    def test_clear(self):

        self.arr4.clear()
        self.assertEqual(self.arr4.to_list(), [])

    def test_merge(self):

        potential_list = [1,1,2,2,4,4,4,4,5,5,6,6]

        li = self.arr3.merge(self.arr4, to_list=True)
        self.assertEqual(li, potential_list)

        li = self.arr3.merge(self.arr3, to_list=True)
        self.assertEqual(li, potential_list)

    def test_ch_order(self):

        potential_list = [1,2,4,4,5,6]

        self.assertEqual(self.arr3.ch_order(), sorted(potential_list, reverse=True))

        self.assertEqual(self.arr4.ch_order(), potential_list)



if __name__ == '__main__':
    unittest.main()
    
    