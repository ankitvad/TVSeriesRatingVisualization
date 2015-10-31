#Ankit Vadehra- ankitvad@gmail.com
import json
import matplotlib.pyplot as plt
import pprint
#Just copy any file name here, that is present in the folder:
x = open("tbbt.json")
y = x.read()
pj = json.loads(y)
#To show the structure of my json file...
pprint.pprint(pj,width=1)

#Remaining Part, for visualization..

RATING=[]
NAME=[]
for a in pj['episodes'].values():
	for season in a:
		NAME.append(season['episode-name'])
		RATING.append(season['rating'])
TVSHOW = pj['name']
TOTALRATING = pj['rating']
#Plotting the values...
#x=[None, u'6.7', u'8.4', u'8.4', u'7.9', u'8.2', u'8.1', u'8.5', u'8.3', u'8.4', u'8.2', u'8.2', u'8.3', u'8.1', u'8.4', u'8.2', u'8.4', u'8.4', u'8.6', u'8.5', u'8.0', u'8.4', u'8.2', u'8.4', u'7.7', u'8.0', u'9.0', u'8.5', u'8.6', u'8.4', u'8.5', u'8.1', u'8.5', u'8.2', u'8.4', u'8.5', u'8.5', u'8.1', u'8.2', u'8.3', u'9.0', u'8.7', u'8.4', u'8.3', u'8.9', u'8.1', u'8.4', u'8.4', u'8.8', u'8.3', u'8.3', u'7.9', u'9.2', u'8.1', u'8.2', u'8.2', u'8.9', u'8.3', u'8.4', u'8.3', u'8.4', u'8.1', u'8.7', u'8.4', u'8.4', u'8.2', u'8.2', u'7.9', u'8.0', u'8.2', u'7.7', u'8.7', u'7.9', u'8.3', u'8.1', u'7.5', u'7.8', u'8.4', u'8.4', u'7.9', u'7.8', u'7.9', u'8.4', u'8.3', u'8.3', u'8.7', u'7.8', u'8.3', u'8.6', u'8.8', u'8.4', u'8.1', u'8.2', u'7.9', u'8.1', u'8.2', u'8.2', u'8.6', u'7.8', u'8.7', u'7.7', u'8.3', u'8.0', u'7.9', u'8.0', u'8.0', u'8.3', u'8.2', u'8.3', u'8.3', u'7.9', u'8.1', u'8.6', u'8.0', u'8.1', u'8.7', u'8.1', u'7.9', u'8.5', u'7.9', u'7.7', u'8.8', u'7.8', u'8.2', u'7.6', u'7.7', u'8.0', u'8.4', u'7.8', u'7.6', u'7.5', u'8.3', u'8.1', u'7.6', u'7.7', u'8.0', u'8.1', u'7.8', u'7.8', u'8.1', u'8.3', u'8.2', u'8.0', u'7.9', u'8.5', u'8.3', u'8.2', u'8.0', u'8.5', u'8.5', u'8.0', u'8.4', u'8.1', u'7.8', u'7.9', u'8.1', u'8.1', u'8.1', u'8.0', u'8.2', u'7.9', None, u'7.0', u'7.5', u'6.8', u'7.2', u'7.4', u'7.1', u'7.7', u'8.0', u'7.4', u'6.7', u'7.2', u'7.2', u'7.3', u'8.1', u'8.0', u'7.9', u'7.5', u'7.2', u'7.5', u'7.6', u'7.0', u'7.2', u'7.3', u'8.0']
#Change Line Type Here:
plt.plot(RATING, 'ro', linestyle='-')
plt.title(TVSHOW+"("+TOTALRATING+")")
plt.xlabel("TVShow episode Number")
plt.ylabel("Episode Rating")
#Change The scale Here:
plt.axis([1, len(RATING), 5, 10])
plt.show()

