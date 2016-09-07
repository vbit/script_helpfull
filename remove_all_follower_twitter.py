import tweepy

__author__ = 'vbit'

'''
This script will remove all the followers from your twitter account. For that first it will block user one by one and
then unblock them. If you are following your followers, you won't be subscribed to them anymore once you run this job.
Rub this script carefully.

get id of username is http://gettwitterid.com/

Install tweepy module using pip. To install tweepy run below command in your terminal.
sudo pip install tweepy

Please replace consumer_key and consumer_secret. Visit https://apps.twitter.com to get your consumer_key and
consumer_secret.

Once you generate consumer key create an access token from same twitter page. Replace access_token and
access_token_secret with provided values. Then run the script.
'''


consumer_key = '<consumer_key>'
consumer_secret = '<consumer_secret>'
access_token = '<access_token>'
access_token_secret = '<access_token_secret>'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user_twitter = api.me()

followers_list = api.followers_ids(user_twitter.id)

total_followers = len(followers_list)

# ignone_user_list = {123, 12345} #used is number id user
ignone_user_list = {}

counter = 0

for user in followers_list:
	counter = counter + 1
	if user in ignone_user_list:
		print("%s/%s : %s was ignored" %(counter, total_followers, user))
		continue

	api.create_block(user)
	api.destroy_block(user)
	print("%s/%s : %s was removed" %(counter,total_followers,user))
