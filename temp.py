import sys

def convert(temp, typeTemp):
    if typeTemp.upper() == "C":
        return ((int(temp) * 1.8) +32), "F"
    elif typeTemp.upper() == "F":
        return ((int(temp) - 32) * 0.5555555555555556), "C"
    else:
        return "You have no entered a valid temperature type.\nUsage:\n Please enter the temperature followed by F or C.\n E.G. python temp.py 30 C"

def Main():
    if len(sys.argv) != 3:
        return "You have not entered enough arguments.\nUsage:\n Please enter the temperature followed by F or C.\n E.G. python temp.py 30 C"
    else:
        results = convert(sys.argv[1], sys.argv[2])
        print str(results[0]) + " " + results[1]

Main()
