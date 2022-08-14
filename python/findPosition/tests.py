import unittest
import position

class Tests(unittest.TestCase):

    def test_find_val(self):
        nums = []
        target = 0
        want = 0
        test = position.Position.searchPosition(self, nums, target)
        self.assertEqual(test, want)
        pass

    def test_find_val1(self):
        nums = [1]
        target = 0
        want = 0
        test = position.Position.searchPosition(self, nums, target)
        self.assertEqual(test, want)
        pass

    def test_find_val2(self):
        nums = [1]
        target = 1
        want = 0
        test = position.Position.searchPosition(self, nums, target)
        self.assertEqual(test, want)
        pass

    def test_find_val5(self):
        nums = [1,3,5,6]
        target = 5
        want = 2
        test = position.Position.searchPosition(self, nums, target)
        self.assertEqual(test, want)
        pass

    def test_find_val6(self):
        nums = [1,3,5,6]
        target = 2
        want = 1
        test = position.Position.searchPosition(self, nums, target)
        self.assertEqual(test, want)
        pass

    def test_find_val7(self):
        nums = [1,3,5,6]
        target = 7
        want = 4
        test = position.Position.searchPosition(self, nums, target)
        self.assertEqual(test, want)
        pass


if __name__ == "__main__":
    unittest.main()
