## Play around with the inspect function in a wikipedia wegpage, dive deep into the Developer Tools 

import pandas as pd
import requests


## Make a request to a certain page
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

## Check the status of the request
# print(r)

## Retrieve the content of the page (parsing the HTML)
# print(r.content)

## Import a library to 'prettify' the code, and get it done
from bs4 import BeautifulSoup

soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())

## Identify the title of the page and retrieve it onto the console
# s = soup.find('div', class_='entry-content')
# p = soup.find_all('title')
# print(p)

## Identify elements by class and ID, and retrieve an elements by refering to its group
# navbar = soup.find('div', class_ = 'header-main__slider')
# print(navbar)
# footer = soup.find('footer', id = 'gfg-footer')
# print(footer)

## Retrieve the <p> from the page, remove all tags and print it
# lines = s.find_all('p')

# for line in lines:
#     print(line.text)

## Retrieve a list you find in the page
s = soup.find('div', id='main')
leftbar = s.find('ul', class_='leftBarList')
print(leftbar)
# lines = lb.find_all('li')
# for line in lines: 
#     print(line.text)