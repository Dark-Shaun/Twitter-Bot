from textblob import TextBlob
import re
import tweepy
import csv
from access_grant import *
from polarity import *
access,api=api_1()

def timeline():
	name_1=input("Enter the user name:")#Prefer using the username of the particular person for e.g,'iamsrk'/'shahidkapoor'/'realDonaldTrump'
	hometimeline_tweet=api.user_timeline(name_1,count=30)
	#Main
	b=0
	c=0
	a=0
	k=[]
	m=[]
	for i in range(0,len(k)):
		text=k[i]
		polarity=sentiment(text)
		if polarity>0:#Positive Tweet
			try:
				api.create_favorite(m[i])
				api.retweet(m[i])
				#text=re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",text)
				#print(text)
				a=a+1
			except:
				continue
		elif polarity<0:#Negative Tweet
			#text=re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",text)
			#print(text)
			c=c+1
		else:#Neutral Tweet
			#text=re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",text)
			#print(text)
			b=b+1
		if a>b>c:
			return print("Positive Timeline")
		elif a<b>c:
			return print("Neutral Timeline")
		else:
			return print("Negative Timeline")