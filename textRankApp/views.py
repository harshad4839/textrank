from django.http import request
from django.shortcuts import render
import textRankApp.apps as txt

def home(request): 
    
    return render(request, 'textRankApp/home.html')

def result(request):
    text = request.GET["text"]

    tr4w = txt.TextRank4Keyword()
    tr4w.analyze(text, candidate_pos = ['NOUN', 'PROPN'], window_size=4, lower=False)
    result=tr4w.get_keywords(10)
    return render(request, 'textRankApp/result.html', {'result':result})
