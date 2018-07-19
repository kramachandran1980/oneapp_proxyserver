import asyncio
import time
import zmq
import zmq.asyncio
import transport_pb2 as transport
from google.protobuf.json_format import MessageToJson

context = zmq.asyncio.Context()
socket_sub = context.socket(zmq.SUB)
socket_sub.setsockopt_string(zmq.SUBSCRIBE, "")
socket_sub.connect("tcp://127.0.0.1:6666")

pub_socket=context.socket(zmq.PUB)
pub_socket.bind("tcp://127.0.0.1:5555")

def parse_protobuf(msg):
    msg_as_list = list(msg)
    if msg_as_list[0] == 0:
        print("This is a request messsage")
        del msg_as_list[0]
    request = transport.Request()
    request.ParseFromString(bytes(msg_as_list))
    print(request)
    #response = transport.ResponseOK()
    #response.header.request_uuid="2"
    #response.header.metadata.timestamp=1531946191

    #response.device_response.get_all_devices_response.devices.extend([])
    resp_msg=[2,10,14,10,9,9,0,80,219,255,254,74,118,66,18,1,49,26,217,3,10,214,3,10,136,2,10,1,57,18,10,55,56,51,52,53,49,53,57,55,50,26,15,82,97,108,108,121,32,84,97,98,108,101,32,72,117,98,34,7,10,5,49,46,48,46,50,41,0,0,88,56,30,74,118,66,48,1,58,7,10,5,49,46,48,46,51,64,0,77,0,0,0,0,130,1,192,1,10,1,56,18,10,55,56,51,52,53,49,53,57,55,49,26,17,82,97,108,108,121,32,77,105,99,32,80,111,100,32,72,117,98,34,7,10,5,49,46,48,46,50,41,0,0,88,56,30,74,118,66,48,1,58,7,10,5,49,46,48,46,51,64,0,77,0,0,0,0,130,1,58,10,2,49,50,18,10,55,56,51,52,53,49,53,57,55,53,26,13,82,97,108,108,121,32,77,105,99,32,80,111,100,34,7,10,5,49,46,48,46,50,41,0,0,88,56,30,74,118,66,48,0,64,0,77,0,0,0,0,130,1,58,10,2,49,51,18,10,55,56,51,52,53,49,53,57,55,54,26,13,82,97,108,108,121,32,77,105,99,32,80,111,100,34,7,10,5,49,46,48,46,50,41,0,0,88,56,30,74,118,66,48,0,64,0,77,0,0,0,0,10,200,1,10,1,56,18,10,55,56,51,52,53,49,53,57,55,49,26,17,82,97,108,108,121,32,68,105,115,112,108,97,121,32,72,117,98,34,7,10,5,49,46,48,46,50,41,0,0,88,56,30,74,118,66,48,0,64,0,77,0,0,0,0,130,1,75,10,2,49,48,18,10,55,56,51,52,53,49,53,57,55,51,26,12,82,97,108,108,121,32,67,97,109,101,114,97,34,25,10,5,49,46,48,46,50,18,6,49,46,50,51,46,49,26,3,50,46,49,34,3,49,46,49,41,0,0,88,56,30,74,118,66,48,0,64,0,77,0,0,0,0,130,1,58,10,2,49,49,18,10,55,56,51,52,53,49,53,57,55,52,26,13,82,97,108,108,121,32,83,112,101,97,107,101,114,34,7,10,5,49,46,48,46,50,41,0,0,88,56,30,74,118,66,48,0,64,0,77,0,0,0,0]
    pub_socket.send(bytes(resp_msg))
    
async def recvonSub():
    #while True:
    await asyncio.sleep(1)
    print("First Worker Executed")
    received_msg = await socket_sub.recv()
    print(received_msg)
    parse_protobuf(received_msg)
        
async def sendtoSub():
    while True:
        await asyncio.sleep(1)
        print("Second Worker Executed")
        await pub_socket.send_string("Sending to sub")

loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(recvonSub())
    #asyncio.ensure_future(sendtoSub())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()
