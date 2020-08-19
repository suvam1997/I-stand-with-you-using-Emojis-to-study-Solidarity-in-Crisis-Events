from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json  
import twitterCredentials
import tweepy
import csv
 
# # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(twitterCredentials.CONSUMER_KEY, twitterCredentials.CONSUMER_SECRET)
        auth.set_access_token(twitterCredentials.ACCESS_TOKEN, twitterCredentials.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list, languages = ["en"], stall_warnings = True, is_async = True)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(json.loads(data)['text'])
            with open(self.fetched_tweets_filename, 'a', newline='') as tf:
                theWriter = csv.writer(tf)
                theWriter.writerow([json.loads(data)['text']])
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status_code):
        if status_code == 420:
            return False

 
if __name__ == '__main__':
 
    # Authenticate using config.py and connect to Twitter Streaming API.
    hash_tag_list = ['#AyodhyaVerdict','#AYODHYAVERDICT','#BabriMasjid','#AyodhyaCase','#AyodhyaHearing']
    fetched_tweets_filename = "tweets.csv"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
