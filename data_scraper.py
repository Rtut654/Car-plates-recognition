import json 
import requests 
import urllib3
from urllib import request
from bs4 import BeautifulSoup

names = ['российские авто 1','машины с российскими номерами 2','авто в россии 1',
'авто в москве 1','авто на российских дорогах 1','автомобили в томске 1',
'автомобили в томске 1','авто в москве 6','автомобили в иркутске','авто в россии один']

USER_NAME = ''
YOUR_YANDEX_KEY = ''
YOUR_BROWSER_NEADER = ''
t=252
for x in names[:1]:
  query = x
  query = request.quote(query.encode('cp1251'))
  query =  '+'.join(query.split()) 
  url = "https://yandex.ru/search/xml?user=USER_NAME&key=YOUR_YANDEX_KEY&text="+query+"&from=tabbar&groupby=attr%3Dd.mode%3Ddeep.groups-on-page%3D100.docs-in-group%3D3"
  header = YOUR_BROWSER_NEADER
  http = urllib3.PoolManager()
  req = http.request(method='get',url=url,headers=header)
  soup = BeautifulSoup(req.data)
  print(url)

  n = 1
  listimg = []
  for i in range(n):
    listimg.append(str(soup.find_all("div",{"class":"serp-item serp-item_type_search serp-item_group_search serp-item_pos_"+str(i)+ " serp-item_scale_yes justifier__item i-bem"})))
    print()

  #нужно поиграться со split-ами
  k=0
  purelist = []
  for i in range(n):
    try:
      purelist.append(listimg[i].split('origin')[1].split('"url"')[1][2:-25])
    except:
      k=k+1
  print(k)    

  # purelist # just to look at the list of links
  # !rm /content/gdrive/My\ Drive/download/*  #отчистка папки на drive
  for i in range(n):
    # try:
        with open('/data/'+str(t), 'wb') as img:
            response = requests.get(purelist[i], stream=True)
            img.write(response.content)
            t = t+1
    # except:
    #   print(1)         
