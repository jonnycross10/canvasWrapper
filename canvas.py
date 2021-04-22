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


obj = Canvas("https://csus.instructure.com/api/v1/courses", "*******************")

print(obj.getClassData())
