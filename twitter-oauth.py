from requests_oauthlib import OAuth1Session
import secret_data
import json

consumer_key = secret_data.CONSUMER_KEY
consumer_secret = secret_data.CONSUMER_SECRET
access_token = secret_data.ACCESS_KEY
access_secret = secret_data.ACCESS_SECRET

#Code for OAuth starts
url = 'https://api.twitter.com/1.1/account/settings.json'
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret, resource_owner_key=access_token, resource_owner_secret=access_secret)
#requests.get(url, auth=oauth)


protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
response = oauth.get(protected_url, params=params)

res = json.loads(response.text)
result = res['statuses']
'''
tweet = json.dumps(res,indent=4)
fw = open('CACHE',"w")
fw.write(tweet)
fw.close()
'''

for l in result:
	if l['entities']["user_mentions"] != []:
		print(l['entities']["user_mentions"][0]['name']+": ")
		print(l['text'])
		print('------------')
