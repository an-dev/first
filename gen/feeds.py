import sys
from urllib2 import urlopen
from urllib import quote

d = []

def open_topics():
	with open('topics.txt','rU') as f:
		for line in f:
			print line,
			d.append(line.split(':')[0])

def main():  

	key = "MDEwNjQyNzU3MDEzNTY3MTI3MzM5ZjUxNg001"
	url = "http://api.npr.org/query?apiKey={0}&requiredAssets=audio&output=HTML&format=HTML".format(key)

	open_topics()

	npr_id = raw_input("Inserisci un ID relativo agli argomenti forniti dall'NPR...")
	search_string = raw_input("Inserisci un parametro di ricerca...")

	if npr_id in d and search_string:
		raw_input("Premi invio per continuare...")
		
		url+= "&id=" + npr_id
			
		url += "&searchterm=" + quote(search_string)
				
		response = urlopen(url)
		output = response.read()
		with open('file.html', 'w') as my_feed:
			my_feed.write(output)
		print "Scrittura del file eseguita con successo!"
		
	else:
		print "Non e' stato inserito un ID o parametro valido."
	
	
if __name__ == '__main__':
  main()