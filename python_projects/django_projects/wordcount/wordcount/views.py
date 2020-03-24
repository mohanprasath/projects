from django.shortcuts import render
from . import views
from collections import Counter


def home(request):
	return render(request, 'hello.html',  {"author":"Mohan Prasath Chinnasamy"})

def author(request):
	return render(request, 'author.html')

def count(request):
	user_text_entry = request.GET['usertext']
	splitted_words = user_text_entry.split(' ')
	results = []
	for entry in Counter(splitted_words).most_common():
		results.append(str(entry[0]) + " - " + str(entry[1]))
	return render(request, 'count.html', 
		{'user_entry':user_text_entry, 
		'word_count':results,
		'total_words':len(splitted_words)})