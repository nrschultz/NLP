def main():
  f = open('subjclueslen1-HLTEMNLP05.tff','r')
  dt = {}
  for line in f:
    line = line.split()
    s = line[2].split('=')[1]
    pol = ''
    if line[5].split('=')[1] == 'positive':
      pol = '+'
    else:
      pol = '-'
    strength = ''
    if line[0].split('=')[1] == 'strongsubj':
      strength = 'strong'
    else:
      strength = 'weak'
    dt[s] = (pol,strength)
  print dt




if __name__ == '__main__': main()

