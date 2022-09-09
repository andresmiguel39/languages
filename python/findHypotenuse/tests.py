import unittest
import solution

class Tests(unittest.TestCase):

    def test_find_val(self):
        hickA = []
        hickB = []
        want = []
        test = solution.Hypotenuse.findHypotenuse(self, hickA, hickB)
        self.assertEqual(test, want)
        pass

    def test_find_val1(self):
        hickA = [0]
        hickB = [0]
        want = [0.0]
        test = solution.Hypotenuse.findHypotenuse(self, hickA, hickB)
        self.assertEqual(test, want)
        pass

    def test_find_val2(self):
        hickA = [2]
        hickB = [2]
        want = [2.8284271247461903]
        test = solution.Hypotenuse.findHypotenuse(self, hickA, hickB)
        self.assertEqual(test, want)
        pass

    def test_find_val3(self):
        hickA = [2, 8, 16, 32, 64]
        hickB = [3, 10, 25, 40, 80]
        want = [3.605551275463989, 12.806248474865697, 29.68164415931166, 51.22499389946279, 102.44998779892558]
        test = solution.Hypotenuse.findHypotenuse(self, hickA, hickB)
        self.assertEqual(test, want)
        pass


if __name__ == "__main__":
    unittest.main()
