import tweepy
print("Onoma user:")
username = input()
#edw mpainoun ta api keys
auth = tweepy.OAuthHandler("INSERT KEYS", "INSERT KEYS")
auth.set_access_token("INSERT KEYS", "INSERT KEYS")
api = tweepy.API(auth)
timeline = api.user_timeline(screen_name=username,count=10,tweet_mode="extended",include_rts="false")
textonly_tweets = [tweet.full_text for tweet in timeline]
metatropi = ' '.join(textonly_tweets)
listamegala = list(metatropi.split(" "))
listamegala.sort(key=len, reverse=True)
listamikra = list(metatropi.split(" "))
listamikra.sort(key=len)
print(listamegala)
#bgazoyme ta links apo tin lista me tis megales lekseis
nealista = [x for x in listamegala if "https" not in x]

i=0 
print("5 megaliteres lekseis:")
while (i<5):
    print(nealista[i])
    i +=1
i=0
print("5 mikroteres lekseis:")
while (i<5):
    print(listamikra[i])
    i +=1