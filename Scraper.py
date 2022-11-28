import re
import requests
from bs4 import BeautifulSoup

#Code from:
#https://www.codespeedy.com/download-all-images-of-a-webpage-using-python/

site = 'https://en.wikipedia.org/wiki/Cat' #Url to be used
response = requests.get(site)
soup = BeautifulSoup(response.text, 'html.parser')
image_tags = soup.find_all('img')
urls = [img['src'] for img in image_tags]
for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    if not filename:
         print("Regular expression didn't match with the url: {}".format(url))
         continue
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)
print("Download complete, downloaded images can be found in current directory!")
