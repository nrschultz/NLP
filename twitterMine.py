import tweepy
import time
def main():
    #f = open('/scratch/nschult1/tweets.txt','w')
    tweets = []
    for subject in ['iphone 4','evo 4g', 'windows phone']:
      tweets += tweepy.API().search(subject, rpp=100, lang='en')
    for tweet in tweets:
      write = False
      num_letter = 0
      tweet_list = list(tweet.text)
      for letter in tweet_list:
        if ord(letter) > 127:
          tweet_list[num_letter] = chr(127)
        num_letter += 1
      print ''.join(tweet_list)
    #f.close()
    #print 'saved'

main()

