import sys
import re

peakName = ""
geoHashCodeLength = 0
geoHashCode = ""


def ParseInput(inputString):
    regex = "^([!|@|#|$|?|\w]+)=(\d+)<<(.*)";
    res = re.search(regex, inputString)
    if not res:
        return False
    global peakName
    global geoHashCodeLength
    global geoHashCode

    name = res.group(1)
    peakName = re.sub('[!@#$?]', '', name)
    length = res.group(2)
    geoHashCodeLength = int(length)
    code = res.group(3)
    if not len(code) == geoHashCodeLength:
        return False
    geoHashCode = code
    return True


def CheckString(data):
    if not ParseInput(data):
        print("Nothing found!")
    else:
        print("Coordinates found! {} -> {}".format(peakName, geoHashCode))

while True:
    command = input()
    if command == "Last note":
        break
    CheckString(command)
