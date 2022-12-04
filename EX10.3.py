
fname = input("enter a file name ")
fname = open(fname)
fname = str()
import string

leter = dict()
for line in fname:
    line = line.split()
    line = line.lower()
    line = line.translate(None, string.punctuation)
    for t in line:
	    word = list(t)
for letter in word:
			leter[leter] = leter.get(letter,0) + 1
letterlist = []
for letter, count in leter.items():
	letterlist.append( (count, letter) )
letterlist.sort(reverse=True)
for count, letter in letterlist:
	print (letter, count)
