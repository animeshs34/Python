import re

def timeConversion(s):
    element = list(re.findall("(\d{2}):(\d{2}):(\d{2})(AM|PM)",s)[0])
    if element[-1] == "PM":
        if element[0] == "12":
            pass
        else:
            element[0] = str(int(element[0])+ 12)
    if element[-1] == "AM":
        if element[0] == "12":
            element[0] = "00"
        else:
            pass
    
    print(":".join(element[0:-1]))


timeConversion("07:05:45PM")