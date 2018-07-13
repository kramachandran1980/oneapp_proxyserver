import asyncio
import websockets
import zmq

context = zmq.Context()
sock = context.socket(zmq.PUB)
sock.bind("tcp://127.0.0.1:5555")
sub_sock=context.socket(zmq.SUB)
sub_sock.setsockopt_string(zmq.SUBSCRIBE, "")
sub_sock.connect("tcp://127.0.0.1:6666")

async def ws_connection(websocket, path):
    message = await websocket.recv()
    print(f"< {message}")

    sock.send_string(message)
    recd=sub_sock.recv()
    #print(recd)
    await websocket.send(recd)

start_server = websockets.serve(ws_connection, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

