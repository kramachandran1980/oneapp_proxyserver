# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: firmware_requests.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import firmware_structures_pb2 as firmware__structures__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='firmware_requests.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17\x66irmware_requests.proto\x1a\x19\x66irmware_structures.proto\"\x17\n\x15GetAllFirmwareRequest\"K\n\x16GetAllFirmwareResponse\x12\x31\n\x11\x66irmware_versions\x18\x01 \x03(\x0b\x32\x16.DeviceFirmwareVersion\"-\n\x16GetFirmwareByIdRequest\x12\x13\n\x0b\x64\x65vice_uuid\x18\x01 \x01(\t\"K\n\x17GetFirmwareByIdResponse\x12\x30\n\x10\x66irmware_version\x18\x01 \x01(\x0b\x32\x16.DeviceFirmwareVersion\"Z\n\x1aGetFirmwareByFilterRequest\x12\x13\n\x0b\x64\x65vice_uuid\x18\x01 \x03(\t\x12\x12\n\ndevice_pid\x18\x02 \x03(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x03 \x03(\t\"P\n\x1bGetFirmwareByFilterResponse\x12\x31\n\x11\x66irmware_versions\x18\x01 \x03(\x0b\x32\x16.DeviceFirmwareVersion\"\"\n GetFirmwareUpdateProgressRequest\"S\n!GetFirmwareUpdateProgressResponse\x12.\n\x07updates\x18\x01 \x03(\x0b\x32\x1d.DeviceFirmwareUpdateProgress\"\x1a\n\x18UpdateAllFirmwareRequest\"K\n\x19UpdateAllFirmwareResponse\x12.\n\x07updates\x18\x01 \x03(\x0b\x32\x1d.DeviceFirmwareUpdateProgress\"0\n\x19UpdateFirmwareByIdRequest\x12\x13\n\x0b\x64\x65vice_uuid\x18\x01 \x01(\t\"K\n\x1aUpdateFirmwareByIdResponse\x12-\n\x06update\x18\x01 \x01(\x0b\x32\x1d.DeviceFirmwareUpdateProgress\"]\n\x1dUpdateFirmwareByFilterRequest\x12\x13\n\x0b\x64\x65vice_uuid\x18\x01 \x03(\t\x12\x12\n\ndevice_pid\x18\x02 \x03(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x03 \x03(\t\"P\n\x1eUpdateFirmwareByFilterResponse\x12.\n\x07updates\x18\x01 \x03(\x0b\x32\x1d.DeviceFirmwareUpdateProgress\"\x88\x03\n\x0f\x46irmwareRequest\x12\x32\n\x10get_all_firmware\x18\x01 \x01(\x0b\x32\x16.GetAllFirmwareRequestH\x00\x12\x35\n\x12get_firmware_by_id\x18\x02 \x01(\x0b\x32\x17.GetFirmwareByIdRequestH\x00\x12=\n\x16get_firmware_by_filter\x18\x03 \x01(\x0b\x32\x1b.GetFirmwareByFilterRequestH\x00\x12I\n\x1cget_firmware_update_progress\x18\x04 \x01(\x0b\x32!.GetFirmwareUpdateProgressRequestH\x00\x12;\n\x15update_firmware_by_id\x18\x05 \x01(\x0b\x32\x1a.UpdateFirmwareByIdRequestH\x00\x12\x38\n\x13update_all_firmware\x18\x06 \x01(\x0b\x32\x19.UpdateAllFirmwareRequestH\x00\x42\t\n\x07request\"\xc6\x03\n\x10\x46irmwareResponse\x12<\n\x19get_all_firmware_response\x18\x01 \x01(\x0b\x32\x17.GetAllFirmwareResponseH\x00\x12?\n\x1bget_firmware_by_id_response\x18\x02 \x01(\x0b\x32\x18.GetFirmwareByIdResponseH\x00\x12G\n\x1fget_firmware_by_filter_response\x18\x03 \x01(\x0b\x32\x1c.GetFirmwareByFilterResponseH\x00\x12S\n%get_firmware_update_progress_response\x18\x04 \x01(\x0b\x32\".GetFirmwareUpdateProgressResponseH\x00\x12\x45\n\x1eupdate_firmware_by_id_response\x18\x05 \x01(\x0b\x32\x1b.UpdateFirmwareByIdResponseH\x00\x12\x42\n\x1cupdate_all_firmware_response\x18\x06 \x01(\x0b\x32\x1a.UpdateAllFirmwareResponseH\x00\x42\n\n\x08response\"J\n\x15\x46irmwareResponseError\x12(\n\x0e\x66irmware_error\x18\x01 \x01(\x0b\x32\x0e.FirmwareErrorH\x00\x42\x07\n\x05\x65rrorb\x06proto3')
  ,
  dependencies=[firmware__structures__pb2.DESCRIPTOR,])




