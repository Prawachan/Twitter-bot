import tweepy
import random
import json
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("your auth key",
    "your second auth key")
auth.set_access_token("your token",
    "yor token")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


# Authenticate to twitter
auth = tweepy.OAuthHandler("your auth key",
                           "your second auth key")
auth.set_access_token("your token", "your second token")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

#get the user details
user = api.get_user("user_name")
print("User details:")
print(user.name)
print(user.description)
print(user.location)

#optional
print("last 20 followers:")
for follower in user.followers():
    print(follower.name)

# for tweet in api.search(q="your_idea", lang="en", rpp=10):
    # print(f"{tweet.user.name}:{tweet.text}")

#trends_result = api.trends_place(1)
#for trend in trends_result[0]["trends"]:
    #print(trend["name"])

#for tweet in tweepy.Cursor(api.home_timeline).items(5):
    #print(f"{tweet.user.name} said: {tweet.text}")

twt = api.search("your query", result_type="new", count=5)

time = api.user_timeline('your_user_name')

#reply tweet
for s in twt:
    print(s.id)
    sn = s.user.screen_name

    m = "@%s " % sn + "Your reply "

    api.update_status(status=m, in_reply_to_status_id=s.id)
    
print("Done!!!")