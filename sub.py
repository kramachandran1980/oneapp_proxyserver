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
