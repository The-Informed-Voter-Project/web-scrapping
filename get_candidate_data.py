import requests
from requests import get
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from time import sleep
from random import randint

#initializing values
running_for =[]
profile_pics = []
candidate_names = []  

#scraping links from candidate page on KCE
req = Request("https://info.kingcounty.gov/kcelections/Vote/contests/candidates.aspx?eid=21")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")
cans_links=[]
links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))
    
#Removing none values from list
Not_none_values = filter(None.__ne__, links)

link_list = list(Not_none_values)

#Removing links that are not related to candidate info
for item in link_list:
    if 'GenericVoterGuide' in item:
        cans_links.append(item)

#Looping through every candidate profile and recording info
for item in cans_links:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    #Name, profile, bio
    role_links = soup.find("form",{"id": "frmMain"})
    role_links = role_links.find(class_ = "container-fluid m-0 p-0")
    role_links = role_links.find(class_ = "row m-0 p-0")
    role_links = role_links.find(class_ = "col-md-12 m-0 p-0")
    role_links = role_links.find(class_ = "row m-0 p-0")
    role_links = role_links.find(class_ = "container-fluid")
    role_links = role_links.find(class_ = "card rounded shadow bg-transparent col-xl-6 ml-auto mr-auto p-0")
    role_links = role_links.find(api = "https://voter.votewa.gov/elections")
    
    pic_links = soup.find('img').get('src')
    title_links = soup.find(class_ = "title").get_text()
    
    #Adding values to larger arrays
    running_for.append(role_links)
    profile_pics.append(pic_links)
    candidate_names.append(title_links)
    
    #Delay timer to stop spam
    sleep(randint(2,10))
