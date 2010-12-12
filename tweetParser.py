import sentParser
import sys
import re


def tweetParser(filename, parser):
  f = open(filename,'r')
  pdict = parser
  tweetWordDict = {}
  numTweets = 0
  total_score = 0
  urlRE = re.compile('\shttp([^\s]*)')
  puncRE = re.compile(r'([^\w\s]+)\s+') 

  for tweet in f:
    numTweets += 1
    tweet = tweet.strip()
    m = puncRE.findall(tweet)
    patt_d = {}
    for patt in m:
      patt_d[patt] = 1
    for patt in patt_d:
      tweet = tweet.replace(patt, ' %s' %patt)
    tweet_w_list = tweet.split()
    total_tweet_score = 0

    for word in tweet_w_list:

      #if word == 'good':
        #for word in line:
          #print word , pdict.get(word,0)
      total_tweet_score += pdict.get(word.lower(),0)
    for word in tweet_w_list:
      word = word.rstrip('.')
      word = word.lower()
      wordEntry = tweetWordDict.get(word, {'count':0, 'total_sent':0})
      wordEntry['count'] += 1
      wordEntry['total_sent'] += total_tweet_score
      tweetWordDict[word] = wordEntry
    total_score += total_tweet_score
  return tweetWordDict, numTweets, total_score

def tweetParserNeg(filename, parser):
  f = open(filename,'r')
  pdict = parser
  tweetWordDict = {}
  numTweets = 0
  total_score = 0
  for line in f:
    numTweets += 1
    line = line.strip()
    line = line.split()
    negDict={}
    i=0
    total_tweet_score = 0
    for word in line:
      word = word.rstrip('.')
      negDict[i]=word
      #if word == 'good':
        #for word in line:
          #print word , pdict.get(word,0)
      if i>2:
        if negDict.get(i-2)=='not' or negDict.get(i-1)=='not':
          total_tweet_score-=pdict.get(word.lower(),0)
        else:
          total_tweet_score += pdict.get(word.lower(),0)
      else:
        total_tweet_score+=pdict.get(word.lower(),0)
      i+=1
    for word in line:
      word = word.rstrip('.')
      word = word.lower()
      wordEntry = tweetWordDict.get(word, {'count':0, 'total_sent':0})
      wordEntry['count'] += 1
      wordEntry['total_sent'] += total_tweet_score
      tweetWordDict[word] = wordEntry
    total_score += total_tweet_score
  return tweetWordDict, pdict, numTweets, total_score



def tweetParserNegE(filename, parser, enhancers):
  #Will this mess up sentiment values of words
  #Maybe make this just for scoring at the end
  f = open(filename,'r')
  goodemp=0
  bademp=0
  pdict = parser
  edict=enhancers
  tweetWordDict = {}
  numTweets = 0
  total_score = 0
  for line in f:
    numTweets += 1
    line = line.strip()
    line = line.split()
    lineDict={}
    i=0
    total_tweet_score = 0
    for word in line:
      word = word.rstrip('.')
      lineDict[i]=word
      #if word == 'good':
        #for word in line:
          #print word , pdict.get(word,0)
      if i>2:
        if lineDict.get(i-2)=='not' or lineDict.get(i-1)=='not':
          total_tweet_score-=pdict.get(word.lower(),0)
        else:
          if edict.has_key(lineDict.get(i-1)):
              weight=edict.get(lineDict.get(i-1))
              total_tweet_score+=weight*pdict.get(word.lower(),0)
              if total_tweet_score>0:
                goodemp+=1
              else:
                bademp+=1
          else:
              total_tweet_score += pdict.get(word.lower(),0)
      else:
        total_tweet_score+=pdict.get(word.lower(),0)
      i+=1
    for word in line:
      word = word.rstrip('.')
      word = word.lower()
      wordEntry = tweetWordDict.get(word, {'count':0, 'total_sent':0})
      wordEntry['count'] += 1
      wordEntry['total_sent'] += total_tweet_score
      tweetWordDict[word] = wordEntry
    total_score += total_tweet_score
  return tweetWordDict, pdict, numTweets, total_score




def improvePD(twd, pd, threshold, avg):
  size_pd = len(pd)
  for key in twd.keys():
    sent_val = 0.0
    #print twd[key]['count']
    if twd[key]['count'] != 0:
      sent_val = float(twd[key]['total_sent'])/(abs(avg) * float(twd[key]['count']))
    if abs(sent_val) > 1.5 and twd[key]['count'] > threshold:
      pd[key] = sent_val
      #print pd
  #print len(pd)
  return pd





def main(tweetRatio):
  pd = sentParser.createSimpDict('sentmtListsm.txt')

  #pd = sentParser.createSimpDict('sentmtListsm.txt')
  #enhancers=sentParser.createEDict()
  for i in range(1,6):
    twd, numTweets, total_score = tweetParser('/scratch/nschult1/prunedTweets.txt', pd)
    avg = (float(total_score)/float(numTweets))
    print numTweets, total_score, avg
    threshold = ((numTweets*tweetRatio))
    #print pd
    pd = improvePD(twd,pd,threshold, avg)
    #print pd
  f = open('newparser.txt','w')
  for key in pd:
    f.write('%s %f\n' %(key,pd[key]))
  f.close()


if __name__ == '__main__': main(float(sys.argv[1]))



    
