def main():
  f = open('gs_tweets.txt','r')
  for line in f:
    line = line.split()
    line[0] = line[0][1:]
    for i in range(len(line)):
      line[i] = line[i][1:len(line[i])-2]
    pol_d = {}
    for word in line:
      pol_d[word] = 0
    print pol_d
main()

