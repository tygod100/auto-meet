from webbrowser import open_new_tab
import time

#open_new_tab("https://docs.python.org/2/library/webbrowser.html")

meets = list()
working = True # to check if anything is wong

try:
    f = open("meetings.txt", "r")
    meets = list(f.readlines())
    #print(meets)
    f.close()
except:
    print("an error occurred when read meetings.txt, does it exist?")
    working = False

try: # to check for proper syntax
    for x in range(len(meets)):
        checky = meets[x].split()
        int(data[1])
        int(data[0])
except:
    print("an error occurred when read meetings.txt, is the syntax wrong?")
    working = False
    
#time.sleep(2.4)# delays be 2.4 Seconds
if working:print("keep this window open for it to work, if you change your meetings.txt file you will need to reopen this to update.")
else: input("please fix the errors then try again")
while working:
    time.sleep(30)# delay for each check
    localtimer = time.localtime(time.time())# get time
    for x in range(len(meets)):
        data = meets[x].split()
        if (int(localtimer.tm_hour) == int(data[0]) and int(localtimer.tm_min) == int(data[1])):
            open_new_tab(data[2])
    #print(localtimer)

#git push -u origin main