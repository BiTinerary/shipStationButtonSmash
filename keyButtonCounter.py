import pythoncom, pyHook, os, time, re, pyautogui, time

def AddReplaceString(numberToAdd):
    runningCounter = int(numberToAdd) + 1

    timeSaved = int(runningCounter) * .5
    minutes = float(timeSaved) / 60
    tape = int(runningCounter) * 14
    miletape = float(tape / 5280)

    try:
        with open('buttonCounter.txt', 'r+') as writeNewCounter:
            writeNewCounter.write(str(runningCounter))
            writeNewCounter.close()
    except:
        pass

    try:
        with open('README.md', 'w+') as README:
            README.write(
                """# shipStationButtonSmashCounter<br>
This is a counter for the number of times a custom button is pressed that I made/created/installed at work. <br>
Not so much for practicality, it saves only about 1/2 second/press or 1/2 the total keystrokes, but conceptually has broadened my tech aptitude. <br>
<br>
It's primary use is just to be more cathartic in smashing a gigantic switch everytime something is sold and shipped. <br>
As opposed to pressing <kbd>Alt+P</kbd> or swapping from the keyboard to the mouse. <br>
<br>
Keystrokes **not** pressed: **<kbd>%s</kbd>**<br>
Time saved: **<kbd>%s</kbd>** minutes<br>
**<kbd>%s</kbd>** miles of tape used<br>
<center><img src='https://github.com/BiTinerary/shipStationButtonSmash/blob/master/20170414_124519.jpg'></center>""" % (runningCounter, round(minutes, 2), miletape))
            README.close()
    except:
        pass

    print miletape


def finalCommit
    os.system('git add .')
    os.system('git commit -m "counterUpdate: %s"' % runningCounter)
    os.system('git push')

def counterFile():
    with open('buttonCounter.txt', 'r') as readCounter:
        totalNumber = readCounter.readline()
        AddReplaceString(totalNumber)
    readCounter.close()

def onKeyDown(event):
    keyname = event.GetKey()
    if keyname == 'S':
        counterFile()
        return 1
    else:
        print keyname
        return 1

hookmgr = pyHook.HookManager()
hookmgr.KeyDown = onKeyDown
hookmgr.HookKeyboard()
pythoncom.PumpMessages()