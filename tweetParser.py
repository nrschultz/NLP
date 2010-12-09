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
  for i in range(1,11):
    if i == 1:
      twd, pd, numTweets, total_score = tweetParser('/scratch/nschult1/prunedTweets.txt', sentParser.createSimpDict())
    else:
      twd, pd, numTweets, total_score = tweetParser('/scratch/nschult1/prunedTweets.txt', pd)
    print numTweets, total_score
    avg = (float(total_score)/float(numTweets))
    threshold = ((numTweets*tweetRatio))
    improvePD(twd,pd,threshold, avg)
  f = open('newparser.txt','w')
  for key in pd:
    f.write('%s %f\n' %(key,pd[key]))
  f.close()


if __name__ == '__main__': main(float(sys.argv[1]))



      
