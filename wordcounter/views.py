from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    wordDict = {}
    for word in wordlist:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

    sortedWords = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)
    char_count = len(fulltext)
    context = {
        'fulltext':fulltext, 
        'count': len(wordlist), 
        'sortedWords': sortedWords, 
        'char_count': char_count
    }
    return render(request, 'count.html', context)



