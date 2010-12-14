import sentParser
import tweetScorer
import tweetCleaner
import sys
import re
import math
import time
import pickle


def tweetParser(tweets, parser):
  pdict = parser
  tweetWordDict = {}
  num_tweets = 0
  total_score = 0
  num_words = 0
  neg_tweets = 0
  pos_tweets = 0

  for tweet_w_list in tweets:
    num_tweets += 1
    total_tweet_score = 0
    for word in tweet_w_list:
      num_words+=1
      word_score = pdict.get(word,0)
      total_tweet_score += word_score
      tweet_dict = {}
      for w in tweet_w_list:
        tweet_dict[w] = tweet_dict.get(w,0) + 1
    for word in tweet_w_list:
      wc = tweet_dict[word]
      if wc != 1:
        first = False
      else:
        first = True
        tweet_dict[word] = wc - 1
      if total_tweet_score == 0:
        continue
      wordEntry = tweetWordDict.get(word, {'count':0,'sent':0,'tweets':0})
      wordEntry['count'] += 1
      wordEntry['sent'] += total_tweet_score
      if first:
        wordEntry['tweets'] += 1
      tweetWordDict[word] = wordEntry
  return tweetWordDict, num_tweets

def improvePD(twd, pd, num_tweets, thresh, thresh2, neg_bool):                  
  new_sent_dict = {}
  sent_dict = {}
  for word in twd:
    times = twd[word]['count']
    total_sent = twd[word]['sent']
    tweets = twd[word]['tweets']
    sent_val = (float(total_sent)/times)
    twt_pct = (float(tweets)/num_tweets)
    if twt_pct > thresh2 and twt_pct < .5:
      sent_dict[word]=sent_val
    #end loop

  l = sent_dict.items()
  l.sort(key=lambda s: s[1])
  if neg_bool:
    l.reverse()
  st = l[int(len(l)-(thresh*len(l))):]
  for item in st:
    new_sent_dict[item[0]] = item[1]
  
  sent_sum = sum(new_sent_dict.values())
  avg_sent = float(sent_sum)/len(new_sent_dict)
  for word in new_sent_dict:
    new_sent_dict[word] = (new_sent_dict[word]/float(abs(avg_sent)))

  return new_sent_dict

def combine(p_pd, n_pd):
  pd = p_pd

  for key in n_pd:
    val = pd.get(key,0)
    val += n_pd[key]
    pd[key] = val
  rem = []
  for key in pd:
    if abs(pd[key]) < 1:
      rem.append(key)
  for key in rem:
    pd.pop(key)
  return pd
        
def main(top_pct,pct_tweets,iterations):    
  print top_pct, pct_tweets, iterations
  p_pd, n_pd = sentParser.createSimpDict('sentmtListsm.txt',2)
  #pd = sentParser.createParseDict()
  #p_pd, n_pd = sentParser.createSimpDict('testsent.txt',2)
  
  tweets = tweetCleaner.cleanTweets('/scratch/nschult1/prunedTweets.txt')
  gs_test_tweets = tweets[1:50]
  train_tweets = tweets[50:]

  for i in range(iterations):

    p_twd , p_num_tweets = tweetParser(train_tweets,p_pd)
    n_twd , n_num_tweets = tweetParser(train_tweets,n_pd)

    thresh = top_pct
    thresh2 = pct_tweets

    p_pd = improvePD(p_twd,p_pd,p_num_tweets,thresh,thresh2,False)
    n_pd = improvePD(n_twd,n_pd,n_num_tweets,thresh,thresh2,True)

    pd = combine(p_pd, n_pd)
  
  f = open('newparser.txt','w')
  for key in pd:
    f.write('%s %f\n' %(key,pd[key]))
  f.close()

  total_score = tweetScorer.scorer(gs_test_tweets,pd,sentParser.createEDict(), True, True)







if __name__ == '__main__': main(float(sys.argv[1]), float(sys.argv[2]),int(sys.argv[3]))



    
