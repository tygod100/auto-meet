from webbrowser import open_new_tab
import time

#open_new_tab("https://docs.python.org/2/library/webbrowser.html")

meets = list()
working = True # to check if anything is wong

weekdays = ["monday", "tuesday", "wednesday", 'thursday', 'friday', 'saturday', 'sunday'] #days in order
setdays = [0,1,2,3,4,5,6] # days that will be used, defalst all


try:
    f = open("meetings.txt", "r")
    meets = list(f.readlines())
    #print(meets)
    f.close()
except:
    print("an error occurred when reading meetings.txt, does it exist?")
    working = False

try: # to check for proper syntax
    for x in range(len(meets)):
        checky = meets[x].split()
        if not (len(checky) <= 0 or checky[0].lower() == "setday"):
            int(checky[1])
            int(checky[0])
except:
    print("an error occurred when reading meetings.txt, is the syntax wrong?")
    working = False
    
#time.sleep(2.4)# delays be 2.4 Seconds
if working:print("keep this window open for it to work, if you change your meetings.txt file you will need to reopen this to update.")
else: input("please fix the errors then try again")
while working:
    time.sleep(30)# delay for each check
    localtimer = time.localtime(time.time())# get time
    for x in range(len(meets)):
        data = meets[x].split() #.lower()
        if len(data) <= 0: # when emty skip
            1 + 1
        elif data[0].lower() == "setday": # when stert with setdays set days
            setdays = list() # reset set day list
            for i in range(len(data)):
                if data[i] in weekdays:
                    setdays.append(weekdays.index(data[i]))
                
        elif (int(localtimer.tm_hour+ localtimer.tm_isdst) == int(data[0]) and int(localtimer.tm_min) == int(data[1]) and (localtimer.tm_wday in setdays)):
            open_new_tab(data[2])
    #print(localtimer)

#git push -u origin main