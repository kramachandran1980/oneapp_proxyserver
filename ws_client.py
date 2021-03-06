import asyncio
import websockets
import transport_pb2 as transport
from google.protobuf.json_format import MessageToJson

test_str="{\
    name: 'Mic Pod',\
    count: 2,\
    maxCount: 7,\
    img: 'assets/images/devices/pod.png',\
    thumb: 'assets/images/dashboard/devices/mic-pod-skus-289.png',\
    devices: [\
        {\
            id: '84938463',\
            status: 'ok',\
            connected: true,\
            firmware: '6.3.7',\
            lastUpdate: '2018-06-15T19:27:46.617Z',\
            settings: {\
                volume: getSlider(50),\
                treble: getSlider(50),\
                balance: getSlider(50),\
                bass: getSlider(50),\
                fader: getSlider(50),\
            },\
        },\
        {\
            id: '483729743',\
            status: 'ok',\
            connected: false,\
            firmware: '1.01.1',\
            lastUpdate: '2018-06-15T19:27:46.617Z',\
            settings: {\
                volume: getSlider(30),\
                treble: getSlider(20),\
                balance: getSlider(60),\
                bass: getSlider(30),\
                fader: getSlider(20),\
            },\
        },\
    ],\
}"

def parse_protobuf(msg):
    msg_as_list = list(msg)
    if msg_as_list[0] == 2:
        print("This is a response messsage")
        del msg_as_list[0]
    response = transport.ResponseOK()
    response.ParseFromString(bytes(msg_as_list))
    print(response)

async def hello():
    async with websockets.connect(
            'ws://localhost:8765') as websocket:
        while True: 
            await asyncio.sleep(1)
            message=[0, 10, 14, 10, 9, 9, 0, 144, 105, 105, 166, 74, 118, 66, 18, 1, 49, 26, 2, 10, 0]
            ba=bytes(message)
            print(ba)
            await websocket.send(ba)
            print(f"> {ba}")
            response = await websocket.recv()
            parse_protobuf(response)

loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(hello())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()
