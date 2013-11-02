import sys

def do(d,filename):
  f = open(filename,'rU')
  for line in f:
    wordlist = line.split()
    for word in wordlist:
      word = word.lower()
      if word and word not in d:
        d[word] = 1
      else: 
        d[word] = d[word] + 1
  f.close()

def print_words(filename):  
  d = {}
  do(d,filename)
  
  for key in sorted(d.keys()):
    print key, d[key]

def print_top(filename):
  d = {}
  do(d,filename)

  def func(e):
    return e[1]

  items = sorted(d.items(), key = func, reverse = True)

  for k in items[:20]:
    print k[0], k[1]
  
###

def main():
  if len(sys.argv) != 3:
    print 'opzioni: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'opzioni sconosciuta: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
