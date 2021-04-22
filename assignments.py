import requests
import json
import dateutil.parser
from datetime import *

'''
Throughout this API, the :user_id parameter can be replaced with self as a shortcut for the id of the user accessing the API.
For instance, users/:user_id/page_views can be accessed as users/self/page_views to access the current user's page views.
'''

apiKey = "**********************"

headers = {
  "Authorization":"Bearer "+apiKey
}

r = requests.get("https://csus.instructure.com/api/v1/courses", headers = headers)

data = r.json()

#print(data)
#print(data[]["name"])
def findRightClasses(d):#return actual classes
	correctClass = []
	for i in range(0,len(d)):
		if (len(d[i].keys()) > 10):
			correctClass.append(d[i])
	return(correctClass)

def thisTerm(d): #return classes from this term
	correctClass = []
	
	
	fiveMonthsAgo = datetime.now() - date(0000,5,00)
	for i in range(0,len(d)):
		createdDate = dateutil.parser.parse(d[i]["created_at"])
		if(createdDate>fiveMonthsAgo):
			correctClass.append(d[i])
	return(correctClass)

#created at date within the last 5 months, pop if not

print(thisTerm(findRightClasses(data)))
