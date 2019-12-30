from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.youtube.com/results?search_query=python')
res.text

bs = BeautifulSoup(res.text,'lxml')
elements = bs.find_all('ul',class_='yt-lockup-meta-info')
len(elements)
archivo = open('lista.txt','w') 

for ele in elements:
    lis=ele.findChildren()
    for li in lis:
        if li.string.endswith('views'):
            archivo.write(li.text+'\n') 
            print(li.text)
    
archivo.close()