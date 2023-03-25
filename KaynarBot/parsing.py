import requests
from bs4 import BeautifulSoup as BS
from django.dispatch import receiver


def get_html(url):
    response = requests.get(url)
    return response.text


def get_soup(html):
    soup = BS(html, 'lxml')
    return soup


def get_dogs(soup):
    dogs = soup.find_all('div', class_="pet.card_container")
    data = []

    count_ = 0

    
    for i in dogs:
        title = i.find('a', class_="").text.strip()
        photo = i.find('img').get('src')
        description_url = i.find('a', class_="ArticleItem--name").get('href')
        description_html = get_html(description_url)
        description_soup = get_soup(description_html)
        description = description_soup.find('div', class_="BbCode").text.replace('\n', '')
        data.append([title, photo, description])

        count_ += 1
        if count_ == 20:
            break
     
    return data


def get_cats(soup):
    cats = soup.find_all('div', class_="homepage_cat_div__r2tu8")
    data = []

    count_ = 0

    
    for i in cats:
        title = i.find('a', class_="").text.strip()
        photo = i.find('img').get('src')
        description_url = i.find('a', class_="ArticleItem--name").get('href')
        description_html = get_html(description_url)
        description_soup = get_soup(description_html)
        description = description_soup.find('div', class_="BbCode").text.replace('\n', '')
        data.append([title, photo, description])

        count_ += 1
        if count_ == 20:
            break
     
    return data

def main():
    url = 'https://fullstack-hacaton-makers.vercel.app/'
    html = get_html(url)
    soup = get_soup(html)
    cats = get_cats(soup)
    dogs = get_dogs(soup)

    return dogs, cats

main()

