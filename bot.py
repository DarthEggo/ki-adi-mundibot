import praw;



reddit = praw.Reddit(
    user_agent="KiAdiMundiBot by u/DarthEggo1",
    client_id="0XmospxqKil_CVVajzJF6A",
    client_secret="censored",
    username="Ki-Adi-MundiBot",
    password="censored",
)
import time

greylist = ["Ki-Adi-MundiBot", "Ahsoka_Tano_Bot", "Anakin_Skywalker_Bot", "BadBatchBot", "Battle-Droid-Bot", "Captain_Rex_Bot", "GeneralGrievous-Bot", "L17-Bot", "Maul_Bot", "Padme-Bot", "Qui-Gon_Jinn_Bot", "clone_trooper_bot", "jarjar_bot",]]
subreddit = reddit.subreddit("PrequelMemes")
KEYWORDS = ["palp", "wookies", "dooku", "maul" "young", "!ignoremundi"]
word1 = ["palp"]
word2 = ["wookies"]
word3 = ["dooku"]
word4 = ["maul"]
word5 = ["young"]
word6 = ["!ignoremundi"]

def scanReplies(comment):	
	for reply in comment.replies:
		checkReply(reply)
		scanReplies(reply)
				
def checkReply(comment):
		if any(k.lower() in comment.body.lower() for k in KEYWORDS):
			reply(comment)
def reply(comment):
	check = checkforrepeat(comment)
	print(check)
	if comment.author != "Ki-Adi-MundiBot":
		if check == 0:
			if any(k.lower() in comment.body.lower() for k in word1): 
				comment.reply("If he does not give up his emergency powers after the destruction of Grievous, then he should be removed from office")
				print(comment.body)
			if any(k.lower() in comment.body.lower() for k in word2):
				comment.reply("But what about the droid attack on the Wookies?")
				print(comment.body)
			if any(k.lower() in comment.body.lower() for k in word3):
				comment.reply("He is a political idealist, not a murderer.")
				print(comment.body)
			if any(k.lower() in comment.body.lower() for k in word4):
				comment.reply("Impossible! The Sith are extinct! They have been for nearly a millenium.")
				print(comment.body)
			if any(k.lower() in comment.body.lower() for k in word5):
				comment.reply("Your thoughts dwell on your mother?")
				print(comment.body)
			if any(k.lower() in comment.body.lower() for k in word6):
				reddit.redditor('dartheggo1').message(comment.author)
				greylist.append(comment.author)
			time.sleep(600)
			

			
		
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

for submission in subreddit.stream.submissions():
		
		
		for comment in submission.comments:	
					checkReply(comment)
					scanReplies(comment)
					
			
					
				
				

					

