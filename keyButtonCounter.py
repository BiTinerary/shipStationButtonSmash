import pythoncom, pyHook, os, time, re

def AddAndReplace(numberToAdd):
    holla = int(numberToAdd) + 1
    holla = str(holla)
    print holla
    numberRegex = re.compile(r'\d{3}')
    try:
        with open('attiny85ButtonCounter.txt', 'r+') as writeNewCounter:
            writeNewCounter.write(holla)
    except:
        pass

    with open('README.md', 'r+') as README:
        for line in README:
            print line
            """
            findRegex = numberRegex.search(str(line))
            foundMatch = findRegex.group()
            print foundMatch
            #line.replace(numberRegex, holla)
            """

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