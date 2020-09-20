# If you want to scrape a website :
# 1. Use the API
# 2. HTML Web Scraping using some tool like bs4



#step 0:

#pip install requests
#pip install bs4
#pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com/"


#step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)



#step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)


#step 3: HTML Tree Traversal  

#Commonly used type of objects
#1.Tag
#2.NavigableString
#3. BeautifulSoup
#4. Comment
markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))



#print(title)
#print(type(soup))
#print(type(title))
#print(type(title.string))

#get the title of html page
title = soup.title

#Get all the anchor tags from the page
anchors = soup.find_all('a')

#Get all links on the page
for link in  anchors:
    print(link.get('href'))
    
#print(anchors)
print(soup.find('p')['class'])

#find all the elements with class lead
print(soup.find_all("p", class_="lead"))

#get text from tags/soup
print(soup.find('p').get_text())
#get all soup text
print(soup.get_text())


#Get all the anchor tags from the page
anchors = soup.find_all('a')
all_links = set()
#Get all links on the page
for link in  anchors:
    if(link != '#'):
        link = "https://codewithharry.com" +link.get('href')
        all_links.add(link)
        print(link)
    
