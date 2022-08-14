import unittest
import solution

class Tests(unittest.TestCase):

    def test_find_val(self):
        nums = []
        target = 0
        want = [-1,-1]
        test = solution.Solution.searchRange(self, nums, target)
        self.assertEqual(test, want)
        pass

    def test_find_val1(self):
        nums = [1]
        target = 0
        want = [-1,-1]
        test = solution.Solution.searchRange(self, nums, target)
        self.assertEqual(test, want)
        pass

    def test_find_val2(self):
        nums = [1]
        target = 1
        want = [0,0]
        test = solution.Solution.searchRange(self, nums, target)
        self.assertEqual(test, want)
        pass

    def test_find_val3(self):
        nums = [2,2]
        target = 2
        want = [0,1]
        test = solution.Solution.searchRange(self, nums, target)
        self.assertEqual(test, want)
        pass

    def test_find_val4(self):
        nums = [1,4]
        target = 4
        want = [1,1]
        test = solution.Solution.searchRange(self, nums, target)
        self.assertEqual(test, want)
        pass

    def test_find_val5(self):
        nums = [5,7,7,8,8,10]
        target = 6
        want = [-1,-1]
        test = solution.Solution.searchRange(self, nums, target)
        self.assertEqual(test, want)
        pass

    def test_find_val6(self):
        nums = [5,7,7,8,8,10]
        target = 8
        want = [3,4]
        test = solution.Solution.searchRange(self, nums, target)
        self.assertEqual(test, want)
        pass

    def test_find_val7(self):
        nums = [5,7,7,8,8,8,10]
        target = 8
        want = [3,5]
        test = solution.Solution.searchRange(self, nums, target)
        self.assertEqual(test, want)
        pass


if __name__ == "__main__":
    unittest.main()