_GETALLFIRMWAREREQUEST = _descriptor.Descriptor(
  name='GetAllFirmwareRequest',
  full_name='GetAllFirmwareRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=77,
)


_GETALLFIRMWARERESPONSE = _descriptor.Descriptor(
  name='GetAllFirmwareResponse',
  full_name='GetAllFirmwareResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='firmware_versions', full_name='GetAllFirmwareResponse.firmware_versions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=154,
)


_GETFIRMWAREBYIDREQUEST = _descriptor.Descriptor(
  name='GetFirmwareByIdRequest',
  full_name='GetFirmwareByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_uuid', full_name='GetFirmwareByIdRequest.device_uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=156,
  serialized_end=201,
)


_GETFIRMWAREBYIDRESPONSE = _descriptor.Descriptor(
  name='GetFirmwareByIdResponse',
  full_name='GetFirmwareByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='firmware_version', full_name='GetFirmwareByIdResponse.firmware_version', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=203,
  serialized_end=278,
)


_GETFIRMWAREBYFILTERREQUEST = _descriptor.Descriptor(
  name='GetFirmwareByFilterRequest',
  full_name='GetFirmwareByFilterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_uuid', full_name='GetFirmwareByFilterRequest.device_uuid', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_pid', full_name='GetFirmwareByFilterRequest.device_pid', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_name', full_name='GetFirmwareByFilterRequest.device_name', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=280,
  serialized_end=370,
)


_GETFIRMWAREBYFILTERRESPONSE = _descriptor.Descriptor(
  name='GetFirmwareByFilterResponse',
  full_name='GetFirmwareByFilterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='firmware_versions', full_name='GetFirmwareByFilterResponse.firmware_versions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=372,
  serialized_end=452,
)


_GETFIRMWAREUPDATEPROGRESSREQUEST = _descriptor.Descriptor(
  name='GetFirmwareUpdateProgressRequest',
  full_name='GetFirmwareUpdateProgressRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=454,
  serialized_end=488,
)


_GETFIRMWAREUPDATEPROGRESSRESPONSE = _descriptor.Descriptor(
  name='GetFirmwareUpdateProgressResponse',
  full_name='GetFirmwareUpdateProgressResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='updates', full_name='GetFirmwareUpdateProgressResponse.updates', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=490,
  serialized_end=573,
)


_UPDATEALLFIRMWAREREQUEST = _descriptor.Descriptor(
  name='UpdateAllFirmwareRequest',
  full_name='UpdateAllFirmwareRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=575,
  serialized_end=601,
)


_UPDATEALLFIRMWARERESPONSE = _descriptor.Descriptor(
  name='UpdateAllFirmwareResponse',
  full_name='UpdateAllFirmwareResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='updates', full_name='UpdateAllFirmwareResponse.updates', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=603,
  serialized_end=678,
)


_UPDATEFIRMWAREBYIDREQUEST = _descriptor.Descriptor(
  name='UpdateFirmwareByIdRequest',
  full_name='UpdateFirmwareByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_uuid', full_name='UpdateFirmwareByIdRequest.device_uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=680,
  serialized_end=728,
)


