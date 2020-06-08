import pandas as pd
import flask
import requests
from flask import Flask
from firebase import firebase
from datetime import date
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
from google.cloud import storage
# import datalab.storage as gcs

firebase = firebase.FirebaseApplication('https://xxy.firebaseio.com', None)

userList = pd.read_csv('users.csv')
userIds = userList['User ID']
rows_list = []

video_list = firebase.get("/quizzes",None)
col_list = []
for col in video_list.items():
    col_list.append(str(col[0]))
column = col_list
column.insert(0,'User ID')
column.append("Count")

def quiz_data(request):
    for user in userIds[0:]:
        print(str(user))
        
        user_dict = { "User ID" : str(int(user)) }
        user_cc = firebase.get("/users/"+ str(int(user)) +"/content_consumed/quiz", None)
        count = 0
        if (type(user_cc) == dict):
            for quiz in user_cc.items():
                count += 1
                try:
                  user_dict.update({ str(quiz[0]) : str(quiz[1]["first_at"]) })
                except:
                  print("Error")
                #print (user_dict[video[0]])
    #else:
        user_dict.update({ "Count" : str(count) })
        rows_list.append(user_dict)
        df = pd.DataFrame(rows_list, columns = column)
    today = date.today()
    myfile = str("quizdata_" + str(today) +".csv")
    #resp = flask.make_response(df.to_csv())
    

    
    storage_client = storage.Client.from_service_account_json('xxy.json')
    bucket = storage_client.get_bucket('staging.xxy.appspot.com')
    blob = bucket.blob(str(myfile))
    # df.to_csv('test.csv')
    blob.upload_from_string(df.to_csv(),content_type="text/csv")
    
    print('File {} uploaded to {}.'.format('test.csv',str(myfile)))
    return "Successfull!"

    
if __name__ == "__main__":
    
    app = Flask(__name__)

    @app.route('/')
    def index():
        return quiz_data(requests)
        

    #app.run('127.0.0.1', 8000, debug=True)

