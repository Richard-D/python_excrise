def manual_iter():
    with open("movie.txt") as f:
        try:
            while True:
                line = next(f.encoding)
                print(line,end = ".")
        except StopIteration:
            pass

manual_iter()

# import unittest
#
# class Test_manual_iter(unittest.TestCase):
#     def test_init(self):

