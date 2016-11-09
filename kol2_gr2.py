#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

class Course(object):
	name = ''
	
	def __init__(self, name):
		self.name = name


class Grade(object):
	value = ''
	course = Course

	def __init__(self, value, course):
		self.value = value
		self.course = course


class Student(object):
	firstname = ''
	lastname = ''
	grades = []
	attendances = []

	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
	
	def addGrade(self, grade):
		self.grades.append(grade)

	def getAvg(self):
		gradesSum = 0.
		gradesCnt = len(self.grades)

		for grade in self.grades:
			gradesSum += grade.value


		if gradesCnt:
			return gradesSum/gradesCnt
		return 0

	def getCourseAvg(self, course):
		gradesSum = 0.
		gradesCnt = 0

		for grade in self.grades:
			if grade.course.name == course.name:
				gradesSum += grade.value
				gradesCnt += 1

		if gradesCnt:
			return gradesSum/gradesCnt
		return 0

	def add_attendance(self, present):
		self.attendances.append(present)

	def get_attendance_stat(self):
		return 1.*sum(self.attendances)/len(self.attendances)

math = Course("Math")
physics = Course("Physics")

student_a = Student("Tomasz", "Abacki")
student_b = Student("Adam", "Babacki")

student_a.addGrade(Grade(5, math))
student_a.addGrade(Grade(3, math))
student_a.addGrade(Grade(5, physics))

student_a.add_attendance(1)
student_a.add_attendance(1)
student_a.add_attendance(1)
student_a.add_attendance(0)

print "Student "+student_a.firstname+" "+student_a.lastname
print "Grades avg: "+str(student_a.getAvg())
print "Grades for course "+math.name+": "+str(student_a.getCourseAvg(math))
print "Grades for course "+physics.name+": "+str(student_a.getCourseAvg(physics))
print "Attendance "+str(student_a.get_attendance_stat())
