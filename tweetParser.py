import sentParser
def main():
  f = open('testtweets.txt','r')
  pdict = sentParser.createParseDict()
  pdict = {'top':1, 'terrible':-1}
  tweetWordDict = {}
  for line in f:
    line = line.strip()
    line = line.split()
    total_score = 0
    for word in line:
      word = word.rstrip('.')
      #if word == 'good':
        #for word in line:
          #print word , pdict.get(word,0)
      total_score += pdict.get(word.lower(),0)
    for word in line:
      wordEntry = tweetWordDict.get(word, {'count':0, 'total_sent':0})
      wordEntry['count'] += 1
      wordEntry['total_sent'] += total_score
      tweetWordDict[word] = wordEntry
  print tweetWordDict['app']


if __name__ == '__main__': main()



      
