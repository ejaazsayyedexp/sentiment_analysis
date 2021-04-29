import requests
import re
from bs4 import BeautifulSoup as bs

def get_movie_review(movie_name='the dark knight'):
    first_link = "https://www.imdb.com/find?q="
    response = requests.get(first_link+movie_name)
    soup1 = bs(response.text,'html5lib')

    movie_list = list(soup1.find_all('td',{'class':'result_text'}))

    movie = str(movie_list[0])

    link = "https://imdb.com"+movie.split('"')[3]+'reviews'
    print(link)
    reviews = []

    for i in range(1,11):
        newlink =link+'?spoiler=hide&sort=helpfulnessScore&dir=desc&ratingFilter='+str(i)
        res = requests.get(newlink)
        soup2 = bs(res.text,'html.parser')
        rev = soup2.find('div',{'class':'text'})
        if(rev):
            rev = str(rev)
            rev = rev[1:]
            rev = rev[rev.index('>')+1:rev.index('<')]
            reviews.append(rev)
    return reviews










