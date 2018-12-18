# CMSC 491-01, Spring 2018
# Dr. George Ray
# Project: Accessing and Mining Social Media
# Anna Aladiev       
#####################################################################################################################################
# This program analyzes the Twitter hashtag #Google.
# It first connects to Twitter and retrieves 50 tweets from the company hashtag, then displays a well formatted report of the posts.
# For each tweet, the report dislays its user, text, retweet count, lexical analysis, and sentiment analysis.
#####################################################################################################################################

import twitter
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment
from prettytable import PrettyTable 		

def removeUnicode(text):
        asciiText = ""
        for char in text:
            if (ord(char) < 128):
                asciiText = asciiText + char
        return asciiText

# CONNECT TO TWITTER 
# FILL IN TWITTER TEST CREDENTIALS IN PLACE OF EMPTY STRING VALUES
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

tw = twitter.Twitter(auth=auth)

# RETRIEVE 50 #GOOGLE TWEETS
q = ['#Google']
count = 100
tweets = tw.search.tweets(q = q, count = count, lang = 'en')
users = []
retweets = []
texts = []
sentiments = []

table = PrettyTable(field_names = ["#", "User", "Tweet", "Retweet Count", "Lexical Analysis", "Sentiment Analysis"])

# LOOP THROUGH ENTITIES
listCounter = 0
for status in tweets['statuses']:
	if listCounter < 50:
		texts.append(removeUnicode(status["text"]))													# RETRIEVE TWEET
		users.append(tweets["statuses"][listCounter]["user"]["screen_name"].encode('utf-8'))		# RETRIEVE USER
		retweets.append(tweets["statuses"][listCounter]["retweet_count"])							# RETRIEVE RETWEET COUNT
		vs = vaderSentiment(status["text"].encode('utf-8'))											# CALCULATE SENTIMENT ANALYSIS
		sentiments.append(str(vs['compound']))	
		listCounter = listCounter + 1

# CALCULATE LEXICAL DIVERSITY
tableCounter = 0
for text in texts:
	words = []
	string = ""
	for w in text.split():
		words.append(w)
		string += w + " "
	lexicals = 1.0*len(set(words))/len(words)														# CALCULATE LEXICAL DIVERSITY
	table.add_row([tableCounter + 1, users[tableCounter], string, retweets[tableCounter], lexicals, sentiments[tableCounter]])		
	tableCounter = tableCounter + 1

# FOR EACH TWEET: DISPLAY USER, TWEET, RETWEET COUNT, LEXICAL DIVERSITY, SENTIMENT ANALYSIS
print(table)


