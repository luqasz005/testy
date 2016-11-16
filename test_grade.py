import unittest
from kol2_gr2 import Grade
from kol2_gr2 import Course

class test_Grade(unittest.TestCase):
	def setUp(self):
		self.value = 5
		self.course = Course('Math')
		self.test = Grade(self.value, self.course)

	def test_init(self):
		self.assertEqual(self.test.value, self.value)
		self.assertEqual(self.test.course, self.course)
	
if __name__ == '__main__':
	unittest.main()

