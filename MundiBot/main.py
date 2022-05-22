import praw
import time
import random

reddit = praw.Reddit(
    user_agent="KiAdiMundiBot by u/DarthEggo1",
    client_id="CENSORED",
    client_secret="CENSORED",
    username="Ki-Adi-MundiBot",
    password="CENSORED",
)

otherTriggers = [
["ahsoka", "tano"],
['separatists', 'battle droid', 'trapped', 'sith lord', 'chancellor, "darth maul', 'not the jedi way", "treason', 'master', 'senate', 'unfair'],
['padme', 'padmé', 'amidala', 'federation', "love won't save you, padme. only my new powers can do that.", 'are you an angel?', 'liberty', 'military transport'],
['Qui-Gon', 'Qui Gon', 'bigger fish', 'credits will do', 'i spake', 'what are midi-chlorians', 'what are midichlorians', 'the queen will not approve.', 'one of us? what do you mean?', 'i have a bad feeling about this', 'they live inside of me?', 'negotiations were short', 'gamble', 'information', ' rain'],
['gonk', 'g o n k", "bonk', 'gonk can you program', 'stonk', 'gond'],
['for the republic', 'nice shooting', 'now you got it', "we're gaining on em", 'were gaining on em', 'keep up the assault', 'just Like the simulations', 'for the chancellor', 'no one messes with the 501st', 'bomb', 'explosive', 'explosion', 'explode', 'disarm', 'warhead', 'nuke', 'demolitions team', 'demolitions expert', 'clone', 'trooper', '501st', 'order 66', 'order sixty six', 'order sixty-six', 'order 69', 'order sixty nine', 'order sixty-nine', 'the creeps', 'creeped out', 'give me the creeps', 'creep me out', 'creeps me out', 'red red green', 'red green red', ' egg', 'egg ', ' eggs', 'eggs ']
]
blacklist = ["Ki-Adi-MundiBot", "CENSORED"] #Censored for protection of users who chose to block this bot
greylist = ["Threepio_Bot", "Sheev-Palpatine-Bot","Ahsoka_Tano_Bot", "Anakin_Skywalker_Bot", "BadBatchBot", "Battle-Droid-Bot", "Captain_Rex_Bot", "GeneralGrievous-Bot", "L17-Bot", "Maul_Bot", "Padme-Bot", "Qui-Gon_Jinn_Bot", "clone_trooper_bot", "jarjar_bot", "The-Guild"]

KEYWORDS = ["emergency powers","supreme chancellor", "wookiee", "wookie", "count dooku", "darth maul" "the boy", "!ignore", "snow", "luck","grievous", "greivous", "too strong", "we can't"]
word1 = ["supreme chancellor", "emergency powers"]
word2 = ["wookiee"]
word2b = ["wookie"]
word3 = ["count dooku"]
word4 = ["darth maul"]
word5 = ["the boy"]
word6 = ["snow"]
word7 = ["luck"]
word8 = ["grievous", "greivous"]
word9 = ["too strong"]
word10 = ["we can't"]
ignore = ["!ignore"]

def scanReplies(comment):	
    for reply in comment.replies:
        try:
            checkReply(reply)
            scanReplies(reply)
        except Exception as e:
            print(e)
				
def checkReply(comment):
		if any(k.lower() in comment.body.lower() for k in KEYWORDS):
			print("Step 2: Found a keyword!")
			reply(comment)
def reply(comment):
    print("Checking for repeated comment and/or greylist ")
    check = checkforgreylist(comment)
    check1 = checkOtherTriggers(comment)
    if check1 == 0:
        if check == 0:
            try:
                print("passed!")
                check3 = ignoreCheck(comment)
                if check3 == 1:
                    print("ignore!")
                elif any(k.lower() in comment.body.lower() for k in word1):
                    comment.reply("If he does not give up his emergency powers after the destruction of Grievous, then he should be removed from office")
                    print(comment.body)
                elif any(k.lower() in comment.body.lower() for k in word2):
                    comment.reply("But what about the droid attack on the Wookiees?")
                    print(comment.body)
                elif any(k.lower() in comment.body.lower() for k in word2b):
                    comment.reply("But what about the droid attack on the Wookiees? Also it's spelled with a double e")
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
            except:
                print("error replying to comment")
        else:
            print("failed. reason: commented user " + comment.author.name + " is greylisted...")
    else:
        print("spam")
def ignoreCheck(comment):
    if any(k.lower() in comment.body.lower() for k in ignore):
        print("here")
        a = reddit.comment(id=comment.parent_id)
        if a.author == "Ki-Adi-MundiBot":
            reddit.redditor("DarthEggo1").message("ignore request", comment.author.name)
            print("Sadly, " + comment.author.name + " has decided to no longer use our bot's services")
            reddit.redditor(comment.author.name).message("Our Apologies","We're sorry our bots were unsatisfactory. If you have the time, could you message this bot and tell us why you want to ignore the bot? Our primary goal is to have our bots be useful and fun for the good members of r/prequelmemes, so we will listen to any suggestions")
            blacklist.append(comment.author.name)
            return 1
    return 0

def checkforgreylist(comment):
    b = 0
    for p in greylist:
        if comment.author.name == p:
            if random.randrange(0,10) == 0:
                print("passed greylist!")
                return 0
            else:
                return 1
    for d in blacklist:
        if comment.author.name == d:
            return 1
    return 0

	
def checkOtherTriggers(comment):
    l = 0
    p = 0 
    for trigList in otherTriggers:
        if any(trig in comment.body.lower() for trig in trigList):
            print("Detected other trigger")
            l = 1
            l += 1
    if l == 1:
        if random.randint(1, p) == 1:
            l = 0
    return l
	


print("init")

while 1 == 1:
    print("while loop restarting")
    try:
    for c in reddit.subreddit("PrequelMemes+botmakers_guild").stream.comments(skip_existing=True):
        print("Step 1: checking submission")
        checkReply(c)
        scanReplies(c)
    except:
        print("exception raised")
					
			
def blockMessage(s):
	reddit.redditor(s).message("Our Apologies","We're sorry our bots were unsatisfactory. If you have the time, could you message this bot and tell us why you want to ignore the bot? Our primary goal is to have our bots be useful and fun for the good members of r/prequelmemes, so we will listen to any suggestions")
				
	

	   
