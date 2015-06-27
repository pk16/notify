# system
import yweather

# package
import input as ip
import output as op
import network as net
import app
from system import exitApp


def main():
	options=["Choose an option"]
	options.append("Global Trending")
	options.append("Indian Trending")
	options.append("Custom HashTag")
	options.append("Back")
	try:
		optionChosen = ip.getUserInput(options)
	except KeyboardInterrupt:
		exitApp()
	if optionChosen == 1:
		trending(options[1],1)
	if optionChosen == 2:
		trending(options[2],yweather.Client().fetch_woeid("India"))
	if optionChosen == 3:
		getData()
	if optionChosen == 4:
		return

def trending(name,woeid):
	options = ["Top 10 {}".format(name)]
	op.popUp("Notify","Fetching Data",0)
	trend = net.getTrending(woeid)
	options = options + trend
	options.append("Back")
	try:
		optionChosen = ip.getUserInput(options)
	except KeyboardInterrupt:
		exitApp()
	if optionChosen == len(options)-1 :
		main()
	else:
		minutes = ip.getMinutes(1)
		if minutes == "":
			trending(name,woeid)
		app.DICTIONARY["Tweets"].append({"HashTag":options[optionChosen] , "Interval":minutes*10 , "Counter":minutes*10 })
		op.popUp("Notification Set","Tweets for \"{}\" every {} minute(s)".format(options[optionChosen],minutes),0)

def getData():
	hashtag = ip.inputData("Hashtag","Enter the hashtag")
	if hashtag == "":
		return
	minutes = ip.getMinutes(1)
	if minutes == "":
		main()
		return
	pb = ip.getPB()
	#IN LIST
	app.DICTIONARY["Tweets"].append({"HashTag":hashtag , "Interval":minutes*10 , "Counter":minutes*10 ,"PB":pb})
	op.popUp("Notification Set","Tweets for \"{}\" every {} minute(s)".format(hashtag,minutes),0)