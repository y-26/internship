#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')


# In[2]:


get_ipython().system('pip install requests')


# # Q-1

# In[3]:


import requests
from bs4 import BeautifulSoup 
page=requests.get("https://en.wikipedia.org/wiki/Main_Page")
page
 


# In[4]:


soup=BeautifulSoup(page.content)
soup.prettify()


# In[10]:


header= soup.find_all('span', class_="mw-headline")


# In[11]:


header
    


# In[12]:


header=[]


# In[13]:


for i in soup.find_all('span',class_="mw-headline"):
    header.append(i.text)


# In[14]:


header


# # Q-2

# In[101]:


import requests
from bs4 import BeautifulSoup 
import pandas as pd
page=requests.get("https://www.imdb.com/chart/top")
page


# In[102]:


soup=BeautifulSoup(page.content)
soup.prettify()


# In[109]:


movies= soup.find_all('td', class_="titleColumn")


# In[110]:


movies


# In[117]:


name=[]
for i in soup.find_all('td',class_="titleColumn"):
    name.append(i.text.replace('\n',''))


# In[118]:


name


# In[121]:


rating=[]
for i in soup.find_all('td',class_="ratingColumn imdbRating"):
    rating.append(i.text.replace('\n',''))
    


# In[122]:


rating


# In[123]:


yearofrelease=[]
for i in soup.find_all('span',class_="secondaryInfo"):
    yearofrelease.append(i.text)


# In[124]:


yearofrelease


# In[125]:


data=pd.DataFrame()


# In[126]:


data['Movies namme']= name


# In[127]:


data['Ratings']= rating


# In[128]:


data['yearofrelease']=yearofrelease


# In[150]:


data


# In[151]:


data.head(101)


# # Q-3

# In[1]:


import requests
from bs4 import BeautifulSoup 
import pandas as pd
page=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
page


# In[2]:


soup=BeautifulSoup(page.content)
soup.prettify()


# In[3]:


movie= soup.find_all('td', class_="titleColumn")


# In[4]:


movie


# In[6]:


moviename=[]


# In[7]:


for i in soup.find_all('td',class_="titleColumn"):
    moviename.append(i.text.replace('\n',''))


# In[8]:


moviename


# In[9]:


movierating=[]
for i in soup.find_all('td',class_="ratingColumn imdbRating"):
    movierating.append(i.text.replace('\n',''))
    


# In[10]:


movierating


# In[11]:


yearofreleasing=[]
for i in soup.find_all('span',class_="secondaryInfo"):
    yearofreleasing.append(i.text)


# In[12]:


yearofreleasing


# In[13]:


data=pd.DataFrame()


# In[14]:


data['Movies namme']= moviename


# In[15]:


data['Ratings']= movierating


# In[16]:


data['yearofrelease']=yearofreleasing


# In[18]:


data.head(101)


# # Q-4

# In[19]:


import requests
from bs4 import BeautifulSoup 
import pandas as pd
page=requests.get("https://meesho.com/bags-ladies/pl/p7vbp")
page


# In[20]:


soup=BeautifulSoup(page.content)
soup.prettify()


# In[57]:


Productname=soup.find_all('p',class_="Text__StyledText-sc-oo0kvp-0 cPgaBh NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 hofZGw NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 hofZGw")


# In[58]:


Productname


# In[59]:


Productname=[]


# In[60]:


for i in soup.find_all('p',class_="Text__StyledText-sc-oo0kvp-0 cPgaBh NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 hofZGw NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 hofZGw"):
    Productname.append(i.text)


# In[61]:


Productname


# In[62]:


Productprice=soup.find_all('h5',class_="Text__StyledText-sc-oo0kvp-0 dLSsNI")


# In[63]:


Productprice


# In[66]:


Productprice=[]


# In[68]:


for i in soup.find_all('h5',class_="Text__StyledText-sc-oo0kvp-0 dLSsNI"):
 Productprice.append(i.text)


# In[69]:


Productprice


# In[70]:


Productdiscount=soup.find_all('span',class_="Text__StyledText-sc-oo0kvp-0 cZvGTZ")


# In[71]:


Productdiscount


# In[73]:


