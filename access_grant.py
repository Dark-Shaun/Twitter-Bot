import tweepy
def api_1():
	CONSUMER_KEY=''
	CONSUMER_SECRET=''
	ACCESS_KEY=''
	ACCESS_SECRET=''
	auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
	global api
	api=tweepy.API(auth)
	access='Access Granted'
	return access,api 