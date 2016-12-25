import pythoncom, pyHook, os, time

def AddAndReplace(numberToAdd):
    holla = int(numberToAdd) + 1
    holla = str(holla)
    print holla
    try:
        with open('attiny85ButtonCounter.txt', 'r+') as writeNewCounter:
            writeNewCounter.write(holla)
    except:
        pass

    try:
        with open('README.md', 'r+') as README:
            for line in README:
                print line
    except:
        pass

    writeNewCounter.close()
    README.close()
    os.system('git add .')
    os.system('git commit -m "counterUpdate: %s"' % holla)
    os.system('git push')
    time.sleep(1)

def counterCommit():
    with open('attiny85ButtonCounter.txt', 'r') as readCounter:
        totalNumber = readCounter.readline()
        AddAndReplace(totalNumber)
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