Productdiscount=[]


# In[77]:


for i in soup.find_all('span',class_="Text__StyledText-sc-oo0kvp-0 cZvGTZ"):
    Productdiscount.append(i.text)


# In[78]:


Productdiscount


# # Q.5 (a)

# In[81]:


import requests
from bs4 import BeautifulSoup 
import pandas as pd
page=requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
page


# In[82]:


soup=BeautifulSoup(page.content)
soup.prettify()


# In[83]:


Team=soup.find_all('span',class_="u-hide-phablet")


# In[84]:


Team


# In[86]:


Team=[]


# In[87]:


for i in soup.find_all('span',class_="u-hide-phablet"):
    Team.append(i.text)


# In[90]:


Team


# In[116]:


table=soup.find('div',class_="rankings-block__container full rankings-table")


# In[117]:


print(table)


# In[132]:


df=pd.read_html('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')


# In[135]:


df[0].head(10)


# # Q5 (b)

# In[137]:


import requests
from bs4 import BeautifulSoup 
import pandas as pd
page=requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting")
page


# In[138]:


soup=BeautifulSoup(page.content)
soup.prettify()


# In[139]:


df=pd.read_html('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')


# In[140]:


df[0].head(10)


# 
# # Q.5 (c)

# In[150]:


import requests
from bs4 import BeautifulSoup 
import pandas as pd
page=requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/all-time-bowling")
page


# In[151]:


soup=BeautifulSoup(page.content)
soup.prettify()


# In[152]:


df=pd.read_html('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/all-time-bowling')


# In[158]:


df


# # Q.6 (a)
# 

# In[159]:


import requests
from bs4 import BeautifulSoup 
import pandas as pd
page=requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")
page


# In[160]:


soup=BeautifulSoup(page.content)
soup.prettify()


# In[162]:


df=pd.read_html('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')


# In[163]:


df[0].head(10)


# # Q.6(b)

# In[164]:


import requests
from bs4 import BeautifulSoup 
import pandas as pd
page=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting")
page


# In[165]:


soup=BeautifulSoup(page.content)
soup.prettify()


# In[166]:


df=pd.read_html('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')


# In[167]:


df[0].head(10)


# # Q.6 (c)

# In[169]:


import requests
from bs4 import BeautifulSoup 
import pandas as pd
page=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder")
page


# In[170]:


soup=BeautifulSoup(page.content)
soup.prettify()


# In[171]:


df=pd.read_html('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')


# In[172]:


df[0].head(10)


# # Q.7
# 

# In[173]:


import requests
from bs4 import BeautifulSoup 
page=requests.get("https://coreyms.com/")
page


# In[174]:


soup=BeautifulSoup(page.content)
soup.prettify()


# In[175]:


header= soup.find_all('a', class_="entry-title-link")


# In[176]:


header


# In[177]:


header=[]


# In[178]:


for i in soup.find_all('a',class_="entry-title-link"):
    header.append(i.text)


# In[179]:


header


# In[180]:


time= soup.find_all('time', class_="entry-time")


# In[183]:


time


# In[184]:


time=[]


# In[185]:


for i in soup.find_all('time',class_="entry-time"):
    time.append(i.text)


# In[186]:


time


# In[188]:


content= soup.find_all('div', class_="entry-content")


# In[189]:


content


# In[190]:


content=[]


# In[191]:


for i in soup.find_all('div',class_="entry-content"):
    content.append(i.text)


# In[192]:


content


# In[198]:


link= soup.find_all('div', class_="ytp-title-text")


# In[199]:


link


# # Q.8

# In[255]:


