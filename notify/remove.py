# package
import app
import output as op
import input as ip

lis = ["Cricket","Coding","Tweets","Custom"]

def main():
	options = ["Choose an option"]
	for elem in lis:
		if len(app.DICTIONARY[elem]) != 0 :
			options.append(elem)

	if len(options) == 1:
		op.popUp("Error","No notifications set up",0)
		return

	options.append("Remove all notifications")
	options.append("Back")

	try:
		optionChosen = ip.getUserInput(options)
	except KeyboardInterrupt:
		t_stop.set()
		exitApp()

	if(optionChosen == len(options)-2):
		for elem in lis:
			del app.DICTIONARY[elem][:]
		op.popUp("Successfull","Removed all notifications",0)

	if(optionChosen == len(options)-1):
		return

	elem = options[optionChosen]

	if elem == lis[0]:
		cricket()

	if elem == lis[1]:
		coding()

	if elem == lis[2]:
		tweet()

	if elem == lis[3]:
		custom()


def cricket():
	options = ["notification for following matche(s) is set"]
	for elem in app.DICTIONARY[lis[0]]:
		options.append(elem["Teams"])
	options.append("Remove All")
	options.append("Back")
	try:
		optionChosen = ip.getUserInput(options)
	except KeyboardInterrupt:
		t_stop.set()
		exitApp()
	if optionChosen == len(options)-1 :
		main()

	elif optionChosen == len(options)-2 :
		del app.DICTIONARY["Cricket"]
		op.popUp("Successfull","Removed all cricket notifications",0)
		return 

	else:
		del app.DICTIONARY["Cricket"][optionChosen-1]
		op.popUp("Successfull","Removed the notification",0)
	return

def coding():
	options = ["notification for following contests is set"]
	for elem in app.DICTIONARY[lis[1]]:
		options.append(elem["Message"])
	options.append("Remove All")
	options.append("Back")
	try:
		optionChosen = ip.getUserInput(options)
	except KeyboardInterrupt:
		t_stop.set()
		exitApp()
	if optionChosen == len(options)-1 :
		main()

	elif optionChosen == len(options)-2 :
		del app.DICTIONARY["Coding"]
		op.popUp("Successfull","Removed all coding notifications",0)
		return 

	else:
		del app.DICTIONARY["Coding"][optionChosen-1]
		op.popUp("Successfull","Removed the notification",0)

def tweet():
	options = ["Following tweets are set"]
	for elem in app.DICTIONARY[lis[2]]:
		options.append("Hashtag \"{}\" with interval of {} minutes".format(elem["HashTag"],elem["Interval"]/10))
	options.append("Remove All")
	options.append("Back")
	try:
		optionChosen = ip.getUserInput(options)
	except KeyboardInterrupt:
		t_stop.set()
		exitApp()
	if optionChosen == len(options)-1 :
		main()

	elif optionChosen == len(options)-2 :
		del app.DICTIONARY["Tweets"]
		op.popUp("Successfull","Removed all tweet notifications",0)
		return 

	else:
		del app.DICTIONARY["Tweets"][optionChosen-1]
		op.popUp("Successfull","Removed the notification",0)

def custom():
	options = ["Following custom notifications are set"]
	for elem in app.DICTIONARY[lis[3]]:
		options.append("Title \"{}\", message \"{}\" with interval of {} minutes".format(elem["Title"],elem["Message"],elem["Interval"]/10))
	options.append("Remove All")
	options.append("Back")
	try:
		optionChosen = ip.getUserInput(options)
	except KeyboardInterrupt:
		t_stop.set()
		exitApp()
	if optionChosen == len(options)-1 :
		main()

	elif optionChosen == len(options)-2 :
		del app.DICTIONARY["Custom"]
		op.popUp("Successfull","Removed all custom notifications",0)
		return 

	else:
		del app.DICTIONARY["Custom"][optionChosen-1]
		op.popUp("Successfull","Removed the notification",0)

