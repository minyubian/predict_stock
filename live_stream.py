import tweepy
import sys
import os
import codecs

CONSUMER_KEY        = ""
CONSUMER_SECRET     = ""
ACCESS_TOKEN        = ""
ACCESS_TOKEN_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

f = codecs.open("C:\\Users\\file_name.txt",  'w', encoding = "utf-8")

class BasicTwitterListener(tweepy.StreamListener):
    def set_max_tweets(self, n):
        self.max_tweets = n

    def on_status(self, status):
        try:
            if self.max_tweets > 0:
                print status.text
                print >> "Tweet Text:", status.text

                self.max_tweets -=1

            elif self.max_tweets ==0:
                f.close()
                print "All Tweets Collected"
                return False

        except Exception, e:
             print e
             print >> sys.stderr, 'Exception when reading from stream:',
             pass

    def on_error(self, status_code):
         print >> sys.stderr, 'Encountered error with status code:', status_code
         return True

    def on_timeout(self):
         print >> sys.stderr, 'Timeout'
         return False

listener = BasicTwitterListener()
listener.set_max_tweets(10)

live_stream = tweepy.streaming.Stream(auth, listener)

keywords = ["tesco"]

live_stream.filter(track=keywords, follow = None)
    
