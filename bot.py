import praw;

reddit = praw.Reddit(
    user_agent="KiAdiMundiBot by u/DarthEggo1",
    client_id="0XmospxqKil_CVVajzJF6A",
    client_secret="XNTVkAXJ1tlXEuLa__Dy1vohc0gTDg",
    username="Ki-Adi-MundiBot",
    password="droidattackwookies",
)
import time

greylist = ["Ki-Adi-MundiBot", "Ahsoka_Tano_Bot", "Anakin_Skywalker_Bot", "BadBatchBot", "Battle-Droid-Bot", "Captain_Rex_Bot", "GeneralGrievous-Bot", "L17-Bot", "Maul_Bot", "Padme-Bot", "Qui-Gon_Jinn_Bot", "clone_trooper_bot", "jarjar_bot", "The-Guild"]
subreddit = reddit.subreddit("botmakers_guild")
KEYWORDS = ["emergency powers","supreme chancellor" "wookies", "dooku", "maul" "young", "!ignoremundi", "66", "luck", "chance", "ow", "die", "grievous"]
word1 = ["supreme chancellor", "emergency powers"]
word2 = ["wookies"]
word3 = ["dooku"]
word4 = ["maul"]
word5 = ["young"]
word6 = ["66"]
word7 = ["luck", "chance"]
word8 = ["ow"]
word9 = ["die"]
word10 = ["grievous"]
ignore = ["!ignoremundi"]


blockMessage = "We're sorry our bots were unsatisfactory. If you have the time, could you message this bot and tell us why you want to ignore the bot? Our primary goal is to have our bots be useful and fun for the good members of r/prequelmemes, so we will listen to any suggestions"


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
				comment.reply("Noo! Shaak Ti!")
				print(comment.body)
			elif any(k.lower() in comment.body.lower() for k in word9):
				comment.reply("Our predicament is dire, but do not despair. For we are Jedi!")
				print(comment.body)
			elif any(k.lower() in comment.body.lower() for k in word10):
				comment.reply("We must try padawan!")
				print(comment.body)
			elif any(k.lower() in comment.body.lower() for k in ignore):
				blockMessage(comment.author.name)			
				print("sadly," + comment.author.name + " has decided to ignore this bot")
				greylist.append(comment.author)	
			time.sleep(300)
		else:
			print("failed. reason: already replied to comment")
	else: 
		print("failed. reason: commented user " + comment.author.name + " is greylisted...")

			
		
def checkforgreylist(comment):
	b = 0
	for p in greylist:
		if(comment.author == p):
			b = 1
	return b
	
def checkforrepeat(comment):
	c = 0
	for reply in comment.replies:
		if reply.author == "Ki-Adi-MundiBot":
			c = 1

	return c


print("init")

while 1 == 1:
	for submission in subreddit.stream.submissions():
			print("Step 1: checking submission")
			submission.comments.replace_more(limit=0)
			for comment in submission.comments:
						checkReply(comment)
						scanReplies(comment)
					
			
def blockMessage(s):
	reddit.redditor(s).message("Our Apologies","We're sorry our bots were unsatisfactory. If you have the time, could you message this bot and tell us why you want to ignore the bot? Our primary goal is to have our bots be useful and fun for the good members of r/prequelmemes, so we will listen to any suggestions")
				
	

					

