# package
import input as ip
import output as op
import network as net
import app
from system import exitApp

def main():
	options=["Choose one of the following sites"]
	options.append("Codechef")
	options.append("Codeforces")
	options.append("Hackerrank")
	options.append("Hackerearth")
	options.append("Topcoder")
	options.append("Back")
	optionChosen = ip.getUserInput(options)
	if optionChosen == len(options)-1 :
		return

	else:
		site = options[optionChosen]
		getEvents(site)


def getEvents(site):

	if site == "Hackerearth":
		lis = net.getHackerEvents()
	else:
		lis = net.getOtherEvents(site)

	if len(lis) == 0:
		op.popUp(site,"No Upcoming Challenges",0)
	options = ["Upcoming challenges on {}".format(site)]
	for elem in lis:
		options.append("{:<50} {:<40} {:>20}".format(elem["Title"],"StartTime : "+elem["Start"],"EndTime : "+elem["End"]))
	options.append("Back")
	try:
		optionChosen = ip.getUserInput(options)
	except KeyboardInterrupt:
		exitApp()
	if optionChosen == len(options)-1 :
		main()
	else:
		minutes = ip.getMinutes(30)
		if minutes == "":
			getEvents(site)
			return
		pb = ip.getPB()
		app.DICTIONARY["Coding"].append({"Title":"{} Challenge".format(site),"Message":options[optionChosen],"Interval":minutes*10,"Counter":minutes*10,"PB":pb})
		op.popUp("Notification Set","For {} every {} minute(s)".format(lis[optionChosen-1]["Title"],minutes),0)