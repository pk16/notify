# pakcage
import app
import network as net
import input as ip
import output as op
from system import exitApp

def main():
	matchIds,matches = net.getLiveMatches()
	if matches[0] == "No Match in progress":
		op.popUp("Cricket","No match in progress or scheduled soon",0)
		return
	options = ["Matches:"]
	for elem in matches:
		options.append(elem)
	options.append("Back")

	try:
		optionChosen = ip.getUserInput(options)
	except KeyboardInterrupt:
		exitApp()

	if optionChosen == len(options)-1 :
		return

	minutes = ip.getMinutes(1)
	if minutes == "":
		main()
		return
	pb = ip.getPB()
	op.popUp("Notification Set","{} every {} minute(s)".format(options[optionChosen],minutes),0)
	app.DICTIONARY["Cricket"].append({"matchId":matchIds[optionChosen-1] , "Teams":options[optionChosen], "Interval":minutes*10 , "Counter":minutes*10 ,"PB":pb})