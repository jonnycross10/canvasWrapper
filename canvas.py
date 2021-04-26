import requests
from assignments import Courses
#a wrapper made by students, for students
class Canvas(object):
	def __init__(self, url, apiKey):
		self.url = url
		self.apiKey = apiKey

	def getClassData(self):
		courseInfo = Courses(self.url,self.apiKey)
		return courseInfo.classData()

	def getClassNames(self):
		classNames = Courses(self.url,self.apiKey)
		return classNames.classNames()

	def getAllAssignments(self):
		currentAssignments = Courses(self.url,self.apiKey)
		return currentAssignments.allAssignments()

	def getUpcomingAssignments(self):
		course = Courses(self.url,self.apiKey)
		return course.upcomingAssignments()


obj = Canvas("https://csus.instructure.com/api/v1/", "11299~LMYUCn8olYHTl1soCXfp9yAA4ybJ46aY2OgZ2IGsFrN4yBQ23j6ZC6BMAAOTYcr0")

#print(obj.getClassData())
#print(obj.getClassNames())
#print(obj.getAllAssignments())
print(obj.getUpcomingAssignments())
