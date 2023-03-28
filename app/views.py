from django.shortcuts import render,HttpResponse
from bs4 import BeautifulSoup
import requests
from .models import Article
import hashlib
# Create your views here.
def scrap(request):
    
    url = 'https://www.theverge.com/'
    response = requests.get(url)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    articles_names = soup.find_all('div', class_='max-w-content-block-standard md:w-content-block-compact md:max-w-content-block-compact lg:w-[240px] lg:max-w-[240px] lg:pr-10')
   
    for i in range(0,len(articles_names)):
        id=i+1
        heading=articles_names[i].find('h2',class_='font-polysans text-20 font-bold leading-100 tracking-1 md:text-24 lg:text-20')
        author_name=articles_names[i].find('a',class_='text-gray-31 hover:shadow-underline-inherit dark:text-franklin mr-8')
        url1=articles_names[i].find('a',class_='group-hover:shadow-underline-franklin')
        url2="https://www.theverge.com"+url1.get('href')
        date=articles_names[i].find('span',class_='text-gray-63 dark:text-gray-94')
        print(id,heading.text,author_name.text,url2,date.text)
        Article.objects.create(id=id,headline=heading.text,url=url2,author=author_name.text,date=date.text)
    
    return HttpResponse("scraped")
