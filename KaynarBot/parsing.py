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
    dogs = soup.find_all('div', class_="homepage_dog_div__da_k9")
    return dogs


def get_cats(soup):
    cats = soup.find_all('div', class_="homepage_cat_div__r2tu8")
    return cats


def main():
    url = 'https://fullstack-hacaton-makers.vercel.app/'
    html = get_html(url)
    soup = get_soup(html)
    cats = get_cats(soup)
    dogs = get_dogs(soup)

    return dogs, cats

main()

