import requests
import json
import dateutil.parser
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pytz

'''
Throughout this API, the :user_id parameter can be replaced with self as a shortcut for the id of the user accessing the API.
For instance, users/:user_id/page_views can be accessed as users/self/page_views to access the current user's page views.
'''

'''
apiKey = "11299~LMYUCn8olYHTl1soCXfp9yAA4ybJ46aY2OgZ2IGsFrN4yBQ23j6ZC6BMAAOTYcr0"

headers = {
  "Authorization":"Bearer "+apiKey
}
'''
class Courses(object):
	def __init__(self, url, apiKey):
		self.url = url
		self.apiKey = apiKey



	def classData(self):
		headers = { "Authorization":"Bearer "+self.apiKey}

		r = requests.get(self.url+"courses", headers = headers)

		data = r.json()

		#print(data)
		#print(data[]["name"])
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



	def classNames(self):
		clData = self.classData()
		classArr = []
		for i in clData:
			classArr.append(i['name'])
		return classArr


		#print(currentClasses(data))