_UPDATEFIRMWAREBYIDRESPONSE = _descriptor.Descriptor(
  name='UpdateFirmwareByIdResponse',
  full_name='UpdateFirmwareByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update', full_name='UpdateFirmwareByIdResponse.update', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=730,
  serialized_end=805,
)


_UPDATEFIRMWAREBYFILTERREQUEST = _descriptor.Descriptor(
  name='UpdateFirmwareByFilterRequest',
  full_name='UpdateFirmwareByFilterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_uuid', full_name='UpdateFirmwareByFilterRequest.device_uuid', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_pid', full_name='UpdateFirmwareByFilterRequest.device_pid', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_name', full_name='UpdateFirmwareByFilterRequest.device_name', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=807,
  serialized_end=900,
)


_UPDATEFIRMWAREBYFILTERRESPONSE = _descriptor.Descriptor(
  name='UpdateFirmwareByFilterResponse',
  full_name='UpdateFirmwareByFilterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='updates', full_name='UpdateFirmwareByFilterResponse.updates', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=902,
  serialized_end=982,
)


_FIRMWAREREQUEST = _descriptor.Descriptor(
  name='FirmwareRequest',
  full_name='FirmwareRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='get_all_firmware', full_name='FirmwareRequest.get_all_firmware', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_firmware_by_id', full_name='FirmwareRequest.get_firmware_by_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_firmware_by_filter', full_name='FirmwareRequest.get_firmware_by_filter', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_firmware_update_progress', full_name='FirmwareRequest.get_firmware_update_progress', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_firmware_by_id', full_name='FirmwareRequest.update_firmware_by_id', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_all_firmware', full_name='FirmwareRequest.update_all_firmware', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='request', full_name='FirmwareRequest.request',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=985,
  serialized_end=1377,
)


_FIRMWARERESPONSE = _descriptor.Descriptor(
  name='FirmwareResponse',
  full_name='FirmwareResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='get_all_firmware_response', full_name='FirmwareResponse.get_all_firmware_response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_firmware_by_id_response', full_name='FirmwareResponse.get_firmware_by_id_response', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_firmware_by_filter_response', full_name='FirmwareResponse.get_firmware_by_filter_response', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_firmware_update_progress_response', full_name='FirmwareResponse.get_firmware_update_progress_response', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_firmware_by_id_response', full_name='FirmwareResponse.update_firmware_by_id_response', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_all_firmware_response', full_name='FirmwareResponse.update_all_firmware_response', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='response', full_name='FirmwareResponse.response',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1380,
  serialized_end=1834,
)


_FIRMWARERESPONSEERROR = _descriptor.Descriptor(
  name='FirmwareResponseError',
  full_name='FirmwareResponseError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='firmware_error', full_name='FirmwareResponseError.firmware_error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='error', full_name='FirmwareResponseError.error',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1836,
  serialized_end=1910,
)

