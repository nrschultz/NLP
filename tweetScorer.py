import sentParser


def tweetScorer(filename, parser, enhancers, neg, enh):
  f = open(filename,'r')
  pdict = parser
  edict=enhancers
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
      if neg==True:
        if i>2:
          if lineDict.get(i-2)=='not' or lineDict.get(i-1)=='not':
            total_tweet_score-=pdict.get(word.lower(),0)
          else:
            if enh==True:
              if edict.has_key(lineDict.get(i-1)):
                  weight=edict.get(lineDict.get(i-1))
                  total_tweet_score+=weight*pdict.get(word.lower(),0)
              else:
                total_tweet_score+= pdict.get(word.lower(),0)
            else:
                total_tweet_score += pdict.get(word.lower(),0)
        else:
          total_tweet_score+=pdict.get(word.lower(),0)
      else:
        total_tweet_score+=pdict.get(word.lower(),0)
      i+=1
    total_score += total_tweet_score
    string=''
    scored={}
    for i in range(len(lineDict)):
      string+=lineDict[i]
      string+=' '
      if pdict.get(lineDict[i],0)!=0:
        scored[lineDict[i]]=pdict.get(lineDict[i], 0)

    print "'"+string+"'"   
    print "\nTotal Score of tweet: ", total_tweet_score
    print "Scored tweet on: ", scored, "\n"

  return total_score



def main():
  txt='newparser.txt'
  txt2='sentmtListsm.txt'
  total_score=tweetScorer('testtweets.txt', sentParser.createSimpDict(txt),
      sentParser.createEDict(), True, True)
  print "Total Score: ", total_score
  


if __name__ == '__main__': main()

