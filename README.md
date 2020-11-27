# auto-meet
This will automatically open zoom, google meed, or whatever it is you need for you meetings. 


# how to use 

## set up

1. Downloded the **exe** file. The current release can be found to the right of the main page, you should find it under the **"Assets"** of the [latest release](https://github.com/tygod100/auto-meet/releases).
2. ones you've downloded the **exe** file, puting in a easy to reach folder then create a new text document **(.txt)** in the same folder.
3. name the new text file **_"meetings.txt"_**, this is case senstive so make sure it's all lower case.
4. read below on how to set days and meetings, then run the **exe** file and leave the window open

## setting a meetting


To set a meetting, you'll have to write a little code. I've made this farly simpal to use.

this is the syntax of a meetting:
> [hour] [minute] [url]


The **"[hour]"** part is where you put the hour of the meeting, this uses a 24-hour clock so **5** will be **5am** and **17** will be **5pm**
  
The **"[minute]"** part is of course where you put the minute of the meeting
  
The **"[url]"** part is  where you put the link that will send you to the meeting, likely copy and pasting it. You can use it for something else too if you wish.
  
### examples
> 5 55 https://en.wikipedia.org/wiki/Meeting

_this will open (https://en.wikipedia.org/wiki/Meeting) on 5:55 am_


> 14 23 https://en.wikipedia.org/wiki/24-hour_clock

_this will open (https://en.wikipedia.org/wiki/24-hour_clock) on 2:23 pm_

After this if verything is correct just run the "auto meet.py" file and leave the window open.

## setting week days
Meny meeting only occur on certain days of the week. You'll need to write a little more code

this is the syntax of a meetting:
> setday [days(list)]

The **"setday"** part will _stay_ as it is, this is to tell the program what your trying to do

The **"[days(list)]"** part is where you'll put all the days of the week you want and separate them by a space, this will make all meething set after this line only open on the set days and will be over witten the next time **setday** is called. _Make sure you spell them correctly._ **by default meeting will open on every day**
  
### examples
>setday wednesday thursday

> 5 55 https://en.wikipedia.org/wiki/Meeting

>setday monday

> 14 23 https://en.wikipedia.org/wiki/24-hour_clock

this will open the first link on 5:55am only on wednesday and thursday and will only open the second on Monday


#### if you need help you can ask, I don't actually check very often but it worth a shot. 

# to do 
* maybe improve instructions on read me
* make use easyer
* make GUI
* check back on day light saving time, just in case
* find feed back or testers



# how to use (old)

## set up
In the same folder as the **"auto meet.py"** file (or the .exe when I get to making that), make a **"meetings.txt"** file. _Note that is is **case sestive**; the file name **"Meetings.txt"** won't work but **"meetings.txt"** will, this is because the former had an uppercase._

## making meetings
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

this will open the first link on 5:55am only on wednesday and thursday and will only open the second on Monday