_GETALLFIRMWARERESPONSE.fields_by_name['firmware_versions'].message_type = firmware__structures__pb2._DEVICEFIRMWAREVERSION
_GETFIRMWAREBYIDRESPONSE.fields_by_name['firmware_version'].message_type = firmware__structures__pb2._DEVICEFIRMWAREVERSION
_GETFIRMWAREBYFILTERRESPONSE.fields_by_name['firmware_versions'].message_type = firmware__structures__pb2._DEVICEFIRMWAREVERSION
_GETFIRMWAREUPDATEPROGRESSRESPONSE.fields_by_name['updates'].message_type = firmware__structures__pb2._DEVICEFIRMWAREUPDATEPROGRESS
_UPDATEALLFIRMWARERESPONSE.fields_by_name['updates'].message_type = firmware__structures__pb2._DEVICEFIRMWAREUPDATEPROGRESS
_UPDATEFIRMWAREBYIDRESPONSE.fields_by_name['update'].message_type = firmware__structures__pb2._DEVICEFIRMWAREUPDATEPROGRESS
_UPDATEFIRMWAREBYFILTERRESPONSE.fields_by_name['updates'].message_type = firmware__structures__pb2._DEVICEFIRMWAREUPDATEPROGRESS
_FIRMWAREREQUEST.fields_by_name['get_all_firmware'].message_type = _GETALLFIRMWAREREQUEST
_FIRMWAREREQUEST.fields_by_name['get_firmware_by_id'].message_type = _GETFIRMWAREBYIDREQUEST
_FIRMWAREREQUEST.fields_by_name['get_firmware_by_filter'].message_type = _GETFIRMWAREBYFILTERREQUEST
_FIRMWAREREQUEST.fields_by_name['get_firmware_update_progress'].message_type = _GETFIRMWAREUPDATEPROGRESSREQUEST
_FIRMWAREREQUEST.fields_by_name['update_firmware_by_id'].message_type = _UPDATEFIRMWAREBYIDREQUEST
_FIRMWAREREQUEST.fields_by_name['update_all_firmware'].message_type = _UPDATEALLFIRMWAREREQUEST
_FIRMWAREREQUEST.oneofs_by_name['request'].fields.append(
  _FIRMWAREREQUEST.fields_by_name['get_all_firmware'])
_FIRMWAREREQUEST.fields_by_name['get_all_firmware'].containing_oneof = _FIRMWAREREQUEST.oneofs_by_name['request']
_FIRMWAREREQUEST.oneofs_by_name['request'].fields.append(
  _FIRMWAREREQUEST.fields_by_name['get_firmware_by_id'])
_FIRMWAREREQUEST.fields_by_name['get_firmware_by_id'].containing_oneof = _FIRMWAREREQUEST.oneofs_by_name['request']
_FIRMWAREREQUEST.oneofs_by_name['request'].fields.append(
  _FIRMWAREREQUEST.fields_by_name['get_firmware_by_filter'])
_FIRMWAREREQUEST.fields_by_name['get_firmware_by_filter'].containing_oneof = _FIRMWAREREQUEST.oneofs_by_name['request']
_FIRMWAREREQUEST.oneofs_by_name['request'].fields.append(
  _FIRMWAREREQUEST.fields_by_name['get_firmware_update_progress'])
_FIRMWAREREQUEST.fields_by_name['get_firmware_update_progress'].containing_oneof = _FIRMWAREREQUEST.oneofs_by_name['request']
_FIRMWAREREQUEST.oneofs_by_name['request'].fields.append(
  _FIRMWAREREQUEST.fields_by_name['update_firmware_by_id'])
_FIRMWAREREQUEST.fields_by_name['update_firmware_by_id'].containing_oneof = _FIRMWAREREQUEST.oneofs_by_name['request']
_FIRMWAREREQUEST.oneofs_by_name['request'].fields.append(
  _FIRMWAREREQUEST.fields_by_name['update_all_firmware'])
_FIRMWAREREQUEST.fields_by_name['update_all_firmware'].containing_oneof = _FIRMWAREREQUEST.oneofs_by_name['request']
_FIRMWARERESPONSE.fields_by_name['get_all_firmware_response'].message_type = _GETALLFIRMWARERESPONSE
_FIRMWARERESPONSE.fields_by_name['get_firmware_by_id_response'].message_type = _GETFIRMWAREBYIDRESPONSE
_FIRMWARERESPONSE.fields_by_name['get_firmware_by_filter_response'].message_type = _GETFIRMWAREBYFILTERRESPONSE
_FIRMWARERESPONSE.fields_by_name['get_firmware_update_progress_response'].message_type = _GETFIRMWAREUPDATEPROGRESSRESPONSE
_FIRMWARERESPONSE.fields_by_name['update_firmware_by_id_response'].message_type = _UPDATEFIRMWAREBYIDRESPONSE
_FIRMWARERESPONSE.fields_by_name['update_all_firmware_response'].message_type = _UPDATEALLFIRMWARERESPONSE
_FIRMWARERESPONSE.oneofs_by_name['response'].fields.append(
  _FIRMWARERESPONSE.fields_by_name['get_all_firmware_response'])
