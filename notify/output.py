# system
import pynotify 
from time import sleep

# package
from system import exitApp
import app
import network as net

def popUp(title, msg , pb):
	try:
		pynotify.init("Notify")
		pynotify.Notification(title, msg, "dialog-information").show()
	except:
		print "Error sending notification"
		exitApp()
	if pb == 1 and app.PBon == 1:
		try:
			app.PBobj.push_note(title,msg)
		except Exception as e:
			popUp("PushBullet","Failure sending notification",0)

def success():
	popUp("Done!" , "",0)

def thread_func(stop_event):
	while (not stop_event.is_set()):
		for lis in app.DICTIONARY["Custom"]:
			if(lis["Counter"]==0):
				popUp(lis["Title"],lis["Message"],lis["PB"])
				lis["Counter"]=lis["Interval"]
			else:
				lis["Counter"]=lis["Counter"]-1
		for lis in app.DICTIONARY["Coding"]:
			if(lis["Counter"]==0):
				popUp(lis["Title"],lis["Message"],lis["PB"])
				lis["Counter"]=lis["Interval"]
			else:
				lis["Counter"]=lis["Counter"]-1
		for lis in app.DICTIONARY["Tweets"]:
			if(lis["Counter"]==0):
				title = "Latest Tweet for {}".format(lis["HashTag"])
				msg = net.getTweet(lis["HashTag"])
				popUp(title,msg,lis["PB"])
				lis["Counter"]=lis["Interval"]
			else:
				lis["Counter"]=lis["Counter"]-1

		for lis in app.DICTIONARY["Cricket"]:
			if(lis["Counter"]==0):
				jsonUrl = "http://www.espncricinfo.com/ci/engine/match/" + lis["matchId"] + ".json"
				playingTeams = net.getPlayingTeamNames(jsonUrl)
				title,msg = net.getLatestScore(jsonUrl, playingTeams)
				popUp(title,msg,lis["PB"])
				lis["Counter"]=lis["Interval"]
			else:
				lis["Counter"]=lis["Counter"]-1

		sleep(6)
