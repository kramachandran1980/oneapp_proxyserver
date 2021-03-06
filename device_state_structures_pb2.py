# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: device_state_structures.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2
import firmware_structures_pb2 as firmware__structures__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='device_state_structures.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1d\x64\x65vice_state_structures.proto\x1a\x0c\x63ommon.proto\x1a\x19\x66irmware_structures.proto\"\xc7\x02\n\x06\x44\x65vice\x12\x13\n\x0b\x64\x65vice_uuid\x18\x01 \x01(\t\x12\x0b\n\x03pid\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12+\n\x08\x66irmware\x18\x04 \x01(\x0b\x32\x19.ComponentFirmwareVersion\x12!\n\x19last_firmware_update_time\x18\x05 \x01(\x01\x12$\n\x1cis_firmware_update_available\x18\x06 \x01(\x08\x12\x35\n\x12\x61vailable_firmware\x18\x07 \x01(\x0b\x32\x19.ComponentFirmwareVersion\x12\x1c\n\x14is_firmware_updating\x18\x08 \x01(\x08\x12\x10\n\x08progress\x18\t \x01(\x02\x12\x15\n\x05\x65rror\x18\n \x01(\x0b\x32\x06.Error\x12\x19\n\x08\x63hildren\x18\x10 \x03(\x0b\x32\x07.Device\"9\n\x0b\x44\x65viceError\x12\x13\n\x0b\x64\x65vice_uuid\x18\x01 \x01(\t\x12\x15\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x06.Errorb\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,firmware__structures__pb2.DESCRIPTOR,])




_DEVICE = _descriptor.Descriptor(
  name='Device',
  full_name='Device',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_uuid', full_name='Device.device_uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pid', full_name='Device.pid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Device.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='firmware', full_name='Device.firmware', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_firmware_update_time', full_name='Device.last_firmware_update_time', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_firmware_update_available', full_name='Device.is_firmware_update_available', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='available_firmware', full_name='Device.available_firmware', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_firmware_updating', full_name='Device.is_firmware_updating', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='progress', full_name='Device.progress', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='Device.error', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='children', full_name='Device.children', index=10,
      number=16, type=11, cpp_type=10, label=3,
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
  serialized_start=75,
  serialized_end=402,
)


_DEVICEERROR = _descriptor.Descriptor(
  name='DeviceError',
  full_name='DeviceError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_uuid', full_name='DeviceError.device_uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='DeviceError.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=404,
  serialized_end=461,
)

_DEVICE.fields_by_name['firmware'].message_type = firmware__structures__pb2._COMPONENTFIRMWAREVERSION
_DEVICE.fields_by_name['available_firmware'].message_type = firmware__structures__pb2._COMPONENTFIRMWAREVERSION
_DEVICE.fields_by_name['error'].message_type = common__pb2._ERROR
_DEVICE.fields_by_name['children'].message_type = _DEVICE
_DEVICEERROR.fields_by_name['error'].message_type = common__pb2._ERROR
DESCRIPTOR.message_types_by_name['Device'] = _DEVICE
DESCRIPTOR.message_types_by_name['DeviceError'] = _DEVICEERROR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), dict(
  DESCRIPTOR = _DEVICE,
  __module__ = 'device_state_structures_pb2'
  # @@protoc_insertion_point(class_scope:Device)
  ))
_sym_db.RegisterMessage(Device)

DeviceError = _reflection.GeneratedProtocolMessageType('DeviceError', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEERROR,
  __module__ = 'device_state_structures_pb2'
  # @@protoc_insertion_point(class_scope:DeviceError)
  ))
_sym_db.RegisterMessage(DeviceError)


# @@protoc_insertion_point(module_scope)
