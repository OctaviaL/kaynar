import requests
from bs4 import BeautifulSoup as BS


def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html):
    soup = BS(html, 'lxml')
    return soup

def get_data(soup):
    post = soup.find_all('div', class_='homepage_container__dCpGD')
    data =[]

    count_ = 0

    for i in post:
        photo = i.find('img').get('src')
        description_url = i.find('a', class_="ArticleItem--name").get('href')
        description_html = get_html(description_url)
        description_soup = get_soup(description_html)
        description = description_soup.find('div', class_="BbCode").text.replace('\n', '')
        
        data.append([photo, description])

        count_ += 1
        if count_ == 20:
            break
     
    return data





def main():
    url = 'https://fullstack-hacaton-makers.vercel.app/'
    html = get_html(url)
    soup = get_soup(html)
    data = get_data(soup)
    return data
