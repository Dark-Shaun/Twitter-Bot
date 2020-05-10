from textblob import TextBlob
import re
import tweepy
import csv
from access_grant import *
from polarity import *
from timeline import *
access,api=api_1()
def search():
	name_1=input("Enter the Name:")#For e.g.=Donald Trump
	hometimeline_tweet=api.search(q=name_1,count=20)
	#Main
	b=0
	c=0
	a=0
	k=[]
	m=[]
	p=[]
	n=[]
	neu=[]
	for tweet in hometimeline_tweet:
		k.append(tweet.text)
		m.append(tweet.id)
#print("Positive Sentence:")
	for i in range(0,len(k)):
		text=k[i]
		polarity=sentiment(text)
		if polarity>0:
			try:
				api.create_favorite(m[i])
				api.retweet(m[i])
				#text=re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",text)
				#print(text)
				p.append(text)
				a=a+1
			except:
				continue
		elif polarity<0:#Negative Tweet
			#text=re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",text)
			#print(text)
			neu.append(text)
			c=c+1
		else:
			#text=re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",text)
			#print(text)
			n.append(text)
			b=b+1

	print("Positive Tweet:{}%".format(round((len(p)/len(k))*100)))
	print("Neutral Tweet:{}%".format(round((len(neu)/len(k))*100)))
	print("Negative Tweet:{}%".format(round((len(n)/len(k))*100)))
	print("\n")
	print("--------------------------------------------------------------------------------------------")
	print("Positive Tweet:")
	for i in range(0,len(p)):
		print(p[i])
	print("--------------------------------------------------------------------------------------------")
	print("Negative Tweet:")
	for i in range(0,len(n)):
		print(n[i])
	print("--------------------------------------------------------------------------------------------")
	print("Neutral Tweet:")
	for i in range(0,len(neu)):
		print(neu[i])
	print("--------------------------------------------------------------------------------------------")

	