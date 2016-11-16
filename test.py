
#Krisznla
import unittest
from kol2_gr2 import Course

class test_Course(unittest.TestCase):
	def setUp(self):
		self.name = 'Math'
		self.test = Course(self.name)

	def test_init(self):
		self.assertEqual(self.test.name, self.name)
	
if __name__ == '__main__':
	unittest.main()

