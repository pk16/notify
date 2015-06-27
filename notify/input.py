# System
from curses import wrapper
import curses
from Tkinter import *
from pushbullet import Pushbullet

# package
import output as op

def printOption(stdscr,options,selected):
	stdscr.clear()
	ctr = 0 
	print curses.LINES
	for index,option in enumerate(options):
		if(index == 0):
			print ctr
			stdscr.addstr(ctr,0,option,curses.color_pair(1))
			ctr=ctr+1
		elif(index!=selected):
			if selected - index + 1 < curses.LINES - 1 and ctr < curses.LINES:
				print ctr
				stdscr.addstr(ctr,10,option, curses.color_pair(0))
				ctr = ctr + 1
		else:
			print ctr
			stdscr.addstr(ctr,10,option, curses.color_pair(2))
			ctr = ctr + 1
	if ctr+1 < curses.LINES:
		stdscr.addstr(ctr+1,0,"Quit or Ctrl+C to close the app. You will not receive any Notifications", curses.color_pair(0))
	stdscr.refresh()


def main(stdscr , options):
	curses.curs_set(False)
	selected = 1
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	while True:
		printOption(stdscr,options,selected)
		event=stdscr.getch()
		if(event == ord("\n")):
			return selected
		elif event == curses.KEY_UP: 
			if (selected!=1):
				selected -=1
				printOption(stdscr,options,selected)
			else:
				selected = len(options)-1
				printOption(stdscr,options,selected)
		elif event == curses.KEY_DOWN:
			if (selected!= len(options)-1):
				selected +=1
				printOption(stdscr,options,selected)
			else:
				selected = 1
				printOption(stdscr,options,selected)


def getUserInput(options):
	selected = wrapper(main,options)
	return selected

def inputData(title,label):
    top = Tk()
    top.title(title)
    inputData.x=""
    def getData():
        inputData.x=E1.get()
        top.destroy()
    L1=Label(top,text = label)
    L1.pack()
    E1=Entry(top, bd=3)
    E1.pack()
    B1=Button(top, text = "OK", command = getData , bd = 3)
    B1.pack(side = LEFT)
    B2=Button(top, text = "Cancel", command = top.destroy , bd = 3)
    B2.pack(side = LEFT)

    top.mainloop()
    return inputData.x

def getMinutes(default):
	minutes = inputData("Frequency","Interval (minutes)")
	interval = default
	if minutes == "":
		return ""
	try:
		interval = int(minutes)
	except Exception as e:
		op.popUp("Input Error","Not integer.\nDefault Interval:{} minutes".format(default),0)
		interval = default
	return interval

def getPB():
	top = Tk()
	top.title("Pushbullet Notification")
	getPB.x=0
	def yes():
		getPB.x=1
		top.destroy()
	L1=Label(top,text = "Want Notification on PushBullet devices after set up?")
	L1.pack()
	B1=Button(top, text = "Yes", command = yes , bd = 3)
	B1.pack(side = LEFT)
	B2=Button(top, text = "No", command = top.destroy , bd = 3)
	B2.pack(side = LEFT)

	top.mainloop()
	return getPB.x