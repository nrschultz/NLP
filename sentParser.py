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


def createSimpDict(fname, num_dicts):
  f = open(fname, 'r')

  if num_dicts == 1:
    dt={}
    for line in f:
      line=line.split()
      dt[line[0]]=float(line[1])
    return dt
  else:
    p_dt = {}
    n_dt = {}
    for line in f:
      line = line.split()
      sent = float(line[1])
      if sent > 0:
        p_dt[line[0]] = sent
      elif sent < 0:
        n_dt[line[0]] = sent
    return p_dt, n_dt

def createEDict():
  f=open('sentEnhancers.txt', 'r')
  dt={}
  for line in f:
    line=line.split()
    dt[line[0]]=float(line[1])
  return dt



if __name__ == '__main__': main()

