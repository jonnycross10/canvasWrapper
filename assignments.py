import requests
import json
import dateutil.parser
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pytz


class Courses(object):
	def __init__(self, url, apiKey):
		self.url = url
		self.apiKey = apiKey


	#returns full data set of current classes
	def classData(self):
		headers = { "Authorization":"Bearer "+self.apiKey}

		r = requests.get(self.url+"courses", headers = headers)

		data = r.json()

		def currentClasses(d):
			def findRightClasses(d):#return actual classes
				correctClass = []
				for i in range(0,len(d)):
					if (len(d[i].keys()) > 10):
						correctClass.append(d[i])
				return(correctClass)

			def thisTerm(d): #return classes from this term
				correctClass = []
				utc = pytz.UTC 
				fiveMonthsAgo = utc.localize(datetime.now() + relativedelta(months=-5))
				for i in range(0,len(d)):
					startDate = dateutil.parser.parse(d[i]["start_at"])
					if(startDate>fiveMonthsAgo): #if start date was sooner than 5 months ago, it was this term
						correctClass.append(d[i])
				return(correctClass)
			return(thisTerm(findRightClasses(d)))
		return(currentClasses(data))


	#returns array of current classes
	def classNames(self): 
		clData = self.classData()
		classArr = []
		for i in clData:
			classArr.append(i['name'])
		return classArr


	#returns dictionary of ids
	def classID(self):
		clData = self.classData()
		idDict = []
		for i in clData:
			idDict.append(i['id'])
		return idDict

	#gets current assignments
	def allAssignments(self):
		clData = self.classData()
		ids = self.classID()
		assignments = []
		headers = { "Authorization":"Bearer "+self.apiKey, "order_by": "due_at"}
		#/api/v1/courses/:course_id/assignments
		for i in range(0,len(ids)):
			r = requests.get(self.url+"courses/"+str(ids[i])+"/assignments", headers = headers)
			assignments.append(r.json())
		return assignments

	
	def upcomingAssignments(self):
		assignments = self.allAssignments()
		notDueYet = []
		for i in range(0,len(assignments)):
			notDueYet.append(assignments[i]['name']) #not json anymore??
		return notDueYet


