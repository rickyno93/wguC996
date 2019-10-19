import requests
import bs4 as bs
import csv

r = requests.get('https://www.census.gov/programs-surveys/popest.html')
submissionFile = open('responseHtml.html', 'w+')
submissionFile.write(r.text)
submissionFile.close()

# setting up the soup borrowed from:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
soup = bs.BeautifulSoup(r.text,features='html.parser')
uriList = []

# bs4 usage idea borrowed from:
# https://www.youtube.com/watch?v=aIPqt-OdmS0
for url in soup.find_all('a'):
    uri = url.get('href')
    if type(uri) is str:
        if uri.startswith('http'):
            uriList.append(url.get('href'))
        if uri.startswith('/'):
            uriList.append('https://www.census.gov%s' % uri)

for i in range(len(uriList)):
    if uriList[i].endswith('/'):
        uriList[i] = uriList[i][:-1]

# duplicate elements in list removal borrowed from:
# https://www.w3schools.com/python/python_howto_remove_duplicates.asp
uriList = list(dict.fromkeys(uriList))

with open('uriList.csv','w') as uriListFile:
    wr = csv.writer(uriListFile, quoting=csv.QUOTE_ALL)
    wr.writerow(uriList)

print('Success')