_FIRMWARERESPONSE.fields_by_name['get_all_firmware_response'].containing_oneof = _FIRMWARERESPONSE.oneofs_by_name['response']
_FIRMWARERESPONSE.oneofs_by_name['response'].fields.append(
  _FIRMWARERESPONSE.fields_by_name['get_firmware_by_id_response'])
_FIRMWARERESPONSE.fields_by_name['get_firmware_by_id_response'].containing_oneof = _FIRMWARERESPONSE.oneofs_by_name['response']
_FIRMWARERESPONSE.oneofs_by_name['response'].fields.append(
  _FIRMWARERESPONSE.fields_by_name['get_firmware_by_filter_response'])
_FIRMWARERESPONSE.fields_by_name['get_firmware_by_filter_response'].containing_oneof = _FIRMWARERESPONSE.oneofs_by_name['response']
_FIRMWARERESPONSE.oneofs_by_name['response'].fields.append(
  _FIRMWARERESPONSE.fields_by_name['get_firmware_update_progress_response'])
_FIRMWARERESPONSE.fields_by_name['get_firmware_update_progress_response'].containing_oneof = _FIRMWARERESPONSE.oneofs_by_name['response']
_FIRMWARERESPONSE.oneofs_by_name['response'].fields.append(
  _FIRMWARERESPONSE.fields_by_name['update_firmware_by_id_response'])
_FIRMWARERESPONSE.fields_by_name['update_firmware_by_id_response'].containing_oneof = _FIRMWARERESPONSE.oneofs_by_name['response']
_FIRMWARERESPONSE.oneofs_by_name['response'].fields.append(
  _FIRMWARERESPONSE.fields_by_name['update_all_firmware_response'])
_FIRMWARERESPONSE.fields_by_name['update_all_firmware_response'].containing_oneof = _FIRMWARERESPONSE.oneofs_by_name['response']
_FIRMWARERESPONSEERROR.fields_by_name['firmware_error'].message_type = firmware__structures__pb2._FIRMWAREERROR
_FIRMWARERESPONSEERROR.oneofs_by_name['error'].fields.append(
  _FIRMWARERESPONSEERROR.fields_by_name['firmware_error'])
_FIRMWARERESPONSEERROR.fields_by_name['firmware_error'].containing_oneof = _FIRMWARERESPONSEERROR.oneofs_by_name['error']
DESCRIPTOR.message_types_by_name['GetAllFirmwareRequest'] = _GETALLFIRMWAREREQUEST
DESCRIPTOR.message_types_by_name['GetAllFirmwareResponse'] = _GETALLFIRMWARERESPONSE
DESCRIPTOR.message_types_by_name['GetFirmwareByIdRequest'] = _GETFIRMWAREBYIDREQUEST
DESCRIPTOR.message_types_by_name['GetFirmwareByIdResponse'] = _GETFIRMWAREBYIDRESPONSE
DESCRIPTOR.message_types_by_name['GetFirmwareByFilterRequest'] = _GETFIRMWAREBYFILTERREQUEST
DESCRIPTOR.message_types_by_name['GetFirmwareByFilterResponse'] = _GETFIRMWAREBYFILTERRESPONSE
DESCRIPTOR.message_types_by_name['GetFirmwareUpdateProgressRequest'] = _GETFIRMWAREUPDATEPROGRESSREQUEST
DESCRIPTOR.message_types_by_name['GetFirmwareUpdateProgressResponse'] = _GETFIRMWAREUPDATEPROGRESSRESPONSE
DESCRIPTOR.message_types_by_name['UpdateAllFirmwareRequest'] = _UPDATEALLFIRMWAREREQUEST
DESCRIPTOR.message_types_by_name['UpdateAllFirmwareResponse'] = _UPDATEALLFIRMWARERESPONSE
DESCRIPTOR.message_types_by_name['UpdateFirmwareByIdRequest'] = _UPDATEFIRMWAREBYIDREQUEST
DESCRIPTOR.message_types_by_name['UpdateFirmwareByIdResponse'] = _UPDATEFIRMWAREBYIDRESPONSE
DESCRIPTOR.message_types_by_name['UpdateFirmwareByFilterRequest'] = _UPDATEFIRMWAREBYFILTERREQUEST
DESCRIPTOR.message_types_by_name['UpdateFirmwareByFilterResponse'] = _UPDATEFIRMWAREBYFILTERRESPONSE
DESCRIPTOR.message_types_by_name['FirmwareRequest'] = _FIRMWAREREQUEST
DESCRIPTOR.message_types_by_name['FirmwareResponse'] = _FIRMWARERESPONSE
DESCRIPTOR.message_types_by_name['FirmwareResponseError'] = _FIRMWARERESPONSEERROR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAllFirmwareRequest = _reflection.GeneratedProtocolMessageType('GetAllFirmwareRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETALLFIRMWAREREQUEST,
  __module__ = 'firmware_requests_pb2'
  # @@protoc_insertion_point(class_scope:GetAllFirmwareRequest)
  ))
