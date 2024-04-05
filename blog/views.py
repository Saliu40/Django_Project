from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import NewsModel 
# Create your views here.
#it takes in functions
# we need create 3functions coming from urls







def index(request):
    index = {'page': 'index page loading for the first time'}
    context = {'first_key': index}
    return render(request, 'blog/index.html', context) #making the right up to be dark


def about(request):
    about = {'page': 'about page loading for the first time'}
    context = {'first_key': about}
    return render(request, 'blog/about.html', about)

def news(request):
    
    url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-02-28&sortBy=publishedAt&apiKey=b639d2ca56a24615b262a157cee5be5f'

    data = requests.get(url)

    allnews = data.json()

    articles = allnews.get('articles', [])

    blog = NewsModel() 

    print(NewsModel.objects)

    for latest in articles:
        blog = NewsModel(description=latest['description'],title=latest['title'],
        url=latest['url'], content=latest['content'])

        blog.save()
        
        



    

    context = {'articles': articles}
    return render(request, 'blog/news.html')
