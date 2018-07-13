import sys
import zmq

port = "5555"

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt_string(zmq.SUBSCRIBE, "")
pub_socket=context.socket(zmq.PUB)
pub_socket.bind("tcp://127.0.0.1:6666")

socket.connect ("tcp://127.0.0.1:%s" % port)

out_str="{\
    name: 'KRKR - Mic Pod',\
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

while True:
    received_message=socket.recv()
    print(received_message)
    response_message=out_str
    print("sending response")
    pub_socket.send_string(response_message)


