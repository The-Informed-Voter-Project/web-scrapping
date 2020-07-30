# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


#calling url
page = requests.get("https://info.kingcounty.gov/kcelections/Vote/contests/ballotmeasures.aspx?lang=en-US&cid=99713&groupname=SpecialPurposeDistrict")
soup = BeautifulSoup(page.text, 'html.parser')


#pulling out needed info
ballot = soup.find(class_ = "well").get_text()
ballot = ballot.replace("\n", " ")
exp = soup.find(id = "explanatorystatement").get_text()
statement_for = soup.find(id = "statementfor").get_text()
statement_against = soup.find(id = "statementagainst").get_text()
pass_req = soup.find(id = "validationrules").get_text()

#Dictionary that will be avaliable in gcp
para_text = {
        
        u'title': ballot,
        u'explanation' : exp,
        u'statement-for' : statement_for,
        u'statement_against' : statement_against,
        u'pass-requirements' : pass_req
        
        }

#Uploading data
#Firestore credentials
'''NOTE: IN ORDER FOR YOU TO RUN THIS ON YOUR DEVICE, REPLACE THE JSON FILE WITH THE PATH/TO/FILE.JSON, WHERE JSON IS THE FILE CONTAINING YOUR PERSONAL KEYS FOR THE
PROJECT. SEE https://firebase.google.com/docs/admin/setup FOR MORE INFO. HAVE A GREAT DAY'''
cred = credentials.Certificate("firstproject-1ead8-firebase-adminsdk-ttdfi-23840dd0c7.json") #Specific key for database with path

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()

#Creating collections and documents
db.collection(u'election').document(u'august-four').collection(u'initiatives').document(u'initiative-a').set(para_text)


#Repeat for other initiatives 

#Pulling second url
page = requests.get("https://info.kingcounty.gov/kcelections/Vote/contests/ballotmeasures.aspx?lang=en-US&cid=99688&groupname=SpecialPurposeDistrict")
soup = BeautifulSoup(page.text, 'html.parser')


#pulling out needed info
ballot = soup.find(class_ = "well").get_text()
ballot = ballot.replace("\n", " ")
exp = soup.find(id = "explanatorystatement").get_text()
statement_for = soup.find(id = "statementfor").get_text()
statement_against = soup.find(id = "statementagainst").get_text()
pass_req = soup.find(id = "validationrules").get_text()

#Dictionary that will be avaliable in gcp
para_text = {
        
        u'title': ballot,
        u'explanation' : exp,
        u'statement-for' : statement_for,
        u'statement_against' : statement_against,
        u'pass-requirements' : pass_req
        
        }


#Uploading data
#Creating collections and documents
db.collection(u'election').document(u'august-four').collection(u'initiatives').document(u'initiative-b').set(para_text)


#Pulling third url
page = requests.get("https://info.kingcounty.gov/kcelections/Vote/contests/ballotmeasures.aspx?lang=en-US&cid=99712&groupname=SpecialPurposeDistrict")
soup = BeautifulSoup(page.text, 'html.parser')


#pulling out needed info
ballot = soup.find(class_ = "well").get_text()
ballot = ballot.replace("\n", " ")
exp = soup.find(id = "explanatorystatement").get_text()
statement_for = soup.find(id = "statementfor").get_text()
statement_against = soup.find(id = "statementagainst").get_text()
pass_req = soup.find(id = "validationrules").get_text()

#Dictionary that will be avaliable in gcp
para_text = {
        
        u'title': ballot,
        u'explanation' : exp,
        u'statement-for' : statement_for,
        u'statement_against' : statement_against,
        u'pass-requirements' : pass_req
        
        }


#Uploading data
#Creating collections and documents
db.collection(u'election').document(u'august-four').collection(u'initiatives').document(u'initiative-c').set(para_text)


