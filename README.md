# auto-meet
This will automatically open zoom, google meed, or whatever it is you need for you meetings. 

# how to use

## set up
In the same folder as the **"auto meet.py"** file (or the .exe when I get to making that), make a **"meetings.txt"** file. _Note that is is **case sestive**; the file name **"Meetings.txt"** won't work but **"meetings.txt"** will, this is because the former had an uppercase._

##making meetings
In put in every line in the txt file the data, this is in 3 parts each seprated by a space. The first part is the hour of the meeting, in the second part is the minute, and the third is the meeting's url. _Note that this uses a **24 hour** clock; **2 0** is **2-am** and **14 0** is **2-pm**._

### examples
> 5 55 https://en.wikipedia.org/wiki/Meeting

_this will open (https://en.wikipedia.org/wiki/Meeting) on 5:55 am_


> 14 23 https://en.wikipedia.org/wiki/24-hour_clock

_this will open (https://en.wikipedia.org/wiki/24-hour_clock) on 2:23 pm_

After this if verything is correct just run the "auto meet.py" file and leave the window open.

## seting week days

to set a week day make thr first word of a line "setday" then type the days that you want to use
this will make all meetings witten after it only open on those set days
_by default meeting will open on every day _



### examples
>setday wednesday thursday
> 5 55 https://en.wikipedia.org/wiki/Meeting
>setday monday
> 14 23 https://en.wikipedia.org/wiki/24-hour_clock

this will open the first link on 5:55am only on wednesday and thursday and will only open the second on monday

#to do
* maybe inprove read me
* make use easyer
* make GUI
* make exe
* might break in daylight saving time, figer out how it works

