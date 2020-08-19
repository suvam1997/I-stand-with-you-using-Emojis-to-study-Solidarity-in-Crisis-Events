import twitterCredentials
import tweepy
import csv

auth = tweepy.OAuthHandler(twitterCredentials.CONSUMER_KEY, twitterCredentials.CONSUMER_SECRET)
auth.set_access_token(twitterCredentials.ACCESS_TOKEN, twitterCredentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

searchTerm = ['AyodhyaVerdict','AYODHYAVERDICT','BabriMasjid','AyodhyaCase','AyodhyaHearing'] ##input("Enter Keyword/Tag to search about: ")
noOfSearchTerms = int(input("Enter how many tweets to search: "))

tweets = tweepy.Cursor(api.search, q=searchTerm, lang='en').items(noOfSearchTerms)

tweetFile = 'tweets.csv'
with open(tweetFile, 'w', newline='') as tf:
    theWriter = csv.writer(tf)
for tweet in tweets:
    print(tweet)
    theWriter.writerow([tweet.text])


 

