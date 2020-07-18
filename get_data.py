# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import boto3


#calling url
page = requests.get("https://info.kingcounty.gov/kcelections/Vote/contests/ballotmeasures.aspx?lang=en-US&cid=99713&groupname=SpecialPurposeDistrict")
soup = BeautifulSoup(page.text, 'html.parser')

#pulling out needed info
ballot = soup.find(class_ = "well").get_text()
ballot = ballot.replace("\n", " ")
exp = soup.find_all(class_ = "panel-title")[0].get_text() + soup.find(id = "explanatorystatement").get_text()
statement_for = soup.find_all(class_ = "panel-title")[1].get_text() + soup.find(id = "statementfor").get_text()
statement_against = soup.find_all(class_ = "panel-title")[2].get_text() + soup.find(id = "statementagainst").get_text()
pass_req = soup.find_all(class_ = "panel-title")[4].get_text() + soup.find(id = "validationrules").get_text()

paragraph_text = ballot + exp + statement_for + statement_against + pass_req


#creating AWS bucket
s3 = boto3.client('s3')
myBucket = "ballot-info"

#sending info to bucket
s3.create_bucket(Bucket = myBucket, ACL = 'public-read')
s3.put_object(Bucket = myBucket, Key = 'KCE-ballot-2', Body = paragraph_text, ACL = "public-read")
