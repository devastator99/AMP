
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# GEtting news from Times of India
  
    
url = "https://www.perplexity.ai/discover"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

headings_and_content = []

# Find the container that encapsulates both heading and content
for container in soup.find_all('div', class_='grid grid-cols-1 gap-six md:grid-cols-2 lg:grid-cols-3'):
    # Within each container, find heading and content
    heading = container.find('div', class_='break-all transition duration-300 line-clamp-1 md:group-hover:text-super md:dark:group-hover:text-superDark')
    content = container.find('div', class_='break-word text-balance mt-two line-clamp-2 light font-sans text-base text-textOff dark:text-textOffDark selection:bg-super/50 selection:text-textMain dark:selection:bg-superDuper/10 dark:selection:text-superDark')
    
    # Check if both heading and content are found before appending
    if heading and content:
        headings_and_content.append({
            'heading': heading.text.strip(),
            'content': content.text.strip()
        })

#Getting news from Hindustan times

ht_r = requests.get("https://www.hindustantimes.com/india-news/")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
ht_headings = ht_soup.findAll("div", {"class": "headingfour"})
ht_headings = ht_headings[2:]
ht_news = []

for hth in ht_headings:
    ht_news.append(hth.text)


def index(req):
    return render(req, 'news/index.html', {'headings_and_content':headings_and_content, 'ht_news': ht_news})

