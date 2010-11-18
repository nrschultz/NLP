import sentParser

def tweetParser(filename, parser):
  f = open(filename,'r')
  pdict2 = sentParser.createParseDict()
  pdict = sentParser.createSimpDict()
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
      word = word.rstrip('.')
      word = word.lower()
      wordEntry = tweetWordDict.get(word, {'count':0, 'total_sent':0})
      wordEntry['count'] += 1
      wordEntry['total_sent'] += total_score
      tweetWordDict[word] = wordEntry
  return tweetWordDict, pdict

def improvePD(twd, pd):
  improvedic={}
  for key in twd.keys():
    sent_val = 0.0
    #print twd[key]['count']
    if twd[key]['count'] != 0:
      sent_val = float(twd[key]['total_sent'])/float(twd[key]['count'])
      #print sent_val
    if abs(sent_val) > 1 and twd[key]['count'] > 200:
      improvedic[key]= sent_val
      findKey(key,pd)


def findKey(key,pd):
  keythere=0
  for word in pd:
    if key==word:
      keythere=1
  if keythere==1:
    return True
  else:
    print "New sentmt word found", key, "\n"
    return False
   




    
  


def main():
  twd, pd = tweetParser('/scratch/nschult1/apptweets.txt', 'parser2')
  improvePD(twd,pd)

if __name__ == '__main__': main()



      
