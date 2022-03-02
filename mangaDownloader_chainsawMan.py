#downloads Chainsaw Man
import requests, os, bs4 
import urllib.request


#Edit this depending on manga
url = 'https://w16.read-chainsawman.com/'
mangaName = 'Chainsaw Man'

#create folder
os.makedirs(mangaName, exist_ok=True)

#loop over every link 

#download initial html 
res = requests.get(url)
res.raise_for_status() 
soup = bs4.BeautifulSoup(res.text, 'html.parser')

chapterElems = soup.select('#Chapters_List a')
totalChapters = len(chapterElems)

for i in range(totalChapters):
  chapterUrl = chapterElems[i].get('href')
  #request individual chapter
  print('Downloading Chapter %s...' %chapterUrl)
  chapterRes = requests.get(chapterUrl)
  chapterRes.raise_for_status() 

  chapterSoup = bs4.BeautifulSoup(chapterRes.text, 'html.parser')
  imageElems = chapterSoup.select('.entry-content img')
  numPages = len(imageElems)
  for j in range(numPages): 
    imageUrl = imageElems[j].get('src')

    print('Downloading image %s...' %imageUrl)

    #(totalChapters - i) if manga listed in descending order 
    customPageName = 'Chapter'+str(totalChapters - i)+'Page'+str(j) + '.jpg'

    #os.path.join so downloaded files are 
    imageFile = open(os.path.join(mangaName, customPageName), 'wb')

    imageRes = requests.get(imageUrl)
    imageRes.raise_for_status()
    for chunk in imageRes.iter_content(100000):
      imageFile.write(chunk)
  imageFile.close()
