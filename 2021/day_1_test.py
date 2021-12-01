import unittest

import day_1


class MyTestCase(unittest.TestCase):
  def setUp(self):
    self.raw_report = """
    199
    200
    208
    210
    200
    207
    240
    269
    260
    263
    """
    self.report = day_1.parse_report(self.raw_report)

  def test_parse_report(self):
    self.assertListEqual(day_1.parse_report(self.raw_report),
                         [199, 200, 208, 210, 200, 207, 240, 269, 260, 263])

  def test_pairwise(self):
    self.assertListEqual(['AB', 'BC', 'CD', 'DE', 'EF', 'FG'],
                         [''.join(pair) for pair in day_1.pairwise('ABCDEFG')])

  def test_count_depth_increases(self):
    self.assertEqual(day_1.count_depth_increases(self.report), 7)

  def test_threewise(self):
    self.assertListEqual(['ABC', 'BCD', 'CDE', 'DEF', 'EFG'],
                         [''.join(triple) for triple in
                          day_1.threewise('ABCDEFG')])

  def test_count_depth_increases_windowed(self):
    self.assertEqual(day_1.count_depth_increases_windowed(self.report), 5)


if __name__ == '__main__':
  unittest.main()
