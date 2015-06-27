# package
import input as ip
import output as op
import app 

def getData():
	title = ip.inputData("Title","Enter the title")
	if title == "":
		return
	msg = ip.inputData("Message","Enter the message for notification")
	if msg == "":
		return
	minutes = ip.getMinutes(10)
	if minutes == "":
		return
	pb = ip.getPB()
	#IN LIST
	app.DICTIONARY["Custom"].append({"Title":title , "Message":msg , "Interval":minutes*10 , "Counter":minutes*10 , "PB":pb})
	op.popUp("Notification Set","For title \"{}\" and message \"{}\" every {} minute(s)".format(title,msg,minutes),0)