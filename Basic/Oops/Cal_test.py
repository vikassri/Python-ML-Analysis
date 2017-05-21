import unittest

from addition import Cal


class CalTest(unittest.TestCase):

    def test(self):
        cal = Cal(5, 4)
        self.assertEqual(Cal.add(cal), 9)
        self.assertEqual(Cal.sub(cal), 1)


if __name__ == "__main__":
    unittest.main()