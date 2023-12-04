import asyncio
import json
import random
import requests
import websockets
#websocket client
SERCIVE_HOST = "127.0.0.1:8088"
async def Wsdemo():
    uri = "ws://{}/ws".format(SERCIVE_HOST)
    try:
        async with websockets.connect(uri) as websocket:
            while True:
                greeting = await websocket.recv()
                EventJson = json.loads(greeting)
                EventName = EventJson["CurrentPacket"]["EventName"]
                EventData = EventJson["CurrentPacket"]["EventData"]
                print(f"<{EventName} {greeting}")

    except Exception as e:
        # 断线重连
        t = random.randint(5, 8)
        print(f"< 超时重连中... { t}", e)
        await asyncio.sleep(t)
        await Wsdemo()
asyncio.get_event_loop().run_until_complete(Wsdemo())
