import requests
import qrcode

login_url = "http://127.0.0.1:8088/v1/login/getqrcode?qq=1411365785&devicename=李三喵🐱&json=1"

payload={}
headers = {
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
}

response = requests.request("GET", login_url, headers=headers, data=payload)

response_json = response.json()
QRurl = response_json["ResponseData"]["QrUrl"] #存储登录二维码的url信息并用qrcode将其重新生成打印到终端

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=0,
)
qr.add_data(QRurl)
qr.print_ascii(invert = True)