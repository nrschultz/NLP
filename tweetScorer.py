import sentParser



def scorer(tweets, pdict, enhancers, neg_bool, enh_bool):
  p_max = 0
  p_tweet = ''
  n_max = 0
  n_tweet = ''
  edict=enhancers
  numTweets = 0
  total_score = 0
  for line in tweets:
    scored = {}
    numTweets += 1
    total_tweet_score = 0
    for i in range(len(line)):
      word = line[i]
      word_score = pdict.get(word,0)
      if neg_bool:
        if i>2:
          if line[i-1]=='not' or line[i-2]=='not':
            word_score = -1.0*word_score
          else:
            if enh_bool:
              if edict.has_key(line[i-1]):
                  weight=edict.get(line[i-1])
                  word_score = (float(weight)*word_score)
      if abs(word_score) > 0:
        scored[word] = word_score
      total_tweet_score += word_score
    total_score += total_tweet_score
    string=' '.join(line)    
    if total_tweet_score > p_max:
      p_tweet = string
      p_max = total_tweet_score
    if total_tweet_score < n_max:
      n_tweet = string
      n_max = total_tweet_score
    print scored
    #for word in line:
    #  string+=word
    #  string+=' '
    #  if pdict.get(lineDict[i],0)!=0:
    #    scored[lineDict[i]]=pdict.get(lineDict[i], 0)

    #if total_tweet_score < 0:
    #print "'"+string+"'"   
    #print "\nTotal Score of tweet: ", total_tweet_score
    #print "Scored tweet on: ", scored, "\n"
  
  return total_score



def main():
  txt='newparser.txt'
  txt2='sentmtListsm.txt'
  total_score=scorer('/scratch/nschult1/prunedTweets.txt', sentParser.createSimpDict(txt,1),
      sentParser.createEDict(), True, True)
  print "Total Score: ", total_score
  


if __name__ == '__main__': main()

