# -*- coding: utf-8 -*-
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#Example questions and issues

q = {
     
u'Social' : 'Should the government fund Planned Parenthood? Should the health insurance providers be required to cover birth control?',
            
u'Transportation': 'Should the government increase spending on public transportation?',

u'Science' : 'Should the government require children to be vaccinated against preventable diseases? Should producers be required to label genetically engineered foods?',
            
u'Education' : 'Should the government fund universal pre-school? Should we raise taxes to fund reduced interest rates on student loans?',
            
u'Environment' : 'Should disposable products (i.e. straws, cups) that contain less than 50% biodegradable material be banned? Should the government provide subsidies to renewable energy companies?',
                
u'Healthcare' : 'Should the government increase funding for healthcare for low income individuals? Should people be employed in order to receive Medicare?',
                
u'Criminal and Justice' : 'Should police officers be required to wear body cams? Should teachers be allowed to carry guns in schools?',
                        
u'Economic' : 'Should the government raise the minimum wage? Should the government raise taxes on the wealthiest 1%?',

u'Electoral' : 'Should a photo ID be required to vote? Should convicted felons have the right to vote?'
   
     }
#Firestore credentials
cred = credentials.Certificate("firstproject-1ead8-firebase-adminsdk-ttdfi-23840dd0c7.json") #Specific key for database with path

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()

#Creating collections and documents
db.collection(u'exmaple issues and questions').document(u'issues and examples').set(q)
