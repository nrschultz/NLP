def main():
  createParseDict()

def createParseDict():
  f = open('subjclueslen1-HLTEMNLP05.tff','r')
  dt = {}
  for line in f:
    line = line.split()
    s = line[2].split('=')[1]
    pol = ''
    if line[5].split('=')[1] == 'positive':
      pol = 1
    else:
      pol = -1
    strength = ''
    if line[0].split('=')[1] == 'strongsubj':
      strength = 2
    else:
      strength = 1
    dt[s] = pol*strength
  return dt

def createSimpDict():
  f = open('sentmtListsm.txt','r')
  dt = {}
  for line in f:
    line = line.split()
    dt[line[0]] = int(line[1])
  return dt



if __name__ == '__main__': main()

