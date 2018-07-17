import asyncio
import time
import zmq
import zmq.asyncio
import websockets

context = zmq.asyncio.Context()
socket_sub = context.socket(zmq.SUB)
socket_sub.setsockopt_string(zmq.SUBSCRIBE, "")
socket_sub.connect("tcp://127.0.0.1:5555")

pub_socket=context.socket(zmq.PUB)
pub_socket.bind("tcp://127.0.0.1:6666")


connections = set()
async def ws_connection(websocket, path):
    while True:
        await asyncio.sleep(1)
        print("Third worker Executed")
        connections.add(websocket)
        message = await websocket.recv()
        if message is None:
            break
        print(message)

async def recvonSub():
    while True:
        await asyncio.sleep(1)
        print("First Worker Executed")
        received_msg = await socket_sub.recv()
        print(received_msg)
        for ws in connections:
            await ws.send(received_msg)
        
async def sendtoSub():
    while True:
        await asyncio.sleep(1)
        print("Second Worker Executed")
        await pub_socket.send_string("Sending to sub")

loop = asyncio.get_event_loop()
try:
    start_server = websockets.serve(ws_connection, 'localhost', 8765)
    asyncio.ensure_future(start_server)
    asyncio.ensure_future(recvonSub())
    asyncio.ensure_future(sendtoSub())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()
