import requests
import json
import http.client

def ApiCaller() :
    url = "http://127.0.0.1:8088/v1/LuaApiCaller?funcname=MagicCgiCmd&timeout=10&qq=1411365785"

    payload = json.dumps({
       "CgiCmd": "ClusterInfo",
       "CgiRequest": {}
    })
    headers = {
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Content-Type': 'application/json'
}

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

def Friend_Get() :
    conn = http.client.HTTPSConnection("v1")
    payload = json.dumps({
       "CgiCmd": "GetFriendLists",
       "CgiRequest": {
          "LastUin": 0
       }
    })
    headers = {
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Content-Type': 'application/json'
    }
    conn.request("POST", "/LuaApiCaller?funcname=MagicCgiCmd&timeout=10&qq=%7B%7BQQBotUid%7D%7D", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
