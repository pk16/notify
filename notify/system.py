# system
import sys

# package
import app

def exitApp():
	print "Cleaning Everything"
	app.t_stop.set()
	print "Thank you for using notifier"
	sys.exit()