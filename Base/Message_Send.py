import requests
import json

url = "http://127.0.0.1:8088/v1/LuaApiCaller?funcname=MagicCgiCmd&timeout=10&qq=1411365785"

payload =json.dumps({
    "CgiCmd": "MessageSvc.PbSendMsg",
    "CgiRequest": {
        "ToUin":289581481 ,
        "ToType": 1,
        "Content": "你好"
    }
})
headers = {
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)