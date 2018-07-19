import json
import transport_pb2 as transport
import common_pb2 as common
from google.protobuf import json_format
from google.protobuf.message import Message

response = transport.ResponseOK()

camera = {
    "device_uuid": "10",
    "pid": "7834515973",
    "name": "Rally Camera",
    "firmware": {
        "package_version": "1.0.2",
        "video_version": "1.23.1",
        "eeprom_version": "2.1",
        "ble_version": "1.1",
    },
    "last_firmware_update_time": "1531724400000",
    "is_firmware_update_available": False,
    "available_firmware": "null",
    "is_firmware_updating": False,
    "progress": "0.0",
    "error": "null",
    "children": []
}

speaker = {
    "device_uuid": "11",
    "pid": "7834515974",
    "name": "Rally Speaker",
    "firmware": {
        "package_version": "1.0.2",
    },
    "last_firmware_update_time": "1531724400000",
    "is_firmware_update_available": False,
    "available_firmware": "null",
    "is_firmware_updating": False,
    "progress": "0.0",
    "error": "null",
    "children": []
}

micPod0 = {
    "device_uuid": "12",
    "pid": "7834515975",
    "name": "Rally Mic Pod",
    "firmware": {
        "package_version": "1.0.2",
    },
    "last_firmware_update_time": "1531724400000",
    "is_firmware_update_available": False,
    "available_firmware": "null",
    "is_firmware_updating": False,
    "progress": "0.0",
    "error": "null",
    "children": [],
}

micPod1 = {
    "device_uuid": "13",
    "pid": "7834515976",
    "name": "Rally Mic Pod",
    "firmware": {
        "package_version": "1.0.2",
    },
    "last_firmware_update_time": "1531724400000",
    "is_firmware_update_available": False,
    "available_firmware": "null",
    "is_firmware_updating": False,
    "progress": "0.0",
    "error": "null",
    "children": [],
}


responseHeader = {
    "metadata": {
        "timestamp": "1531946191",
    },
    "request_uuid": "2",
}

deviceResponseHubs = {
    "get_all_devices_response": { 
        "devices": [micPod0, speaker] },
}

getAllDevicesResponseHubs = {
    "header": responseHeader,
    "device_response": deviceResponseHubs,
}

dict = json.dumps(getAllDevicesResponseHubs)
print dict

dict='{"header": {"request_uuid": "2", "metadata": {"timestamp": "1531946191"}}, "device_response": {"get_all_devices_response": {"devices": [{"is_firmware_updating": false, "device_uuid": "12", "pid": "7834515975", "available_firmware": "null", "children": [], "name": "Rally Mic Pod", "firmware": {"package_version": "1.0.2"}, "is_firmware_update_available": false, "error": "null", "progress": "0.0", "last_firmware_update_time": "1531724400000"}, {"is_firmware_updating": false, "device_uuid": "11", "pid": "7834515974", "available_firmware": "null", "children": [], "name": "Rally Speaker", "firmware": {"package_version": "1.0.2"}, "is_firmware_update_available": false, "error": "null", "progress": "0.0", "last_firmware_update_time": "1531724400000"}]}}}'


response.header.request_uuid="2"
response.header.metadata.timestamp=1531946191

response.device_response.get_all_devices_response.devices.extend([])
print response.SerializeToString()

