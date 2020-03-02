from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	# return HttpResponse('Helloworld!')
	#return render(request, 'home.html', {'hi':'hellojiii'})
	return render(request, 'home.html')

def eggspage(request):
	return HttpResponse("Eggs are great ")

def count(request):
	fulltext = request.GET['fulltext']
	worddictonary = dict()
	wordlist = fulltext.split()
	for words in wordlist:
		if words in worddictonary:
			worddictonary[words] +=1 
		else:
			worddictonary[words] =1
	return render(request,'count.html', {'fulltextkey' : fulltext, 'wordscount' :len(wordlist), 'worddictonary' : sorted(worddictonary.items(),key=operator.itemgetter(1),reverse=True)})
#count.html mein sirf hum {{ --- }} aise call krenge python dictonary ko... --- will replace by dictonary key.

def about(request):
	return render(request,'aboutus.html')