_sym_db.RegisterMessage(GetAllFirmwareRequest)

GetAllFirmwareResponse = _reflection.GeneratedProtocolMessageType('GetAllFirmwareResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETALLFIRMWARERESPONSE,
  __module__ = 'firmware_requests_pb2'
  # @@protoc_insertion_point(class_scope:GetAllFirmwareResponse)
  ))
_sym_db.RegisterMessage(GetAllFirmwareResponse)

GetFirmwareByIdRequest = _reflection.GeneratedProtocolMessageType('GetFirmwareByIdRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETFIRMWAREBYIDREQUEST,
  __module__ = 'firmware_requests_pb2'
  # @@protoc_insertion_point(class_scope:GetFirmwareByIdRequest)
  ))
_sym_db.RegisterMessage(GetFirmwareByIdRequest)

GetFirmwareByIdResponse = _reflection.GeneratedProtocolMessageType('GetFirmwareByIdResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETFIRMWAREBYIDRESPONSE,
  __module__ = 'firmware_requests_pb2'
  # @@protoc_insertion_point(class_scope:GetFirmwareByIdResponse)
  ))
_sym_db.RegisterMessage(GetFirmwareByIdResponse)

GetFirmwareByFilterRequest = _reflection.GeneratedProtocolMessageType('GetFirmwareByFilterRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETFIRMWAREBYFILTERREQUEST,
  __module__ = 'firmware_requests_pb2'
  # @@protoc_insertion_point(class_scope:GetFirmwareByFilterRequest)
  ))
_sym_db.RegisterMessage(GetFirmwareByFilterRequest)

GetFirmwareByFilterResponse = _reflection.GeneratedProtocolMessageType('GetFirmwareByFilterResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETFIRMWAREBYFILTERRESPONSE,
  __module__ = 'firmware_requests_pb2'
  # @@protoc_insertion_point(class_scope:GetFirmwareByFilterResponse)
  ))
_sym_db.RegisterMessage(GetFirmwareByFilterResponse)

GetFirmwareUpdateProgressRequest = _reflection.GeneratedProtocolMessageType('GetFirmwareUpdateProgressRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETFIRMWAREUPDATEPROGRESSREQUEST,
  __module__ = 'firmware_requests_pb2'
  # @@protoc_insertion_point(class_scope:GetFirmwareUpdateProgressRequest)
  ))
_sym_db.RegisterMessage(GetFirmwareUpdateProgressRequest)

