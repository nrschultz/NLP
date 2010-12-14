#!/usr/bin/env python
# vim: set fileencoding=< UTF-8 :

import re
import sys


def cleanTweets(fname):
  tweets = open(fname,'r')
  urlRE = re.compile(r'[\s]http[^\s]*')
  puncRE = re.compile(r'([^\w\s]+)\s+') 
  atRE = re.compile(r'@\S*')
  
  t=[]
  t2 = {}
  for tweet in tweets:
    #print tweet
    tweet = tweet.lower()
    for url in urlRE.findall(tweet):
      tweet = tweet.replace(url,'')
    for at in atRE.findall(tweet):
      tweet = tweet.replace(at,'')
    punc_pattern = {}
    for patt in puncRE.findall(tweet):
      punc_pattern[patt] = 1
    for patt in punc_pattern:
      tweet = tweet.replace(patt, ' %s' %patt)
    tweet_word_list = tweet.split()
    #print tweet_word_list
    twl = ' '.join(tweet_word_list)
    t2[twl] = 1
  for twt in t2:
    t.append(twt.split())

  return t
  
def main():
  cleanTweets('testtweets.txt')

if __name__ == '__main__': main()


