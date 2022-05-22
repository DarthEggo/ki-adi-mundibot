import praw
import time
import random

reddit = praw.Reddit(
    user_agent="MaceWinduBot by u/DarthEggo1",
    client_id="CENSORED",
    client_secret="CENSORED",
    username="Mace-Windu-Bot",
    password="CENSORED
)
#The triggers of other bots on the subreddit
otherTriggers = [
["ahsoka", "tano"],
["emergency powers","supreme chancellor", "wookiee", "wookie", "count dooku", "darth maul" "young anakin", "!ignore", "snow", "luck","ouch", "too strong", "we can't"],
['padme', 'padmé', 'amidala', 'federation', "love won't save you, padme. only my new powers can do that.",'are you an angel?', 'liberty', 'military transport'],
['Qui-Gon', 'Qui Gon', 'bigger fish', 'credits will do', 'i spake', 'what are midi-chlorians', 'what are midichlorians', 'the queen will not approve.', 'one of us? what do you mean?', 'i have a bad feeling about this', 'they live inside of me?', 'negotiations were short', 'gamble', 'information', ' rain'],
['gonk', 'g o n k", "bonk', 'gonk can you program', 'stonk', 'gond'],
['for the republic', 'nice shooting', 'now you got it', "we're gaining on em", 'were gaining on em', 'keep up the assault', 'just Like the simulations', 'for the chancellor', 'no one messes with the 501st', 'bomb', 'explosive', 'explosion', 'explode', 'disarm', 'warhead', 'nuke', 'demolitions team', 'demolitions expert', 'clone', 'trooper', '501st', 'order 66', 'order sixty six', 'order sixty-six', 'order 69', 'order sixty nine', 'order sixty-nine', 'the creeps', 'creeped out', 'give me the creeps', 'creep me out', 'creeps me out', 'red red green', 'red green red', ' egg', 'egg ', ' eggs', 'eggs ']
]
blacklist = ["Mace-Windu-Bot", "CENSORED"] #Censored for safety of users who blocked the bot
greylist = ["Sheev-Palpatine-Bot","Ahsoka_Tano_Bot", "Anakin_Skywalker_Bot", "BadBatchBot", "Battle-Droid-Bot", "Captain_Rex_Bot", "GeneralGrievous-Bot", "L17-Bot", "Maul_Bot", "Padme-Bot", "Qui-Gon_Jinn_Bot", "clone_trooper_bot", "jarjar_bot", "The-Guild"]
subreddit = reddit.subreddit("PrequelMemes")
KEYWORDS = ["!ignore", "window", "separatists", "CIS", "trapped", "sith lord", "chancellor", "darth maul", "not the jedi way", "treason", "appointed", "i am the senate", "unfair"]

ignore = ["!ignore"];
word1 = ["separatists", "CIS"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
word2 = ["trapped"]
word3 = ["sith lord"]
word4 = ["chancellor"]
word5 = ["darth maul"]
word6 = ["treason"]
word7 = ["not the jedi way"]
word8 = ["appointed"]
word9 = ["i am the senate"]
word10 = ["unfair"]
word11 = ["window"]


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
    if check == 0:
        try:
            print("passed!")
            check3 = ignoreCheck(comment)
            if check3 == 1:
                print("ignore!")
            elif any(k.lower() in comment.body.lower() for k in word1):
                comment.reply("I have dismantled and destroyed over 100,000 of you type one battle droids")
                print(comment.body)
            elif any(k.lower() in comment.body.lower() for k in word2):
                comment.reply("We will not be hostages to be bartered, Dooku!")
                print(comment.body)
            elif any(k.lower() in comment.body.lower() for k in word3):
                comment.reply("A SITH LAWD?!?!")
                print(comment.body)
            elif any(k.lower() in comment.body.lower() for k in word4):
                comment.reply("In the name of the galatic senate of the republic, you're under arrest chancellor!")           
                print(comment.body)
            elif any(k.lower() in comment.body.lower() for k in word5):
                comment.reply("But which was destroyed? The master, or the apprentice?")
                print(comment.body)
            elif any(k.lower() in comment.body.lower() for k in word6):
                comment.reply("Not. Yet.")
            elif any(k.lower() in comment.body.lower() for k in word7):
                comment.reply("He has control of the senate *and* the courts! He's too dangerous to be left alive!")
            elif any(k.lower() in comment.body.lower() for k in word8):
                comment.reply("You are on this council, but we do not grant you the rank of master.")
            elif any(k.lower() in comment.body.lower() for k in word9):
                comment.reply("The senate will decide your fate!")
            elif any(k.lower() in comment.body.lower() for k in word10):
                comment.reply("Take a seat young " + comment.author.name + "!")
                print(comment.body)
            elif any(k.lower() in comment.body.lower() for k in word11):
                comment.reply("*gets thrown out the windu*")
                print(comment.body)
            time.sleep(300)
        except:
            print("error replying to comment")
    else:
        print("failed. reason: commented user " + comment.author.name + " is greylisted...")

def ignoreCheck(comment):
    if any(k.lower() in comment.body.lower() for k in ignore):
        print("here")
        a = reddit.comment(id=comment.parent_id)
        if a.author == "Mace-Windu-Bot":
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
        print(trigList)
        if any(trig in comment.body.lower() for trig in trigList):
            print("Detected other trigger")
            l = 1
            l += 1
    if l == 1:
        if random.randint(1, p) == 1:
            print("rng success!")
            return 0
    return l


print("init")

while 1 == 1:
    print("while loop restarting")
    try:
        for c in reddit.subreddit("PrequelMemes+botmakers_guild").stream.comments(skip_existing=True):
            print("Step 1: checking submission")
            checkReply(c)
            scanReplies(c)
    except Exception as e:
        print(e)
					
			
def blockMessage(s):
	reddit.redditor(s).message("Our Apologies","We're sorry our bots were unsatisfactory. If you have the time, could you message this bot and tell us why you want to ignore the bot? Our primary goal is to have our bots be useful and fun for the good members of r/prequelmemes, so we will listen to any suggestions")
				
	

	   
