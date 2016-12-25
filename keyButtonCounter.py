import pythoncom, pyHook, os, time, re

def AddReplacePush(numberToAdd):
    holla = int(numberToAdd) + 1
    holla = str(holla)
    print holla
    timeSaved = int(holla) * .5
    minutes = float(timeSaved) / 60
    totesMinutes = minutes * 100

    try:
        with open('buttonCounter.txt', 'r+') as writeNewCounter:
            writeNewCounter.write(holla)
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
Keystrokes not pressed: **<kbd>%s</kbd>**<br>
Time saved: **<kbd>%s</kbd>** minutes""" % (holla, totesMinutes))

    except:
        pass

    writeNewCounter.close()
    README.close()
    os.system('git add .')
    os.system('git commit -m "counterUpdate: %s"' % holla)
    os.system('git push')
    time.sleep(1)

def counterCommit():
    with open('buttonCounter.txt', 'r') as readCounter:
        totalNumber = readCounter.readline()
        AddReplacePush(totalNumber)
    readCounter.close()

def onKeyDown(event):
    keyname = event.GetKey()
    if keyname == 'Rmenu':
        counterCommit()
        return 1
    else:
        return 1

hookmgr = pyHook.HookManager()
hookmgr.KeyDown = onKeyDown
hookmgr.HookKeyboard()
pythoncom.PumpMessages()