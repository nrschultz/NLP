import sentParser
import sys


def tweetParser(filename, parser):
  f = open(filename,'r')
  pdict = parser
  tweetWordDict = {}
  numTweets = 0
  total_score = 0
  for line in f:
    numTweets += 1
    line = line.strip()
    line = line.split()
    total_tweet_score = 0
    for word in line:
      word = word.rstrip('.')
      #if word == 'good':
        #for word in line:
          #print word , pdict.get(word,0)
      total_tweet_score += pdict.get(word.lower(),0)
    for word in line:
      word = word.rstrip('.')
      word = word.lower()
      wordEntry = tweetWordDict.get(word, {'count':0, 'total_sent':0})
      wordEntry['count'] += 1
      wordEntry['total_sent'] += total_tweet_score
      tweetWordDict[word] = wordEntry
    total_score += total_tweet_score
  return tweetWordDict, pdict, numTweets, total_score

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
      sent_val = float(twd[key]['total_sent'])/(avg * float(twd[key]['count']))
      #print sent_val
    if abs(sent_val) > 1 and twd[key]['count'] > threshold:
      pd[key] = sent_val
      #print pd
  print len(pd)
      #print key, sent_val





def main(tweetRatio):
  pd = {}
  enhancers=sentParser.createEDict()
  for i in range(1,11):
    if i == 1:
      twd, pd, numTweets, total_score = tweetParser('testtweets.txt', sentParser.createSimpDict())
      #twd, pd, numTweets, total_score = tweetParserNegE('testtweets.txt',  
          #sentParser.createSimpDict(),enhancers)
    else:
      twd, pd, numTweets, total_score = tweetParser('testtweets.txt', pd)
      #twd, pd, numTweets, total_score = tweetParserNegE('testtweets.txt', pd, enhancers)
    print numTweets, total_score
    avg = (float(total_score)/float(numTweets))
    threshold = ((numTweets*tweetRatio))
    improvePD(twd,pd,threshold, avg)
  f = open('newparser.txt','w')
  for key in pd:
    f.write('%s %f\n' %(key,pd[key]))
  f.close()


if __name__ == '__main__': main(float(sys.argv[1]))



    
