# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


#Firestore credentials
cred = credentials.Certificate() #Specific key for database with path
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
db = firestore.client()

#Election candidates url
page = requests.get("https://info.kingcounty.gov/kcelections/Vote/contests/candidates.aspx?eid=21")
soup = BeautifulSoup(page.text, "html.parser")

#Info on offices up for election
role_list = soup.find_all(class_ = "list-group-item candidatelist-div")

#Find all offices
for item in role_list:
    running_for = item.h5.text
    can = item.find_all('a')
    can = can[:-1]
    #Find bio, pic, and name of candidates
    for per in can:
        candidates = per.text
        url = per.get("href")
        res = requests.get("https://voter.votewa.gov/elections/candidate.ashx?e=865&r=57369&b=45923&la=&c=17")
        data = res.json()
        photo = data[0]['statement']['Photo']
        statement = data[0]['statement']['Statement']
        soup = BeautifulSoup(statement, 'html.parser')
        bio = soup.get_text()
    
        ballot = {
         u'name': candidates,
         u'pic': photo,
         u'bio': bio       
         }
        
        #Send to database        
        db.collection(u'election').document(u'august-four').collection(u'offices').document(running_for).collection(u'candidates').document(candidates).set(ballot)
    

    
