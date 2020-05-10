from textblob import TextBlob
import re
import tweepy
import csv
from access_grant import *
from polarity import *
from timeline import *
from search import *
access,api=api_1()
print(access)

print("1.Enter 1 if you want to analyze the Timeline of any User") 
print("2.Enter 2 if you want analyze Public Actions on Twitter towards the User")
options=int(input('Options:'))
if options==1:
	timeline=timeline()
elif options==2:
	search()
else:
	print("Wrong Option")