GetFirmwareUpdateProgressResponse = _reflection.GeneratedProtocolMessageType('GetFirmwareUpdateProgressResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETFIRMWAREUPDATEPROGRESSRESPONSE,
  __module__ = 'firmware_requests_pb2'
  # @@protoc_insertion_point(class_scope:GetFirmwareUpdateProgressResponse)
  ))
_sym_db.RegisterMessage(GetFirmwareUpdateProgressResponse)

UpdateAllFirmwareRequest = _reflection.GeneratedProtocolMessageType('UpdateAllFirmwareRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEALLFIRMWAREREQUEST,
  __module__ = 'firmware_requests_pb2'
  # @@protoc_insertion_point(class_scope:UpdateAllFirmwareRequest)
  ))
_sym_db.RegisterMessage(UpdateAllFirmwareRequest)

UpdateAllFirmwareResponse = _reflection.GeneratedProtocolMessageType('UpdateAllFirmwareResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEALLFIRMWARERESPONSE,
  __module__ = 'firmware_requests_pb2'
  # @@protoc_insertion_point(class_scope:UpdateAllFirmwareResponse)
  ))
_sym_db.RegisterMessage(UpdateAllFirmwareResponse)

UpdateFirmwareByIdRequest = _reflection.GeneratedProtocolMessageType('UpdateFirmwareByIdRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEFIRMWAREBYIDREQUEST,
  __module__ = 'firmware_requests_pb2'
  # @@protoc_insertion_point(class_scope:UpdateFirmwareByIdRequest)
  ))
_sym_db.RegisterMessage(UpdateFirmwareByIdRequest)

UpdateFirmwareByIdResponse = _reflection.GeneratedProtocolMessageType('UpdateFirmwareByIdResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEFIRMWAREBYIDRESPONSE,
  __module__ = 'firmware_requests_pb2'
  # @@protoc_insertion_point(class_scope:UpdateFirmwareByIdResponse)
  ))
_sym_db.RegisterMessage(UpdateFirmwareByIdResponse)

UpdateFirmwareByFilterRequest = _reflection.GeneratedProtocolMessageType('UpdateFirmwareByFilterRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEFIRMWAREBYFILTERREQUEST,
  __module__ = 'firmware_requests_pb2'
  # @@protoc_insertion_point(class_scope:UpdateFirmwareByFilterRequest)
  ))
_sym_db.RegisterMessage(UpdateFirmwareByFilterRequest)

UpdateFirmwareByFilterResponse = _reflection.GeneratedProtocolMessageType('UpdateFirmwareByFilterResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEFIRMWAREBYFILTERRESPONSE,
  __module__ = 'firmware_requests_pb2'
  # @@protoc_insertion_point(class_scope:UpdateFirmwareByFilterResponse)
  ))
_sym_db.RegisterMessage(UpdateFirmwareByFilterResponse)

FirmwareRequest = _reflection.GeneratedProtocolMessageType('FirmwareRequest', (_message.Message,), dict(
  DESCRIPTOR = _FIRMWAREREQUEST,
  __module__ = 'firmware_requests_pb2'
  # @@protoc_insertion_point(class_scope:FirmwareRequest)
  ))
_sym_db.RegisterMessage(FirmwareRequest)

FirmwareResponse = _reflection.GeneratedProtocolMessageType('FirmwareResponse', (_message.Message,), dict(
  DESCRIPTOR = _FIRMWARERESPONSE,
  __module__ = 'firmware_requests_pb2'
  # @@protoc_insertion_point(class_scope:FirmwareResponse)
  ))
_sym_db.RegisterMessage(FirmwareResponse)

FirmwareResponseError = _reflection.GeneratedProtocolMessageType('FirmwareResponseError', (_message.Message,), dict(
  DESCRIPTOR = _FIRMWARERESPONSEERROR,
  __module__ = 'firmware_requests_pb2'
  # @@protoc_insertion_point(class_scope:FirmwareResponseError)
  ))
_sym_db.RegisterMessage(FirmwareResponseError)


# @@protoc_insertion_point(module_scope)