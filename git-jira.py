from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

app = ("__name__")

@app.route("/CreateJira", methods=["POST"])

def CreateJira():
    url = "https://rohitpandey-jira.atlassian.net/rest/api/3/issue"

    API_TOKEN = ""
    
    auth = HTTPBasicAuth("@gmail.com", API_TOKEN)
    
    headers = {
      "Accept": "application/json",
      "Content-Type": "application/json"
    }
    
    payload = json.dumps( {
      "fields": {
        
        "description": {
          "content": [
            {
              "content": [
                {
                  "text": "My first Jira-ticket",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },
        
        "issuetype": {
          "id": "10014"
        },
    
        "project": {
            "key": "RP"
        },
        "summary": "Main order flow broken",
        
      }
    })   
        
    
    response = requests.request(
       "POST",
       url,
       data=payload,
       headers=headers,
       auth=auth
    )
    
    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

    


app.run("0.0.0.0", PORT = 5000)
