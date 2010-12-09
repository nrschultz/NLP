def main():
  f = open('/scratch/nschult1/tweets.txt','r')
  w = open('/scratch/nschult1/prunedTweets.txt','w')
  d = {}
  for line in f:
    d[line] = d.get(line,0) + 1
  for key in d:
    w.write(key)

main()

