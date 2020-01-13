import unittest
from src import BubbleSort

class BubbleSortTest(unittest.TestCase):
    def test_bubbleSort(self):
        # stub
        arr1=[1,2,3,4,5]
        arr2=[4,3,2,1,5]
        arr3=[]
        arr4=[-4,-6,-2,-5,-7]
        arr5=[-1,-3,-5,-7,-9]
        arr6=[1,4,-5,2,-8]
        arr7=[-5,-3,3,6,8]

        # assume
        expected1 = [1,2,3,4,5]
        expected2 = [1,2,3,4,5]
        expected3 = []
        expected4 = [-7,-6,-5,-4,-2]
        expected5 = [-9,-7,-5,-3,-1]
        expected6 = [-8,-5,1,2,4]
        expected7 = [-5, -3, 3, 6, 8]

        # action
        result1 = BubbleSort.bubbleSort_func(arr1)
        result2 = BubbleSort.bubbleSort_func(arr2)
        result3 = BubbleSort.bubbleSort_func(arr3)
        result4 = BubbleSort.bubbleSort_func(arr4)
        result5 = BubbleSort.bubbleSort_func(arr5)
        result6 = BubbleSort.bubbleSort_func(arr6)
        result7 = BubbleSort.bubbleSort_func(arr7)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)
        self.assertEqual(result4, expected4)
        self.assertEqual(result5, expected5)
        self.assertEqual(result6, expected6)
        self.assertEqual(result7, expected7)

if __name__ == '__main__':
    unittest.main()