#system
from pushbullet import Pushbullet
from threading import Thread

#package
import input as ip
import output as op
from system import exitApp
import tweet
import custom
import threading
import remove
import coding
import cricket

DICTIONARY = { "Cricket":[] , "Coding":[] , "Tweets":[] , "Custom":[] }
PBon = 0
PBobj = ""
t_stop=threading.Event()

def main():
	global PBon
	global PBobj
	PB=""
	thread = Thread(target = op.thread_func, args = (t_stop,))
	thread.start()
	while True:
		options = ["Choose one of the following"]
		options.append("Cricket Scores")
		options.append("Coding Contest Updates")
		options.append("Tweets")
		options.append("Custom Notification with user defined frequency")
		options.append("Remove any set notification")
		if(PB == ""):
			options.append("Want Notifications on Your PushBullet Devices? Enter Access Token here.")
			PBon = 0
		else:
			options.append("PushBullet Device Set Up Successfully. Want to remove the Access Token?")
			PBon = 1
		options.append("Quit")
		try:
			optionChosen = ip.getUserInput(options)
		except KeyboardInterrupt:
			exitApp()
		if optionChosen == len(options)-1:
			exitApp()
		if(optionChosen == len(options) -2):
			if(PB == ""):
				PB=ip.inputData("PushBullet","Enter Valid Access Token")
				if PB != "":
					try:
						PBobj=Pushbullet(PB) 
						PBon = 1
						op.popUp("Notify","Successfull Setup",1)
					except Exception as e:
						op.popUp("PushBullet","Wrong Access Token or Network Error\nTry Again",0)
						PB=""
			else:
				op.success()
				PB=""
			continue
		if(optionChosen == 1):
			cricket.main()

		if(optionChosen == 2):
			coding.main()

		if(optionChosen == 3):
			tweet.main()

		if(optionChosen == 4):
			custom.getData()
		
		if(optionChosen == 5):
			remove.main()
		


if __name__ == '__main__':
    main()