import requests
import pandas as pd
from bs4 import BeautifulSoup 
page=requests.get("https://www.nobroker.in/property/sale/hyderabad/multiple?searchParam=W3sibGF0IjoxNy40NDc0NDc1LCJsb24iOjc4LjM1NjkyNzUsInBsYWNlSWQiOiJDaElKZzVwcF9KU1R5enNSaHBYNzU2M2VkX2ciLCJwbGFjZU5hbWUiOiJJbmRpcmEgTmFnYXIifSx7ImxhdCI6MTcuNTAwMDcyOCwibG9uIjo3OC40MDUxOTU5OTk5OTk5OSwicGxhY2VJZCI6IkNoSUpzWEZxb3VtUnl6c1JiWlZ5ZGVqMkdKSSIsInBsYWNlTmFtZSI6IkpheWFuYWdhciBDb2xvbnkifSx7ImxhdCI6MTcuMzkwNTk4MywibG9uIjo3OC4zMzgzNTEsInBsYWNlSWQiOiJDaElKbjVoZFVsLVV5enNSRUpnOHktRmhyejQiLCJwbGFjZU5hbWUiOiJSYWphcHVzaHBhIEF0cmlhIn1d&radius=2.0&city=hyderabad&locality=Indira%20Nagar,&locality=Jayanagar%20Colony,&locality=Rajapushpa%20Atria")
page


# In[201]:


soup=BeautifulSoup(page.content)
soup.prettify()


# In[202]:


Housetitle= soup.find_all('span', class_="overflow-hidden overflow-ellipsis whitespace-nowrap max-w-80pe po:max-w-full")


# In[203]:


Housetitle


# In[205]:


Housetitle=[]


# In[207]:


for i in soup.find_all('span',class_="overflow-hidden overflow-ellipsis whitespace-nowrap max-w-80pe po:max-w-full"):
    Housetitle.append(i.text)


# In[208]:


Housetitle


# In[209]:


Houselocation= soup.find_all('div', class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0 po:max-w-95")


# In[210]:


Houselocation


# In[213]:


Houselocation=[]


# In[214]:


for i in soup.find_all('div',class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0 po:max-w-95"):
    Houselocation.append(i.text)


# In[215]:


Houselocation


# In[247]:


emi= soup.find_all('div', class_="font-semi-bold heading-6")


# In[248]:


emi


# In[251]:


emi=[]


# In[252]:


for i in soup.find_all('div',class_="font-semi-bold heading-6"):
    emi.append(i.text)


# In[253]:


emi


# # Q.9

# In[254]:


#1


# In[256]:


import requests
import pandas as pd
from bs4 import BeautifulSoup 
page=requests.get("https://www.dineout.co.in/delhi-restaurants/buffet-special")
page


# In[257]:


soup=BeautifulSoup(page.content)
soup.prettify()


# In[258]:


Restroname= soup.find_all('div', class_="restnt-info cursor")


# In[259]:


Restroname


# In[260]:


Restroname=[]


# In[261]:


for i in soup.find_all('div',class_="restnt-info cursor"):
    Restroname.append(i.text)


# In[262]:


Restroname


# In[263]:


#2


# In[265]:


Cuisine= soup.find_all('div', class_="filter-component-wrap cuisine-wrap")


# In[266]:


Cuisine


# In[267]:


Cuisine=[]


# In[268]:


for i in soup.find_all('div',class_="filter-component-wrap cuisine-wrap"):
    Cuisine.append(i.text)


# In[269]:


Cuisine


# In[270]:


#3


# In[271]:


Location= soup.find_all('div', class_="restnt-loc ellipsis")


# In[272]:


Location


# In[273]:


Location=[]


# In[274]:


for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    Location.append(i.text)


# In[275]:


Location


# In[276]:


#4


# In[277]:


Rating= soup.find_all('div', class_="restnt-rating rating-4")


# In[278]:


Rating


# In[279]:


Rating=[]


# In[280]:


for i in soup.find_all('div',class_="restnt-rating rating-4"):
    Rating.append(i.text)


# In[281]:


Rating


# In[282]:


#5


# In[294]:


Image= soup.find_all('img', class_="no-img")


# In[295]:


Image


# In[296]:


Image=[]


# In[297]:


for i in soup.find_all('img',class_="no-img"):
    Image.append(i['data-src'])


# In[298]:


Image


# # Q.10

# In[299]:


import requests
import pandas as pd
from bs4 import BeautifulSoup 
page=requests.get("https://www.bewakoof.com/women-tshirts?ga_q=tshirts")
page


# In[300]:


soup=BeautifulSoup(page.content)
soup.prettify()


# In[ ]:


(/, No, products, are, available, on, this, link, and, the, link, is, invalid, .)

