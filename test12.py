import bs4, requests, os

os.chdir('/home/uriel/Documents/test')
os.makedirs('xkcd', exist_ok=True)
url = 'http://www.xkcd.com'
print('Downloading page %s...' % url)
page = requests.get(url)
page.raise_for_status()
soup = bs4.BeautifulSoup(page.text,'html.parser')
comic = soup.select('#comic img')
if comic == []:
    print('no image found')
else:
    comic_image = requests.get('http:'+ comic[0].get('src'))
    comic_image.raise_for_status()
imageFile = open(os.path.join('xkcd', os.path.basename(comic[0].get('src'))),'wb')
for chunk in comic_image.iter_content(100000):
    imageFile.write(chunk)
imageFile.close()


