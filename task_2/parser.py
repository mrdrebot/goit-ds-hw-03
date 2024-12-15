import requests
from bs4 import BeautifulSoup
import json

def main():
    url = 'https://quotes.toscrape.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    # qoutes.json
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    tags = soup.find_all('div', class_='tags')

    qoutes_list = []

    for i in range(0, len(quotes)):
        tagsforquote = tags[i].find_all('a', class_='tag')

        tags_list = []
        for tagforquote in tagsforquote:
            tags_list.append(tagforquote.text)

        qoutes_list.append({"tags": tags_list, "author": authors[i].text, "quote": quotes[i].text})

    with open("./files/qoutes.json", "w", encoding="utf-8") as file:
        json.dump(qoutes_list, file)

    # authors.json
    authors_list = []

    for author in authors:
        a_tag = author.find_next_sibling('a')
        link = a_tag['href'][1:]
        response_data = requests.get(f"{url}{link}")
        soup_data = BeautifulSoup(response_data.text, 'lxml')
        div_tag = soup_data.find('div',  class_='author-details')
        name = div_tag.find('h3', class_= 'author-title').text
        born_date = div_tag.find('span', class_= 'author-born-date').text
        born_location = div_tag.find('span', class_= 'author-born-location').text
        descripion = div_tag.find('div', class_= 'author-description').text
        authors_list.append({"fullname": name, "born_date": born_date, "born_location": born_location, "descripion": descripion})

    with open("./files/authors.json", "w", encoding="utf-8") as file:
        json.dump(authors_list, file)

if __name__ == "__main__":
    main()