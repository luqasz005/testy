import unittest
from kol2_gr2 import Grade
from kol2_gr2 import Course
from kol2_gr2 import Student


class test_Student(unittest.TestCase):
	def setUp(self):
		self.fname = "Tomasz", 
		self.sname = "Abacki"
		self.test = Student(self.fname, self.sname)

	def test_init(self):
		self.assertEqual(self.test.firstname, self.fname)
		self.assertEqual(self.test.lastname, self.sname)
	
	def test_addgrade(self):
		testgrade = Grade(5,"Math")
		test_inst = Student("Tomasz","Abacki")
#		self.assertEqual(, )

if __name__ == '__main__':
	unittest.main()

