import praw
import time
import random

reddit = praw.Reddit(
    user_agent="KiAdiMundiBot by u/DarthEggo1",
    client_id="0XmospxqKil_CVVajzJF6A",
    client_secret="XNTVkAXJ1tlXEuLa__Dy1vohc0gTDg",
    username="Ki-Adi-MundiBot",
    password="droidattackwookies",
)


blacklist = ["Ki-Adi-MundiBot"]
greylist = ["Sheev-Palpatine-Bot","Ahsoka_Tano_Bot", "Anakin_Skywalker_Bot", "BadBatchBot", "Battle-Droid-Bot", "Captain_Rex_Bot", "GeneralGrievous-Bot", "L17-Bot", "Maul_Bot", "Padme-Bot", "Qui-Gon_Jinn_Bot", "clone_trooper_bot", "jarjar_bot", "The-Guild"]
subreddit = reddit.subreddit("PrequelMemes")
KEYWORDS = ["emergency powers","supreme chancellor" "wookies", "dooku", "maul" "young", "!ignoremundi", "66", "luck", "chance", "ow", "die", "grievous"]
word1 = ["supreme chancellor", "emergency powers"]
word2 = ["wookies"]
word3 = ["dooku"]
word4 = ["maul"]
word5 = ["young"]
word6 = ["snow"]
word7 = ["luck", "chance"]
word8 = ["ouch"]
word9 = ["die"]
word10 = ["grievous"]
ignore = ["!ignore"]

def scanReplies(comment):	
	for reply in comment.replies:
		checkReply(reply)
		scanReplies(reply)
				
def checkReply(comment):
		if any(k.lower() in comment.body.lower() for k in KEYWORDS):
			print("Step 2: Found a keyword!")
			reply(comment)
def reply(comment):
	print("Checking for repeated comment and/or greylist ")
	check = checkforrepeat(comment)
	check2 = checkforgreylist(comment)
	if check2 == 0:
		if check == 0:
			print("passed!")
			if any(k.lower() in comment.body.lower() for k in word1):
				comment.reply("If he does not give up his emergency powers after the destruction of Grievous, then he should be removed from office")
				print(comment.body)
			elif any(k.lower() in comment.body.lower() for k in word2):
				comment.reply("But what about the droid attack on the Wookies?")
				print(comment.body)
			elif any(k.lower() in comment.body.lower() for k in word3):
				comment.reply("He is a political idealist, not a murderer.")
				print(comment.body)
			elif any(k.lower() in comment.body.lower() for k in word4):
				comment.reply("Impossible! The Sith are extinct! They have been for nearly a millenium.")
				print(comment.body)
			elif any(k.lower() in comment.body.lower() for k in word5):
				comment.reply("Your thoughts dwell on your mother?")
				print(comment.body)
			elif any(k.lower() in comment.body.lower() for k in word6):
				comment.reply("*dies in snow*")
				print(comment.body)
			elif any(k.lower() in comment.body.lower() for k in word7):
				comment.reply("There is no such thing as luck")
				print(comment.body)
			elif any(k.lower() in comment.body.lower() for k in word8):
				comment.reply("Noo! " + comment.author.name + "!")
				print(comment.body)
			elif any(k.lower() in comment.body.lower() for k in word9):
				comment.reply("Our predicament is dire, but do not despair. For we are Jedi!")
				print(comment.body)
			elif any(k.lower() in comment.body.lower() for k in word10):
				comment.reply("We must try padawan " + comment.author.name + "!")
				print(comment.body)
			time.sleep(60)
		else:
			print("failed. reason: already replied to comment")
	else:
		print("failed. reason: commented user " + comment.author.name + " is greylisted...")

def ignoreCheck(comment):
    if any(k.lower() in comment.body.lower() for k in ignore):
        if comment.parent == "Ki-Adi-MundiBot":
            print("Sadly, " + comment.author.name + " has decided to no longer use our bot's services")
            blockMessage(comment.author.name)
            blacklist.append(comment.author.name)

def checkforgreylist(comment):
    b = 0
    for p in greylist:
        if comment.author.name == p:
            if random.randrange(0,10) == 0:
                return 0
            else:
                return 1
    for d in blacklist:
        if comment.author.name == d:
            return 1
    return 0

	
def checkforrepeat(comment):
	c = 0
	for reply in comment.replies:
		if reply.author.name == "Ki-Adi-MundiBot":
			c = 1

	return c


print("init")

while 1 == 1:
    print("while loop restarting")
    
    for c in reddit.subreddit("PrequelMemes").stream.comments(skip_existing=True):
        print("Step 1: checking submission")
        checkReply(c)
        scanReplies(c)
					
			
def blockMessage(s):
	reddit.redditor(s).message("Our Apologies","We're sorry our bots were unsatisfactory. If you have the time, could you message this bot and tell us why you want to ignore the bot? Our primary goal is to have our bots be useful and fun for the good members of r/prequelmemes, so we will listen to any suggestions")
				
	


					

